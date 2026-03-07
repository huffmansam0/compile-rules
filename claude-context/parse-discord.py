"""
Parse a DiscordChatExporter HTML export into a clean Markdown file.

Usage:
    python claude-context/parse-discord.py <input.html> <output.md>

Produces one block per message:
    ### AuthorName — 10/4/2025 12:20 PM
    Message content here...

Works with exports from DiscordChatExporter (Tyrrrz).
Uses regex-based extraction since the HTML is predictably structured.
"""

import re
import sys
from html import unescape


def strip_html(text):
    """Convert HTML content to plain-ish markdown text."""
    # Preserve line breaks
    text = re.sub(r"<br\s*/?>", "\n", text)

    # Convert formatting tags to markdown
    text = re.sub(r"<strong>(.*?)</strong>", r"**\1**", text, flags=re.DOTALL)
    text = re.sub(r"<em>(.*?)</em>", r"*\1*", text, flags=re.DOTALL)
    text = re.sub(r"<s>(.*?)</s>", r"~~\1~~", text, flags=re.DOTALL)

    # Convert links - keep the URL
    text = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>.*?</a>', r"\1", text, flags=re.DOTALL)

    # Convert emoji images to alt text
    text = re.sub(r'<img[^>]*alt="([^"]*)"[^>]*/?\s*>', r"\1", text)
    text = re.sub(r'<img[^>]*/?\s*>', "", text)

    # Blockquotes
    text = re.sub(
        r'<div class="chatlog__markdown-quote[^"]*">.*?<div class="chatlog__markdown-quote-content">(.*?)</div>\s*</div>',
        lambda m: "> " + m.group(1).strip(),
        text,
        flags=re.DOTALL,
    )

    # Code blocks
    text = re.sub(
        r'<code class="[^"]*pre--multiline[^"]*">(.*?)</code>',
        lambda m: "```\n" + m.group(1).strip() + "\n```",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r'<code class="[^"]*pre--inline[^"]*">(.*?)</code>',
        r"`\1`",
        text,
        flags=re.DOTALL,
    )

    # Mentions
    text = re.sub(r'<span class="chatlog__markdown-mention[^"]*">(@[^<]*)</span>', r"\1", text)

    # Spoilers - just show the text
    text = re.sub(r'<span class="chatlog__markdown-spoiler[^"]*">(.*?)</span>', r"[spoiler: \1]", text, flags=re.DOTALL)

    # Strip remaining HTML tags
    text = re.sub(r"<[^>]+>", "", text)

    # Unescape HTML entities
    text = unescape(text)

    # Clean up whitespace (preserve intentional newlines)
    text = re.sub(r" +", " ", text)
    text = re.sub(r"\n ", "\n", text)
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def parse_discord_html(html):
    """Parse all messages from a DiscordChatExporter HTML file."""
    messages = []

    # Split into message groups
    group_splits = re.split(r"<div class=chatlog__message-group>", html)

    for group_html in group_splits[1:]:  # Skip everything before first group
        # Extract group-level author info (from the first message's header)
        author_match = re.search(r'class=chatlog__author[^>]*title=(\S+)[^>]*data-user-id=\d+>([^<]*)</span>', group_html)
        if not author_match:
            # Try quoted attribute version
            author_match = re.search(r'class="chatlog__author"[^>]*title="([^"]*)"[^>]*>([^<]*)</span>', group_html)

        group_author_title = author_match.group(1) if author_match else "Unknown"
        group_author_display = author_match.group(2).strip() if author_match else "Unknown"

        # Extract group-level timestamp
        ts_match = re.search(r'class=chatlog__timestamp title="([^"]*)"', group_html)
        if not ts_match:
            ts_match = re.search(r'class="chatlog__timestamp"[^>]*title="([^"]*)"', group_html)
        group_timestamp = ts_match.group(1) if ts_match else ""

        # Find all message containers in this group
        container_pattern = re.compile(
            r'data-message-id=(\d+)>(.*?)(?=data-message-id=|$)',
            re.DOTALL,
        )

        for container_match in container_pattern.finditer(group_html):
            msg_id = container_match.group(1)
            container_html = container_match.group(2)

            # Check for per-message author (replies from different users in same group)
            msg_author_match = re.search(r'class=chatlog__author[^>]*title=(\S+)', container_html)
            if msg_author_match:
                author = msg_author_match.group(1)
            else:
                author = group_author_title

            # Check for per-message timestamp
            msg_ts_match = re.search(r'class=chatlog__timestamp title="([^"]*)"', container_html)
            if msg_ts_match:
                timestamp = msg_ts_match.group(1)
            else:
                timestamp = group_timestamp

            # Check if pinned
            pinned = "chatlog__message-container--pinned" in container_html

            # Extract reply context
            reply_author = ""
            reply_content = ""
            reply_match = re.search(
                r'class=chatlog__reply-author[^>]*title=(\S+)[^>]*>([^<]*)</div>'
                r'.*?class=chatlog__reply-content>(.*?)</div>',
                container_html,
                re.DOTALL,
            )
            if reply_match:
                reply_author = reply_match.group(1)
                reply_content = strip_html(reply_match.group(3))

            # Extract message content
            content = ""
            content_match = re.search(
                r'class="chatlog__content chatlog__markdown">(.*?)</div>',
                container_html,
                re.DOTALL,
            )
            if content_match:
                raw = content_match.group(1)
                # Remove edited timestamp
                raw = re.sub(r'<span class=chatlog__edited-timestamp[^>]*>[^<]*</span>', '', raw)
                content = strip_html(raw)

            # Extract embeds (simplified - just grab text content)
            embeds = []
            for embed_match in re.finditer(
                r'class="chatlog__embed-description[^"]*">(.*?)</div>',
                container_html,
                re.DOTALL,
            ):
                embeds.append(strip_html(embed_match.group(1)))

            # Extract image attachments
            attachments = []
            for img_match in re.finditer(
                r'class="chatlog__attachment[^"]*"[^>]*>.*?<img[^>]*src="([^"]*)"',
                container_html,
                re.DOTALL,
            ):
                attachments.append(img_match.group(1))

            if content or embeds or attachments:
                messages.append({
                    "id": msg_id,
                    "author": author,
                    "timestamp": timestamp,
                    "content": content,
                    "reply_author": reply_author,
                    "reply_content": reply_content,
                    "embeds": embeds,
                    "attachments": attachments,
                    "pinned": pinned,
                })

    return messages


def format_message(msg):
    """Format a single message as markdown."""
    lines = []

    pinned = " [PINNED]" if msg["pinned"] else ""
    lines.append(f"### {msg['author']} — {msg['timestamp']}{pinned}")
    lines.append("")

    if msg["reply_author"]:
        reply_preview = msg["reply_content"][:200] if msg["reply_content"] else "(attachment/embed)"
        lines.append(f"> **{msg['reply_author']}**: {reply_preview}")
        lines.append("")

    if msg["content"]:
        lines.append(msg["content"])
        lines.append("")

    for embed in msg["embeds"]:
        lines.append(f"> {embed}")
        lines.append("")

    for att in msg["attachments"]:
        lines.append(f"[attachment]({att})")
        lines.append("")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 3:
        print(f"Usage: python {sys.argv[0]} <input.html> <output.md>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(input_path, "r", encoding="utf-8") as f:
        html = f.read()

    messages = parse_discord_html(html)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# Discord Export: rules-questions\n\n")
        f.write(f"Parsed {len(messages)} messages.\n\n---\n\n")
        for msg in messages:
            f.write(format_message(msg))
            f.write("---\n\n")

    print(f"Parsed {len(messages)} messages -> {output_path}")


if __name__ == "__main__":
    main()

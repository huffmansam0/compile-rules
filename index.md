---
title: COMPILE Supplemental Clarifications
---
# COMPILE: Supplemental Clarifications

## Contents

- [General Rules Clarifications](#general-rules-clarifications)
- [Targeting and Selection](#targeting-and-selection)
- [Timing and Resolution](#timing-and-resolution)
- [Card Clarifications and Rulings](#card-clarifications-and-rulings)

| | | | |
|:--|:--|:--|:--|
| [Apathy 2](#apathy-2) | [Clarity 1](#clarity-1) | [Darkness 2](#darkness-2) | [Death 2](#death-2) |
| [Death 3](#death-3) | [Diversity 0](#diversity-0) | [Fire 4](#fire-4) | [Gravity 0](#gravity-0) |
| [Gravity 2](#gravity-2) | [Ice 3](#ice-3) | [Life 0](#life-0) | [Life 1](#life-1) |
| [Light 0](#light-0) | [Luck 2](#luck-2) | [Luck 3](#luck-3) | [Metal 3](#metal-3) |
| [Metal 6](#metal-6) | [Mirror 2](#mirror-2) | [Mirror 4](#mirror-4) | [Plague 0](#plague-0) |
| [Plague 1](#plague-1) | [Plague 2](#plague-2) | [Plague 3](#plague-3) | [Plague 4](#plague-4) |
| [Speed 1](#speed-1) | [Speed 3](#speed-3) | [Spirit 0](#spirit-0) | [Time 0](#time-0) |
| [Time 2](#time-2) | [Unity 1](#unity-1) | [War 2](#war-2) | [Water 4](#water-4) |

---

## General Rules Clarifications

### Game State Must Change for Effects to Resolve

If an effect cannot change the game state, it does not happen and no "After" windows are reached. Specific implications:

- If the only valid target for a flip is a card that **cannot** be flipped (e.g., Ice 4's prevention), the flip doesn't happen and "After you flip a card" windows are never reached.
- Shuffling a deck of 0 or 1 cards does **not** change the game state, so it effectively doesn't happen. Time 2's "After you shuffle" would not trigger in this case.
- Shuffling a deck of 2+ cards **is** considered a game-state change, even though there's a chance the order didn't actually change.

### Mandatory Choices Must Have Effect

When a mandatory effect requires you to make a choice (e.g., choosing a line or target), you **must** choose an option that changes the game state, if one exists. You cannot intentionally choose a "no-effect" option when an effective one is available.

**Example:** If Water 3 would return value-2 cards and one line has value-2 cards but another does not, you cannot choose the empty/ineligible line.

### "May" Is Optional; Everything Else Is Mandatory

Only the word "may" makes something optional. All other card text must be resolved as fully as possible. If you cannot fully resolve an effect, resolve as much as you can.

### The Compiling Player Deletes All Cards

The compiling player deletes **all** cards from the line — both their own stack and their opponent's stack — simultaneously. No middle commands trigger from being uncovered during this step.

### Control Rearrangement Happens Before the Action

When you have the control component and compile or refresh, you return control to neutral and rearrange protocols **before** executing the compile or refresh. This means you can choose which protocol you compile after seeing the board state. When refreshing with control, you rearrange before drawing — you do not see your new hand first.

### Protocol Order Is Fixed After Draft

Protocols are placed left-to-right in the order they were drafted and **cannot be rearranged** before the game starts. Only in-game effects (e.g., Water 2, Spirit 4, control rearrangement) can change protocol order.

### Refresh Limitation

You cannot refresh if you would draw no cards. This covers both having 5 or more cards in hand and having an empty deck and trash. You cannot refresh solely to spend the control component if you would draw no cards.

### Recompiling Is a Draw

Recompiling (compiling a line whose protocol is already on its "Compiled" side) results in drawing the top card of the opponent's deck. This is treated as a **draw action**, which means it can trigger a deck reshuffle if the opponent's deck is empty (shuffle their trash into a new deck, then draw). Effects that "play the top card of your deck" will **fizzle** (do nothing) if the deck is empty — only drawing triggers reshuffles.

### Playing a Card That Returns Itself Is Legal

Even if a card's effect returns itself to the owner's hand (e.g., Water 4), this is a legal play. The game state changed during resolution — the card left the hand and entered the field before being returned.

### Negative Line Values Are Possible

Line values have no floor. Metal 0's top command ("Your opponent's total value in this line is reduced by 2") can push their value below 0. An empty stack across from Metal 0 has a total value of **−2** for that player.

### Active Text Interruption

**"Text that is active and is covered, flipped face-down, or deleted while resolving is cancelled — any remaining text does not happen."**

If a card is covered, flipped face-down, or deleted while its text is resolving, all remaining text on that effect stops immediately.

- **Exception:** Shifting a card does **not** cancel its active text. The card continues resolving after the shift.
- **Exception:** Top commands remain active when covered (they are never obscured), but are interrupted if the card is flipped face-down or deleted.

**Examples:** If Life 0 gets covered mid-resolution, the remaining line plays stop. If Hate 2 deletes itself as the highest-value card, its second delete clause no longer exists. If a card flips itself face-down, any text after the flip is cancelled.

### "Each" Processes One at a Time; "All" Is Simultaneous

- **"Each"** (e.g., Death 0: "Delete 1 card from each other line"): Targets are noted, then processed one line at a time. Each individual deletion fully resolves — including consequences like "After" triggers — before the next line is processed. The card's owner chooses the order.
- **"All"** (e.g., compile deletion, Death 2): All matching cards are affected simultaneously. No intermediate triggers fire between individual cards.

**Example:** If Hate 3 is active and Death 0 deletes cards from 2 separate lines, Hate 3 draws **2 cards** (one for each separate delete event).

### Reveal Is Temporary

Revealing a card shows both players the information, then returns the card to its previous state. Hand reveals are not persistent — cards do not remain visible. Revealing a face-down card on the field shows it, then returns it to face-down.

---

## Targeting and Selection

### Default Targeting: Both Players' Cards

Unless a card specifies otherwise, field effects (flip, delete, shift, return) can target **either player's** uncovered cards. Only uncovered cards are valid targets unless the card uses "covered," "all," "this," or "that."

- **Discard** is always from your own hand, never your opponent's — unless a card explicitly says "your opponent discards."
- **Play** is always to your side of the field — you cannot play cards onto your opponent's side unless a card explicitly permits it.

### Self-Targeting Is Allowed

A middle command can target the card that generated it, unless the text says "other." "Flip 1 card" can target itself; "Flip 1 **other** card" cannot. The same applies to delete, shift, and return.

### "Highest"/"Lowest" Do Not Inherently Target Covered Cards

Effects that reference "highest value" or "lowest value" cards follow the standard selection rules and can only target uncovered cards, unless the card explicitly says "covered" or "all."

---

## Timing and Resolution

### "After" Triggers Check Status at the End, Not the Beginning

An "After" trigger checks whether the card is face-up **when the "After" window is reached** (at the conclusion of the triggering event), not when the event started. A card that becomes face-up partway through a sequence will trigger. Conversely, a card that was face-up at the start but gets flipped face-down before the "After" window is reached will **not** trigger.

**Example:** Hate 3's top command reads "After you delete a card: draw 1 card." Suppose Hate 1 deletes a card that causes Water 0 to be revealed. Water 0 flips Hate 3 face-up, making Hate 3's top command active. Water 0 flips itself. Hate 1's delete is now finished, and we reach the "After you delete a card" window — Hate 3 activates and you draw a card. Then Hate 1 does its second delete, and you draw a second card. The result is 2 draws, even though Hate 3 was not face-up when Hate 1's first delete began.

### End/Start Triggers Are Chosen One at a Time

When you enter the Start or End phase and collect your triggers, you choose **one** trigger from the collection to resolve, fully resolve it, then choose the next. You do not have to commit to an ordering for all of them upfront. This is a runtime decision.

### Triggers Revealed During Start/End Do Not Fire

Cards revealed or played **during** the Start or End phase do not add new triggers for that phase. Only triggers visible at the very beginning of the phase are collected.

### Middle Commands Only Trigger on Reveal

Middle commands trigger when a card is:
1. Played face-up
2. Flipped face-up **while uncovered**
3. Uncovered (by removal of the card above it)

A **covered** card that is flipped face-up does **not** trigger its middle command — it remains covered. A card shifted from a covered position to become the top of another stack **does** trigger its middle command (it was previously hidden and is now revealed). An already-uncovered card that shifts does **not** re-trigger.

### Committed Cards Are Not on the Field

A card entering a "committed" state (during playing, shifting, deleting, or returning) is **not on the field** during transit. Implications:

- Committed cards **cannot be targeted**, selected, or manipulated by any effect.
- They do **not count toward line values**.
- Their landing at the destination is **guaranteed** — nothing can prevent it.
- This applies to cards played from hand as well — a played card is committed before it lands.

### Each Zone Has Its Own Commit Queue

Each stack, the hand, the trash, and the deck each have their own commit queue. Cards commit to their destination's queue and land in FIFO order within that queue. Multiple cards going to the same destination enter in the order they were committed.

### Commit Queue Is FIFO; Everything Else Is LIFO

When multiple cards are committed (waiting to enter the field), the commit queue processes in **FIFO** (first in, first out) order — the card that was committed first lands first. All other game resolution is **LIFO** (last in, first out) — newly triggered effects interrupt and resolve before returning to the prior effect.

### The Covering Card Cannot Be Targeted During OnCover Resolution

When an OnCover effect ("When this card would be covered") triggers, the covering card is still in the committed state and **cannot be targeted** by any effect during this resolution.

### The Play Action Has Distinct Steps

Playing a card consists of these ordered steps:

1. **Decision** — Choose the card, its orientation (face-up/face-down), and its destination line.
2. **Commit** — The card leaves the hand and enters the commit queue for its destination.
3. **Land** — The card enters the stack. If this would cover another card, OnCover effects ("When this card would be covered") can interrupt the Land step and must be completely resolved before proceeding.
4. **Middle command activation** — The card's middle text resolves.

The "After a card is played" window only opens after **all four steps** are complete. A card's middle text activating is considered part of the play action, not separate from it.

### Rearranging Is Instantaneous

Rearranging protocols is a single decision — there is no intermediate state where multiple cards are simultaneously uncovered. At most one card becomes newly uncovered as a result of a rearrange.

### Current Player Decides Resolution Order, Card Owner Decides Targets

When multiple cards trigger simultaneously, the current player decides the order of resolution, regardless of who owns or triggered the cards. The **owner of each card** decides how that card's individual effect resolves (e.g., choosing targets).

For example: If it's your turn and you flip your opponent's Death 2, your opponent decides which lines to delete cards in (their card, their targeting decisions), but you decide which of the simultaneously uncovered middle commands resolves first.

---

## Card Clarifications and Rulings

### Apathy 2

- Top command applies to **both players'** cards in the line, not just the owner's side.

### Clarity 1

- Discarding from the deck still counts as a **discard action** and will trigger effects that respond to discarding (e.g., Corruption 2's "After your opponent discards").

### Darkness 2

- Top command ("All face-down cards in this stack have a value of 4") affects how those cards are treated by **all** value-checking effects, including Death 2, Water 3, and any other effect that checks a card's value.

### Death 2

- You must choose a line where at least one card matches the value criteria. You cannot choose a line where nothing would be deleted.

### Death 3

- Can target **either player's** face-down card, not just your own.

### Diversity 0

- Not a compile action. War 2's "After your opponent compiles" and Speed 2's compile-deletion replacement do not apply. The player who activates Diversity 0 still takes their normal action that turn.
- Checks **all** face-up cards on the field, both covered and uncovered. It is not a persistent effect — it only checks at the moment the middle command triggers. Face-down cards count as non-Diversity (they have no protocol).

### Fire 4

- If Fire 4 was your last card in hand, you discarded 0 cards. Each sentence is treated separately, so you still draw 0 + 1 = **1 card**.

### Gravity 0

- Cards played by Gravity 0's middle command enter the committed queue like any other played card, but land **directly under Gravity 0** in the stack instead of on top.

### Gravity 2

- "That card" bypasses normal selection restrictions. Even if the flipped card becomes covered during resolution, the subsequent shift of "that card" still goes through.

### Ice 3

- The "if this card is covered" condition is checked **when you choose to resolve** Ice 3's End trigger, not when triggers are collected. If another End trigger (e.g., Courage 3's shift) covers Ice 3 first, the condition will be satisfied.

### Life 0

- Lines are noted at activation. Lines that gain a card during resolution do not retroactively qualify. Each valid line is processed one at a time — play the top card of your deck face-down and fully resolve any consequences before moving to the next. If Life 0 gets covered during processing, the remaining lines are skipped.

### Life 1

- The two "Flip 1 card" commands are separate sentences. If the first flip causes Life 1 to be flipped face-down, the second flip is cancelled.

### Light 0

- The value for the draw is checked **when the draw resolves**, not when the flip happens. If the card was flipped face-down, its value is 2. If the card was deleted to the trash, it is face-up in the trash and uses its printed value.
- **Example:** Light 0 targets Metal 6. Metal 6 deletes itself (per its top command). Metal 6 is now face-up in the trash with a value of 6 — you draw 6 cards.

### Luck 2

- Empty deck draws nothing. Luck 2's effect is not a standard draw action and does **not** trigger a reshuffle.

### Luck 3

- You can name **any protocol that exists in the game**, including ones not in the current match. This allows you to intentionally miss.
- When Luck 3's effect discards a card from the top of your opponent's deck, that card goes to the **opponent's trash**, not yours.

### Metal 3

- The deletion is **mandatory**. If a line has 8 or more cards, you must choose it.

### Metal 6

- If Metal 6 is face-down and covered, then flipped face-up (e.g., by Chaos 0), Metal 6 does **not** delete itself. The "when this card would be covered" window has already passed, and Metal 6's text was not active when it was covered (it was face-down).

### Mirror 2

- Cannot swap with an empty line. Stacks only exist when they have cards in them.
- Committed cards stay committed to their **original destination** during a swap. Mirror 2 swaps the cards in the stacks, not the stacks themselves.

### Mirror 4

- Refreshing counts as drawing and will trigger Mirror 4.

### Plague 0

- Bottom text prevents the opponent from **playing** cards into the line. It does **not** prevent cards from being shifted into the line.

### Plague 1

- Triggers on **any** discard action: clearing cache, discarding from deck (Clarity 1, Luck 2, Luck 3, Luck 4), etc.

### Plague 2

- Opponent discards regardless of whether you had cards to discard. If you discarded 0 (empty hand), your opponent discards 0 + 1 = 1.

### Plague 3

- Notes all uncovered face-up cards (both sides, not Plague 3 itself) at activation, then flips them one at a time. Consequences (including middle commands from newly revealed cards) fully resolve between flips. A card newly uncovered by a self-delete during processing gets its middle command resolved but is **not** flipped by Plague 3.

### Plague 4

- End command only targets **uncovered** face-down cards. Covered face-down cards are not valid targets.

### Speed 1

- **Check Cache** is the phase name. **Clear Cache** is the action of discarding down to 5 within that phase. Speed 1 triggers only when you actually discard — not simply for entering the phase with 5 or fewer cards.

### Speed 3

- If Speed 3's End shift moves a card to Speed 3's line, the incoming card covers Speed 3. Speed 3's text is interrupted by being covered, and the flip does **not** happen.

### Spirit 0

- If you have 5 or more cards in hand, the refresh fizzles. The "Draw 1 card" is a separate sentence and **still resolves** regardless.
- The refresh and "Draw 1 card" are two separate draw actions. Spirit 3 triggers **separately** for each.

### Time 0

- Shuffling happens **even if your trash is empty** — the deck still gets randomized. If both deck and trash are empty, nothing happens (game state can't change).

### Time 2

- Shuffling a deck of 0 or 1 cards does **not** change the game state, so Time 2 does not trigger. Shuffling 2+ cards **does** trigger Time 2, even though the order might not have changed.
- Time 2 does **not** interrupt a draw that caused the shuffle. The full draw resolves first, then Time 2's trigger activates. "After you draw cards" and "After you shuffle" triggers happen at the same time after the draw completes.

### Unity 1

- Unity 1's effect is **not a compile action**. It does not trigger control component actions (no rearrangement, no returning control to neutral).
- Unity 1 **cannot recompile** — if the protocol is already compiled, the deletion still happens but no additional benefit occurs.

### War 2

- War 2's "After your opponent compiles" does **not** trigger if War 2 is in the compiled line. War 2 is deleted as part of the compile and is in the trash before the "After compile" window opens.

### Water 4

- Returning itself is a legal play.

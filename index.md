# Compile Codex: Supplemental Clarifications

---

## General Rules Clarifications

### Game State Must Change for Effects to Resolve

If an effect cannot change the game state, it does not happen and no "After" windows are reached. Specific implications:

- If the only valid target for a flip is a card that **cannot** be flipped (e.g., Ice 4's prevention), the flip doesn't happen and "After you flip a card" windows are never reached.
- Shuffling a deck of 0 or 1 cards does **not** change the game state, so it effectively doesn't happen. Time 2's "After you shuffle" would not trigger in this case.
- Shuffling a deck of 2+ cards **is** considered a game-state change, even though there's a chance the order didn't actually change.

### Refresh Limitation

You cannot refresh if you would draw no cards. This covers both having 5 or more cards in hand and having an empty deck and trash. You cannot refresh solely to spend the control component if you would draw no cards.

### Recompiling Is a Draw

Recompiling (compiling a line whose protocol is already on its "Compiled" side) results in drawing the top card of the opponent's deck. This is treated as a **draw action**, which means it can trigger a deck reshuffle if the opponent's deck is empty (shuffle their trash into a new deck, then draw). Effects that "play the top card of your deck" will **fizzle** (do nothing) if the deck is empty — only drawing triggers reshuffles.

### Playing a Card That Returns Itself Is Legal

Even if a card's effect returns itself to the owner's hand (e.g., Water 4), this is a legal play. The game state changed during resolution — the card left the hand and entered the field before being returned.

### "Highest"/"Lowest" Do Not Inherently Target Covered Cards

Effects that reference "highest value" or "lowest value" cards follow the standard selection rules and can only target uncovered cards, unless the card explicitly says "covered" or "all."

---

## Timing and Resolution

### "After" Triggers Check Status at the End, Not the Beginning

An "After" trigger checks whether the card is face-up **when the "After" window is reached** (at the conclusion of the triggering event), not when the event started. A card that becomes face-up partway through a sequence will trigger. Conversely, a card that was face-up at the start but gets flipped face-down before the "After" window is reached will **not** trigger.

**Example:** Hate 3's top command reads "After you delete a card: draw 1 card." Suppose Hate 1 deletes a card that causes Water 0 to be revealed. Water 0 flips Hate 3 face-up, making Hate 3's top command active. Water 0 flips itself. Hate 1's delete is now finished, and we reach the "After you delete a card" window — Hate 3 activates and you draw a card. Then Hate 1 does its second delete, and you draw a second card. The result is 2 draws, even though Hate 3 was not face-up when Hate 1's first delete began.

### End/Start Triggers Are Chosen One at a Time

When you enter the Start or End phase and collect your triggers, you choose **one** trigger from the collection to resolve, fully resolve it, then choose the next. You do not have to commit to an ordering for all of them upfront. This is a runtime decision.

### Commit Queue Is FIFO; Everything Else Is LIFO

When multiple cards are committed (waiting to enter the field), the commit queue processes in **FIFO** (first in, first out) order — the card that was committed first lands first. All other game resolution is **LIFO** (last in, first out) — newly triggered effects interrupt and resolve before returning to the prior effect.

### The Play Action Has Distinct Steps

Playing a card consists of these ordered steps:

1. **Decision** — Choose the card, its orientation (face-up/face-down), and its destination line.
2. **Commit** — The card leaves the hand and enters the commit queue for its destination.
3. **Land** — The card enters the stack (potentially covering another card and triggering "When this card would be covered" effects).
4. **Middle command activation** — The card's middle text resolves.

The "After a card is played" window only opens after **all four steps** are complete. A card's middle text activating is considered part of the play action, not separate from it.

### Current Player Decides Resolution Order, Card Owner Decides Targets

When multiple cards trigger simultaneously, the current player decides the order of resolution, regardless of who owns or triggered the cards. The **owner of each card** decides how that card's individual effect resolves (e.g., choosing targets).

For example: If it's your turn and you flip your opponent's Death 2, your opponent decides which lines to delete cards in (their card, their targeting decisions), but you decide which of the simultaneously uncovered middle commands resolves first.

---

## Committed Cards

### Gravity 0's Played Cards Land Under Gravity 0

When Gravity 0's middle command plays cards from the top of the deck, those played cards enter the committed queue like any other played card. The special rule is that instead of landing on top of the stack, they get placed **directly under Gravity 0** in the stack.

---

## Card Clarifications and Rulings

### Unity 1

Unity 1's middle command can delete all cards in a line and flip a protocol, mimicking a compile. However:

- Unity 1 **cannot recompile** — if the protocol is already compiled, the deletion still happens but no additional benefit (like drawing from opponent's deck) occurs.
- Unity 1's effect **does not trigger control component actions** (no optional protocol rearrangement, no returning control to neutral). It is a card effect, not a compile action.

### Luck 3 — "State a Protocol"

When Luck 3 says "State a protocol," you can name **any protocol that exists in the game**, including ones not present in the current match. This effectively allows you to intentionally miss.

### Time 0 — Shuffle with Empty Trash

Time 0's text instructs you to shuffle your trash into your deck. This shuffle happens **even if your trash is empty** — the deck still gets shuffled (randomized). However, if both your deck and trash are empty, the game state can't change, so nothing happens and Time 2's "After you shuffle" would not trigger.

### Time 2 — Shuffle Doesn't Interrupt Drawing

Time 2's "After you shuffle your deck" trigger does **not** interrupt a draw that caused the shuffle. The full sequence is:

- If a draw begins and the deck is empty: shuffle the deck, draw the cards, **then** Time 2's trigger activates.
- If there are some cards but not enough to complete the draw: draw what you can, shuffle the deck, complete the draw, **then** Time 2's trigger activates.
- In both cases, "After you draw cards" and "After you shuffle" triggers happen at the same time after the draw fully resolves.

### War 2 — Bottom Effect and Compiling

War 2's bottom text ("After your opponent compiles:") does **not** trigger if War 2 is in the compiled line. The "After compile" window occurs only after: the control component is used, all deletions finish, and the protocol is flipped. Since War 2 would be deleted as part of the compile, it is in the trash by the time this window opens.

### Mirror 2 — Swapping with Committed Cards

When Mirror 2's effect is triggered during a shift (e.g., the shift uncovered Mirror 2), any cards that are currently committed to a stack stay committed to their **original destination**. Mirror 2 swaps the cards that are in the stacks, not the stacks themselves. A committed card's destination doesn't change because of a swap.

### Mirror 2 — Cannot Swap with Empty Lines

Stacks only exist when they have cards in them. You **cannot** use Mirror 2 to swap with an empty line.

### Ice 3 — End Trigger and Covering Condition

Ice 3's End trigger ("End: If this card is covered...") activates during the End phase like all End triggers. The **condition** (being covered) is only checked when you choose to resolve Ice 3's trigger, **not** when triggers are collected. This means if another End trigger (e.g., Courage 3's shift) covers Ice 3 before you process Ice 3's End trigger, the condition will be satisfied.

### Courage 3 — Draw Before Shift

Courage 3's "Draw 1 card and you may shift this card" processes the draw **before** the shift.

---

## Miscellaneous

### Clearing Cache Counts as Discarding

Discarding cards during the Check Cache phase (clearing cache) counts as a discard action and will trigger relevant effects (e.g., Plague 1's top command: "After your opponent discards cards: draw 1 card").

### Refreshing Is Drawing (for Trigger Purposes)

Refreshing draws cards from the top of the deck, and this counts as drawing for the purposes of triggers (e.g., Mirror 4).

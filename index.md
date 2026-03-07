---
title: COMPILE Supplemental Clarifications
---
# COMPILE: Supplemental Clarifications

## Contents

- [General Rules Clarifications](#general-rules-clarifications)
- [Timing and Resolution](#timing-and-resolution)
- [Card Clarifications and Rulings](#card-clarifications-and-rulings): [Gravity 0](#gravity-0) · [Ice 3](#ice-3) · [Luck 2](#luck-2) · [Luck 3](#luck-3) · [Mirror 2](#mirror-2) · [Mirror 4](#mirror-4) · [Plague 1](#plague-1) · [Time 0](#time-0) · [Time 2](#time-2) · [Unity 1](#unity-1) · [War 2](#war-2) · [Water 4](#water-4)

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
3. **Land** — The card enters the stack. If this would cover another card, OnCover effects ("When this card would be covered") can interrupt the Land step and must be completely resolved before proceeding.
4. **Middle command activation** — The card's middle text resolves.

The "After a card is played" window only opens after **all four steps** are complete. A card's middle text activating is considered part of the play action, not separate from it.

### Current Player Decides Resolution Order, Card Owner Decides Targets

When multiple cards trigger simultaneously, the current player decides the order of resolution, regardless of who owns or triggered the cards. The **owner of each card** decides how that card's individual effect resolves (e.g., choosing targets).

For example: If it's your turn and you flip your opponent's Death 2, your opponent decides which lines to delete cards in (their card, their targeting decisions), but you decide which of the simultaneously uncovered middle commands resolves first.

---

## Card Clarifications and Rulings

### Gravity 0

- Cards played by Gravity 0's middle command enter the committed queue like any other played card, but land **directly under Gravity 0** in the stack instead of on top.

### Ice 3

- The "if this card is covered" condition is checked **when you choose to resolve** Ice 3's End trigger, not when triggers are collected. If another End trigger (e.g., Courage 3's shift) covers Ice 3 first, the condition will be satisfied.

### Luck 2

- Empty deck draws nothing. Luck 2's effect is not a standard draw action and does **not** trigger a reshuffle.

### Luck 3

- You can name **any protocol that exists in the game**, including ones not in the current match. This allows you to intentionally miss.

### Mirror 2

- Cannot swap with an empty line. Stacks only exist when they have cards in them.
- Committed cards stay committed to their **original destination** during a swap. Mirror 2 swaps the cards in the stacks, not the stacks themselves.

### Mirror 4

- Refreshing counts as drawing and will trigger Mirror 4.

### Plague 1

- Triggers on **any** discard action: clearing cache, discarding from deck (Clarity 1, Luck 2, Luck 3, Luck 4), etc.

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

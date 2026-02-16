# Puzzle Laboratory - Iterative Riddle Development

## Design Principles Learned from TED-Ed Analysis
1. **Counterintuitive solutions** - The answer should defy initial intuition
2. **Narrative framing** - Abstract logic wrapped in compelling stories
3. **Information asymmetry** - What you know vs. what others know drives the puzzle
4. **Emergent elegance** - Simple rules create surprising complexity
5. **The "aha" moment** - Solution should feel inevitable in hindsight

---

## Attempt #1: The Quantum Courier

### The Setup

You are a courier in a dystopian city where the authoritarian government monitors all communication. You must deliver a secret message to one of three rebel contacts: Ada, Bex, or Cole.

Here's the problem:
- **Exactly one** of them is a government spy (you don't know which)
- **Exactly one** of them is your true contact (you don't know which)
- **Exactly one** is a neutral civilian who will simply ignore you
- You may ask **one yes/no question** to **one person**
- The spy always lies, the contact always tells truth, the civilian answers randomly
- If you give the message to the spy, you're captured. If you give it to the civilian, the message is lost. You must deliver to the contact.

After asking your question, you must either:
- Deliver the message to someone, OR
- Walk away (mission failed, but you survive)

### The Question
**What single yes/no question can you ask to ONE person that allows you to identify your contact with certainty, or at minimum, guarantees you won't give the message to the spy?**

---

### Analysis of Why This Might Fail

**Potential issues:**
- Too similar to Three Gods Riddle (the spy/truth-teller/random structure)
- May not have a clean solution
- The "walk away" option might be a cop-out

**What would make it better:**
- Need a novel twist that isn't just "variant of knights/knaves/random"
- The solution should use a mechanism not seen in existing puzzles

---

## Attempt #2: The Inheritance Paradox

### The Setup

Your eccentric billionaire uncle has died and left his fortune to be divided among you and your four cousins. But there's a catch in the will:

The fortune is in a vault with 5 doors. Behind each door is a different amount:
- $1 million, $2 million, $3 million, $4 million, $5 million

The will states:
1. Each heir picks a door simultaneously (no communication)
2. If multiple heirs pick the same door, **that door becomes worthless** (the money is donated to charity)
3. You each receive whatever is behind your uniquely-chosen door (or nothing if someone matched you)

You are the last to learn of this arrangement. Your four cousins have already **secretly decided** their choices and cannot change them. You know they are all **perfectly rational** and were told the rules at the same time.

**Question: Which door should you choose, and how much money will you receive?**

---

### Why This Might Be Better

- Game theory mixed with common knowledge
- The "already decided" twist creates asymmetry
- Requires reasoning about what rational actors would do
- Has echoes of the pirate problem but different mechanism

### Potential Solution Path

If all cousins are rational and chose simultaneously:
- They know collisions = $0
- Nash equilibrium analysis suggests they'd try to avoid each other
- But without communication, they face coordination problem
- Mixed strategy equilibrium? Or is there a pure strategy focal point?

**The twist:** You choosing AFTER they've locked in means you have information they didn't have - the knowledge of what rational actors would converge on.

---

## Attempt #3: The Lighthouse Keeper's Dilemma

### The Setup

You are a lighthouse keeper on a remote island. Three ships are approaching in dense fog - one carries refugees, one carries pirates, and one is the coast guard.

Your lighthouse can signal in three ways:
- **Green light**: "Safe to approach"
- **Red light**: "Danger, stay away"
- **No light**: Ambiguous

The ships react as follows:
- **Refugees**: Approach on green, retreat on red, approach on no light (desperate)
- **Pirates**: Approach on green, approach on red (they don't fear danger), retreat on no light (suspicious of traps)
- **Coast Guard**: Approach on green, approach on red (to investigate danger), stay put on no light (waiting for protocol)

You can change the light **once per hour**. The ships take **2 hours** to reach you or retreat beyond range. You must:
- Allow the refugees to land
- Prevent the pirates from landing
- It doesn't matter what happens to the coast guard

**Starting state**: The light is currently OFF (no light).
**You have exactly 3 hours before the refugee ship runs out of fuel and sinks.**

### The Question
**What sequence of light signals allows the refugees to land while keeping the pirates away?**

---

### Analysis

**Hour 0 (No light currently):**
- Refugees: Approaching
- Pirates: Retreating
- Coast Guard: Staying put

**Hmm, this might be too easy** - if no light already makes pirates retreat and refugees approach, just leave it off?

Let me reconsider the constraints...

---

## Feedback Loop

**After each attempt, document:**
1. What worked / what felt clever
2. What felt derivative or obvious
3. What mechanism hasn't been exploited
4. User feedback (to be added)

---

## User Feedback Section

*[Space for user to add what they liked/disliked about each attempt]*

### Attempt #1 Feedback:
>

### Attempt #2 Feedback:
>

### Attempt #3 Feedback:
>

---

## Unexplored Mechanisms to Try

Based on the TED-Ed analysis, these information theory archetypes are underexplored:

1. **Temporal paradoxes** - Information about the future affecting present decisions
2. **Quantum-style superposition** - States that collapse upon observation
3. **Network effects** - Where the puzzle changes based on how many people are solving it simultaneously
4. **Asymmetric partial information** - Different solvers have different pieces
5. **Self-modifying rules** - The puzzle rules change based on your actions
6. **Irreversibility constraints** - Actions that can't be undone create path dependency

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1 | 2026-02-16 | Initial three attempts |

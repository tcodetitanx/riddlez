# Riddle Evolution Framework

## Goal
Evolve a prompt that produces 10/10 puzzles across all metrics:
- Originality (1-10)
- Cleverness of Solution (1-10)
- Simplicity of Setup (1-10)
- Solution Success (1-10)

## Process
1. **Generation N**: Take best prompt from Gen N-1
2. **Mutate**: Create 5 variations of the prompt
3. **Generate**: Each variation produces 3 riddles (15 total)
4. **Evaluate**: Score all riddles
5. **Select**: Keep prompt that produced highest-scoring riddle
6. **Repeat**: Until 10/10 achieved

## Anti-Overfitting Parameters
To prevent degenerate solutions like "What is 1+1?":

### Minimum Complexity Floor
- Riddle must require at least 3 logical steps to solve
- Solution cannot be immediately obvious from setup
- Must involve at least one non-trivial inference

### Originality Guard
- Cannot be a direct reskin of: Monty Hall, Knights/Knaves, River Crossing, Hat Problems
- Must have at least one novel mechanic or constraint
- If mechanism is recognizable, framing must fundamentally change the problem

### Solution Integrity
- Solution must be verifiable step-by-step
- No hand-waving ("through careful analysis...")
- No admitted incompleteness
- Must have UNIQUE solution (prove alternatives fail)

### Accessibility Ceiling
- Setup must be explainable in under 150 words
- No specialized knowledge required (no physics, advanced math)
- A motivated high schooler should understand the setup

## Evaluation Rubric

### Originality (1-10)
- 1-3: Direct copy or obvious reskin of classic
- 4-5: Familiar mechanism with different context
- 6-7: Novel combination of known archetypes
- 8-9: New mechanism or constraint type
- 10: Genuinely unprecedented puzzle structure

### Cleverness (1-10)
- 1-3: No insight required; brute force works
- 4-5: Single obvious insight
- 6-7: Non-obvious insight that feels inevitable in retrospect
- 8-9: Multiple interlocking insights
- 10: Mind-bending insight that changes how you think

### Simplicity (1-10)
- 1-3: Requires multiple re-reads to understand setup
- 4-5: Complex but followable with effort
- 6-7: Clear after one careful read
- 8-9: Immediately graspable
- 10: Could explain to a child; crystal clear

### Solution Success (1-10)
- 1-3: Solution doesn't work or is incomplete
- 4-5: Works but with edge cases or ambiguity
- 6-7: Solid solution with clear steps
- 8-9: Elegant, complete, verifiable
- 10: Perfect - unique, proven, satisfying

## Generation Log

### Generation 0.1 (Baseline)
- Source: TWENTY_ORIGINAL_PUZZLES.pdf
- Best puzzle: Clone Dilemma (35/40)
- Average: 25.3/40
- Broken puzzles: 4/15

### Generation 1.0
[To be filled after running]

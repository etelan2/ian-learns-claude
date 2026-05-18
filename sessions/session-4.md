# Session 4 — When Claude Gets It Wrong

**Duration**: 90 minutes
**Deliverable**: 3 real bugs fixed in your project
**Meta-lesson**: AI hallucinates. AI lies with confidence. You verify.

---

## Before you start

- [ ] Project defined in session 3
- [ ] Scaffold created and pushed to GitHub

---

## The reality of programming with AI

Claude is brilliant. But also:
- Sometimes invents functions that don't exist
- Sometimes gives you code that looks right but doesn't compile
- Sometimes tells you something with confidence that's false
- Sometimes repeats the same mistake after you told it it's wrong

This is NOT because it's bad. It's the nature of the model. The key skill in 2026 is:

> **Verifying what the AI tells you before trusting it.**

This session you'll practice that.

---

## Part 1 (40 min) — Build with intentional bugs

You're going to build your first 1-2 features of your project.

Ask Claude:

```
I want to start building [FEATURE 1 from my scope]. Build it with me step by step. Explain each decision.
```

**As you build, you'll find bugs.** Guaranteed. When one appears:

### The "it's not working" pattern

❌ **What NOT to say**:
> "It's not working"
> "It's broken"
> "Help"

✅ **What TO say**:
> "I ran command X. I got this exact error: [paste error fully]"
> "I expected A to happen, but B happened instead"

**Difference**: in the second case, Claude has real info to diagnose. In the first, Claude has to guess.

---

## Part 2 (15 min) — Your "read the errors" session

When the first real error appears:

1. **Don't say anything to Claude yet.** Read it.
2. Identify:
   - What line?
   - What file?
   - What does it say exactly?
3. Translate it to plain English mentally.
4. Hypothesis: what do you think is happening?
5. **Now** talk to Claude:

```
I got this error: [paste fully]
I was running: [command]
My hypothesis is that [what you think].
Do you agree? What do we need to verify before changing anything?
```

That way of asking = senior level. You learn it today.

---

## Part 3 (15 min) — When Claude is wrong

In this session it's going to happen at least once that Claude tells you something that DOESN'T work.

When it happens, DON'T get angry. Your job:

```
You said X. I tried it. It didn't work. I got this: [error]

What happened? Why didn't your suggestion work? What information were you missing to give me the right solution?
```

**That last question is gold.** Claude will tell you what info it needed. Next time, you give it that info upfront.

That's **prompt engineering in real life**. It's not an abstract skill. It's knowing what context to give your AI colleague.

---

## Part 4 (15 min) — Document your bugs

Create a file `journal/bugs-learned.md`. For each bug you solved this session:

```markdown
## Bug N: [1-line description]
- **What was happening**: [symptom]
- **What I tried first**: [your first hypothesis]
- **What the real problem was**: [the cause]
- **How I fixed it**: [solution]
- **Lesson**: [what I learned]
```

Minimum 3 bugs documented. If you don't have 3, you're not coding enough. Keep going.

Commit + push.

---

## Part 5 (5 min) — Journal

`journal/session-4.md`:

1. What I learned today
2. What was hard
3. What I want to do next
4. **Bonus**: when did Claude get it wrong? Tell me in 2 sentences.

---

## Meta-lesson

> Programming isn't writing code that works. It's knowing what to do when it DOESN'T work.

70% of a professional programmer's time is debugging. AI sped it up but didn't eliminate it. What changed is:
- Before: reading Stack Overflow for hours
- Now: conversing with your AI about the bug, verifying

People who know how to verify what AI says will earn 2x what others earn. Today you started practicing it.

— Federico + Claude

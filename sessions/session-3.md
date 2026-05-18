# Session 3 — Your First Real Project

**Duration**: 90 minutes
**Deliverable**: project defined + working scaffold locally
**Meta-lesson**: defining scope = the most important programmer skill.

---

## The most important session of the course

This session is the most important one. Because you're going to decide **what you're going to build for the next 5 sessions**. If you pick something boring or way too big, you'll suffer. If you pick something good, you'll get obsessed and learn 3x more.

---

## Part 1 (30 min) — Brainstorming with Claude

Talk to Claude. Start like this:

```
I want to build a software project across the next 5 sessions. I'm new, I know basic Python, I just finished the first 2 sessions of the course.

Before suggesting ideas, ask me 5 questions to get to know me:
- What do I like to do in my free time
- What thing in the world or my daily life frustrates me
- What have I seen online and thought "I could make something like that"
- What app or tool I use every day that could be better
- Who would my project serve (my mom, my friends, strangers, myself)

Ask me one question at a time, listen to my answers, then propose 3 projects.
```

Answer honestly. **Don't say what you think Claude wants to hear. Say what you actually think.**

---

## Part 2 (15 min) — Pick your project

Claude will propose 3 ideas. Read them slowly.

For each one, ask yourself:
- Would I want to work on this outside of session hours?
- Could I explain it to my mom and she'd get it?
- Does it fit in 5 sessions of 90 min each?

If none feel right, ask:

```
None of these convince me 100%. Here's what I like / dislike about each. Propose 3 more.
```

Iterate until ONE excites you.

**Rules to not mess this up**:
- ❌ DON'T pick something just because it sounds impressive
- ❌ DON'T pick something that already exists exactly the same
- ❌ DON'T pick something "to get rich"
- ✅ Pick something YOU would use
- ✅ Pick something you can finish
- ✅ Pick something you can show on a single screen

---

## Part 3 (15 min) — Define the scope

Once picked, ask:

```
I want to define the MINIMUM scope of this project. I want something that works in 5 sessions, not something perfect.

Help me answer:
1. What exactly does this project do? (in one sentence)
2. For whom? (one specific person, not "everyone")
3. What are the 3 minimum features it must have?
4. What will it NOT have? (the hard part)
5. Where does it live? (web, terminal, mobile app, etc.)
```

**The trick**: the "what it will NOT have" list is more important than the features list. Write it well.

---

## Part 4 (20 min) — Scaffold

Ask:

```
Let's do the initial scaffold (folder structure, empty files) of this project. DON'T write code yet — just the structure.

What technologies do you propose? Why? Explain the options before choosing.
```

Learn to pick technology. Most important thing in this course.

When the plan is clear:

```
Create the scaffold in a new folder inside projects/. Do it step by step, explaining what each file does.
```

When you're done:

```bash
git add projects/
git commit -m "Session 3: scaffold of [YOUR PROJECT NAME]"
git push
```

---

## Part 5 (10 min) — Journal

`journal/session-3.md`:

1. **What I learned today**:
2. **What was hard**:
3. **What I want to do next**:
4. **My project is called**: _______
5. **It does**: _______
6. **For**: _______

Commit + push.

---

## Meta-lesson

> 90% of software projects fail not because the technology was bad, but because nobody defined well what they were going to be.

The questions you answered today (1-5 in the scope) are **literally the same ones that billion-dollar founders ask** before they start.

Don't memorize code. Memorize this process.

— Federico + Claude

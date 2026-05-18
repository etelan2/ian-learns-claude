# Session 7 — Teaching Claude Your Context

**Duration**: 90 minutes
**Deliverable**: your own `CLAUDE.md` for your project
**Meta-lesson**: AI without context = dumb AI. The real skill is giving it context.

---

## Before you start

- [ ] Your project deployed with public URL (session 6)
- [ ] At least 1 piece of feedback received

---

## The secret few people know

The difference between someone who **uses** Claude and someone who **works with** Claude is **context**.

If you open an empty conversation with Claude, it helps you like any random person. If you open a conversation with a Claude that already knows:
- Who you are
- What you're building
- Your tech preferences
- Your communication style
- The decisions you already made

...it helps you 10x better. It's like having a colleague who already knows your project vs an external consultant who arrives fresh every time.

Today you learn to give it that context.

---

## Part 1 (20 min) — What is CLAUDE.md

Ask Claude:

```
Explain what a CLAUDE.md file is. What's it for? How does Claude Code read it? What typical info goes in it? Show me short examples.
```

Read calmly.

**Key concept**: when there's a `CLAUDE.md` in a folder, Claude Code reads it automatically when it starts. It's persistent context. You don't have to repeat things every time.

---

## Part 2 (40 min) — Write your CLAUDE.md

You're going to create `CLAUDE.md` in the root of your project. It should contain (minimum):

### 1. Who you are
```markdown
# CLAUDE.md — [My project's name]

I'm Ian, 16, learning to code.
This project is [1-line description].
```

### 2. What the project does
```markdown
## What it does
- [feature 1]
- [feature 2]
- [feature 3]
```

### 3. Tech stack
```markdown
## Stack
- Language: [Python / Node / etc.]
- Framework: [if applicable]
- DB: [if applicable]
- Deploy: [Vercel / Render / etc.]
```

### 4. Your preferences
```markdown
## When you help me
- Talk in English, casual
- Explain things like I'm 16 (because I am)
- DON'T give me code I didn't ask for
- If I make a mistake, tell me WHY, don't just correct it
- One question at a time
```

### 5. Decisions already made
```markdown
## Decisions that are already made
- We're using [X] because [reason]
- We're NOT going to use [Y] even though it sounds good
- The minimum scope is [Z]
```

### 6. What you don't know yet
```markdown
## Things I'm still learning
- [topic 1]
- [topic 2]
```

Write it in your own words. Ask Claude to review:

```
Here's my CLAUDE.md. Is it clear? Is anything important missing? Is anything redundant or unnecessary?
```

Iterate 2-3 times until it's clean.

---

## Part 3 (15 min) — Test the effect

Close Claude Code. Reopen it from your project root. Start a new conversation:

```
Hi. Do you know what we're working on?
```

Claude should respond with real context about your project, without you telling it in this conversation. **That moment is magic.**

Ask for an improvement to your project. Compare the quality of its answer vs previous sessions. Now it knows who you are, what you're building, and how you like to work.

---

## Part 4 (10 min) — Skills (advanced, optional)

If you have time left:

```
Claude Code has something called "Skills". Explain what they are. Does it make sense for me to create one for my project? Which one?
```

If it fits, create one. If not, save it for later.

---

## Part 5 (5 min) — Journal

`journal/session-7.md`:

1. What I learned today
2. What was hard
3. **Before CLAUDE.md, my conversations with Claude were**: _______
4. **After CLAUDE.md, they are**: _______
5. What I want to do next

Commit + push.

---

## Meta-lesson

> The most valuable skill of programming with AI in 2026 isn't writing prompts. It's building persistent context the AI can read.

What you did today is called **context engineering**. It's new. 6 months ago the term didn't even exist. In 2 years it'll be a common job description.

You're already practicing it. At 16. That's valuable.

— Federico + Claude

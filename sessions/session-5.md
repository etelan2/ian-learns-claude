# Session 5 — Talking to the World

**Duration**: 90 minutes
**Deliverable**: your project consumes or serves real data (API, file, DB)
**Meta-lesson**: software lives in systems, not in lonely files.

---

## Before you start

- [ ] Your project has 1-2 features working locally
- [ ] You've solved at least 3 documented bugs

---

## Today your project crosses a border

Until today, your project lives on your Mac. Today it's going to:
- Request data from another system (API), OR
- Save persistent data (DB, file), OR
- Receive data from an external user

That turns it into **real software**, not a homework script.

---

## Part 1 (20 min) — Decide which "connection" to make

Ask Claude:

```
Today my project does [X]. To make it more real, I want to connect it with something from the outside world.

I have 3 options:
1. Consume a public API (e.g., weather, quotes, images, whatever)
2. Save data in a local file or database
3. Receive input from a user via web/terminal

For MY specific project, which one makes most sense and why? Give me 3 specific options and vote for one.
```

Read its recommendation. Decide.

---

## Part 2 (15 min) — Learn the concept

If you picked **API**:
```
Explain what an API is. How does the client-server flow work? Give me a simple analogy. Then show me a simple Python example that calls an API.
```

If you picked **DB**:
```
Explain what a database is. For my project, which type is best (SQLite, JSON file, other)? Give me a simple analogy.
```

If you picked **user input**:
```
Explain how to receive user input. CLI, web form, both? For my project, which makes sense?
```

---

## Part 3 (40 min) — Implement

Build the connection. Same rules as before:
- One question at a time to Claude
- Read every line of code it gives you
- If you don't understand, ask BEFORE copying
- When something doesn't work, paste the literal error

**Important tip**: APIs and DBs require handling **secrets** (API keys, passwords). NEVER put these in your code directly. Ask Claude:

```
How do I properly handle credentials (API keys, passwords) in my project? I want to do it right from the start.
```

It'll teach you about `.env` files and `.gitignore`. **That lesson is worth gold.**

---

## Part 4 (10 min) — Verify end-to-end

Once it works:

1. Delete test data
2. Run the full flow from zero
3. Does it work?
4. Any edge case you missed? (empty data, no internet, weird format)

Ask Claude:

```
My connection works in the happy case. What edge cases should I test? Give me a list of 5 and we'll test them together.
```

---

## Part 5 (5 min) — Journal

`journal/session-5.md`:

1. What I learned today
2. What was hard
3. What I want to do next
4. **New connection**: what does my project do now that it couldn't before?

Commit + push.

---

## Meta-lesson

> Software that doesn't talk to anything is a script. Software that talks to external systems is a product.

What you learned today is called **integration**. It's what separates someone who "knows Python" from someone who "builds products".

Your next project will have integrations from day 1. That's the normal pattern in 2026.

— Federico + Claude

# Session 1 — Hello Claude

**Duration**: 90 minutes
**Deliverable**: Claude Code installed on your Mac + first "hello world" + Claude account working
**Meta-lesson**: AI isn't a search engine. It's a colleague who talks with you.

---

## Before you start

Make sure you have:
- [ ] Your Mac with you, on, with WiFi working
- [ ] Your personal email at hand (you'll create accounts)
- [ ] 90 minutes free, no interruptions

---

## Part 1 (15 min) — Create your Claude account

1. Open Safari or Chrome
2. Go to **claude.ai**
3. Click "Sign up"
4. Use your personal email
5. Create a password (something secure you'll remember — write it on physical paper, NOT in a digital note)
6. Confirm your email

**Federico is going to upgrade your account to Pro ($20 USD/month) — that unlocks Claude Code.**

---

## Part 2 (20 min) — Install Claude Code on your Mac

You're going to open the **Terminal** (the app that looks like a black screen with text). To open it:

1. Press `Cmd + Space`
2. Type "Terminal"
3. Enter

You'll see something like:
```
ian@MacBook ~ %
```

That `%` symbol means "the computer is waiting, type something".

### Install Claude Code

Copy and paste THIS line (exactly, don't change anything):

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Press Enter. It'll take 1-2 minutes.

### Log in

When the install finishes, type:

```bash
claude
```

It'll ask you to log in. Follow the instructions on screen — it'll open your browser, you connect your claude.ai account, done.

### Verify it worked

Type:

```bash
claude --version
```

If you see a version number (something like `2.x.x`), it worked. **If you see an error, ask Claude for help.**

---

## Part 3 (10 min) — Your first conversation with Claude

In Terminal, type:

```bash
claude
```

You'll enter a conversation with Claude. Type this exactly:

```
Hi Claude, I'm Ian. I'm 16 years old and I'm learning to code with you. I'm a former student of Federico Peña at the Algorítmica school. Can you briefly explain what you'll be able to do with me throughout this course?
```

Read what it tells you. **Don't type the next thing until you finish reading.**

When you've read it, type:

```
What's the difference between you and Google? When I ask Google something, it gives me pages. When I ask you something, you give me what exactly?
```

Read the answer. **The meta-lesson here**: you're learning to talk to an AI in natural language. It's not a search engine. It's a colleague.

---

## Part 4 (30 min) — Your first "Hello World"

We're going to make your Mac say "Hello, world" but your way.

Ask Claude:

```
I want my Mac to say "Hello, world" but in a fun way, with my name. I'm Ian. Don't give me the code yet — first ask me what kind of "fun" I want.
```

Claude will ask you what you like. You decide:
- Colored text?
- Like a conversation?
- With emojis?
- Something else you come up with?

Once you reply, Claude will write the code. **Read it line by line with Claude.** If you don't understand something, ask:

```
Wait, what does this line do? Explain it like I'm 12.
```

Once you understand, save it in a file. Ask:

```
Help me save this in a file called hello.py. How do I do it step by step?
```

Run the program. Ask:

```
How do I run it from Terminal?
```

**When it works**: take a screenshot of the result on your screen. Send it to Federico. It's a historic moment — it's your first real program.

---

## Part 5 (10 min) — Journal

Open your editor (we'll cover which one next session — for now you can use the **Notes** app on your Mac).

Create a note titled "Session 1 — Hello Claude" and write (minimum) three sentences:

1. **What I learned today**:
2. **What was hard**:
3. **What I want to do next**:

Send Federico a screenshot of your journal entry. That's your session close.

---

## If you got stuck

- **If a command doesn't work**: ask Claude directly. Copy and paste the error you got.
- **If Claude says something you don't understand**: reply "explain it simpler".
- **If you get frustrated**: close the laptop 5 minutes. Come back. Frustration is normal.
- **If nothing works after 15 min**: message Federico. Don't stay stuck for half an hour.

---

## Meta-lesson of this session

The AI **doesn't know what you want** until you tell it. The most important skill you'll learn in this course is:

> **Knowing how to explain to an AI what you want to build, step by step, in your own words.**

That's not learned in one session. It's learned in 8. But you already started.

Welcome to the course, Ian. Welcome to 2026.

— Federico + Claude

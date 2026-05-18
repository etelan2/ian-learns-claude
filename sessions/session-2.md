# Session 2 — Your Repo, In The World

**Duration**: 90 minutes
**Deliverable**: GitHub account + your first public repo + README written by you
**Meta-lesson**: what you write in code exists permanently. Git is your memory.

---

## Before you start

- [ ] Session 1 completed
- [ ] Your hello.py working
- [ ] Session 1 journal entry written

---

## Part 1 (15 min) — Create a GitHub account

GitHub is where the world's code lives. Linux, Python, Claude Code — everything is on GitHub.

1. Go to **github.com**
2. Sign up with your email
3. Your username: think carefully — it'll be your identity as a programmer forever. Suggestion: `ian-pa` or `ian-yourlastname` (something based on your REAL name, not random). Avoid numbers if you can.
4. Confirm your email

**Once inside**, ask Claude:

```
I just created my GitHub account. My username is [YOUR_USERNAME]. What is GitHub and why does it matter that I have an account?
```

Read the answer.

---

## Part 2 (20 min) — Install git on your Mac

It's probably already installed. Ask Claude:

```
How do I check if git is installed on my Mac? If it's not, how do I install it?
```

Follow its instructions step by step. When done, ask:

```
How do I connect my local git with my GitHub account? My username is [YOUR_USERNAME] and my email is [YOUR_EMAIL].
```

---

## Part 3 (30 min) — Your first repo

Ask Claude:

```
I want to create a repo on GitHub called "ian-learns-claude". It'll be where I save everything I learn in this course. How do I do it step by step?
```

It'll guide you through:
1. Creating the repo on github.com (green "New" button)
2. `git clone` to your Mac to have it locally
3. Move your `hello.py` into it
4. Run `git add`, `git commit`, `git push`

**When you push and see your code on GitHub.com → that's the key moment.** Your code is on the internet. It's public. It's yours.

---

## Part 4 (20 min) — README in markdown

Every serious repo has a README. It's the cover.

Ask Claude:

```
I want to write a README for my repo. What is markdown? How does it work? Give me short examples.
```

Practice with him. Learn:
- `# Big title`
- `## Subtitle`
- `**bold**`
- `- lists`
- `[link](https://...)`
- ` ```code block``` `

Create your README. Ask Claude to help, but YOU write the content. It should answer:
- Who are you?
- What is this repo?
- Why are you learning?

Make it personal. Don't copy generic templates. **Your README is your introduction to the programmer world.**

Commit + push.

---

## Part 5 (5 min) — Journal

Open `journal/session-2.md` (create it if it doesn't exist):

1. What I learned today
2. What was hard
3. What I want to do next

Commit + push. **Your journal is on GitHub too now.**

---

## Meta-lesson

> Git is the one tool that every programmer in the world has used for the past 20 years. You'll use it every day for the rest of your life if you go into this.

You don't need to master it now. Just get familiar. The things we'll use 100 more times:
- `git add .` (stage changes)
- `git commit -m "message"` (save them)
- `git push` (upload to the world)
- `git pull` (download changes from the world)

You learn them with your hands, not your head. In 4 more sessions you'll do them without thinking.

— Federico + Claude

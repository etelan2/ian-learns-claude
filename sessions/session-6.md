# Session 6 — Deploy

**Duration**: 90 minutes
**Deliverable**: your project LIVE on the internet, with a public URL
**Meta-lesson**: your work can be used by real humans.

---

## Before you start

- [ ] Your project works locally with integration (session 5)
- [ ] Pushed to GitHub

---

## The day your project goes out into the world

Until today, only you could use your project (because it runs on your Mac). Today you're going to put it on the internet. Anyone in the world will be able to open your URL and use it.

That's **deploy**. It's the moment you stop being "someone learning to code" and start being "someone who builds things for real people".

---

## Part 1 (15 min) — Pick where to deploy

Ask Claude:

```
My project is in [Python/Node/etc.] and does [X]. I want to deploy it.

The easy options I know are:
- Vercel
- Cloudflare Pages
- Render
- Railway
- GitHub Pages

For MY specific project, which is the best option? Let's compare pros and cons of the 2 most relevant for my case.
```

Read. Decide.

---

## Part 2 (40 min) — Do the deploy

Ask:

```
Let's deploy on [chosen platform]. Do it step by step. Tell me before each step because I want to understand what's happening.
```

What'll happen (it's normal):
- It'll ask you to create an account on the platform
- It'll ask you to connect your GitHub
- It'll ask you to configure environment variables (the `.env` you learned in session 5)
- There'll be at least one error on the first attempt

**When it fails**: check the logs. Ask Claude:

```
The deploy failed. Here are the logs: [paste fully]
What happened? What do we need to change?
```

Iterate until it works.

---

## Part 3 (15 min) — Share your URL

When you have your public URL working:

1. **Open your project from your phone** (not your Mac). If it works there too, it's real.
2. **Share it with 3 people**:
   - Federico (obviously)
   - Your mom
   - A friend
3. Ask them to use it. To tell you what they think.

**Document the first feedback you get.** Even if it's bad. It'll be valuable info.

---

## Part 4 (15 min) — Basic monitoring

Ask:

```
My project is on the internet. How do I know if it's running? What if it crashes? How do I find out?

Set up something simple to know my project's status without having to open it every time.
```

Learn about uptime monitoring (free with UptimeRobot or similar). Configure it.

---

## Part 5 (5 min) — Journal

`journal/session-6.md`:

1. What I learned today
2. What was hard
3. **My public URL**: _______
4. **First feedback I got**: _______
5. **What I'd change based on the feedback**: _______

Commit + push.

**Bonus**: add a badge to your README with your deployed URL:

```markdown
🌐 **Live**: [YOUR_URL_HERE](https://...)
```

---

## Meta-lesson

> Until real people use it, it's not a product. It's an exercise.

Today was the most important day of the course. People who finished session 6 are on another level than people who only "learned Python".

— Federico + Claude

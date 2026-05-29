# AI with Ant — A Personal AI Operating System

> AI as an operating system, not a chat window.
> **Persistent memory first. Skills on top.**

This repo is the open blueprint behind [AI with Ant](https://aiwithant.com) — building a personal AI operating system that actually *remembers*.

Most people use AI as a vending machine. Walk up, type a question, get an output, walk away. Tomorrow they do the same dance, and the model remembers nothing. That's not "using AI." That's renting it by the minute.

The fix isn't a sharper prompt or a newer tool. It's **memory.** Give your AI a persistent, cross-surface place to remember — and a rule for what goes where — and it stops being a chat window and starts being an operating system. Everything you build on top compounds instead of resetting to zero every Monday.

---

## The system

The memory is a **hybrid** of two pieces, on purpose:

- **Open Brain** — a *capture* layer you can write to from any surface (phone, laptop, Claude Code, ChatGPT, the browser). Frictionless in, nothing lost. Built as an MCP server on Supabase, so every tool shares the same memory.
- **The vault** — a *synthesize* layer: an Obsidian / markdown knowledge base in git. The canonical source of truth your AI reads before it does anything.

Connected by one rule:

> **Capture once. Synthesize in the vault. Produce many.**

![The hybrid memory architecture: capture (Open Brain) → synthesize (the vault) → produce (Skills) → publish.](diagrams/hybrid-memory-architecture.png)

Once that substrate exists, you build **Skills** on top of it for the role you actually do — Sales, CSM, PM, Creator. Same memory, different Skills. The full design and the reasoning behind every layer is in **[`ARCHITECTURE.md`](ARCHITECTURE.md) — start there.**

---

## Why memory-first

A persistent, indexed memory isn't a nice-to-have. It changes the economics and the capability of everything downstream:

- **Lower token cost** — Skills retrieve only the pages a job needs instead of dumping whole transcripts and documents into every prompt. You stop re-explaining your world each session.
- **Indexed recall** — captures are stored with vector embeddings, so you find things by *meaning*, not by remembering where you filed them.
- **A knowledge graph** — the vault links entities, decisions, and people, so the model traverses relationships instead of scanning a flat list.
- **Flexible collection → synthesis** — capture loose and fast from anywhere; impose structure later, when captures get distilled into canonical vault pages. Loose in, structured out.

The full argument is in [`ARCHITECTURE.md`](ARCHITECTURE.md#what-the-hybrid-buys-you).

---

## What's in here

| Path | What it is |
|---|---|
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | **The system.** The hybrid memory model — Open Brain + the vault, how capture works, and why the split. **Read this first.** |
| [`METHOD.md`](METHOD.md) | **The method.** Map / Build / Run — how to turn that memory into Skills for the role you actually do. |
| [`diagrams/`](diagrams/) | Reference architectures — the hybrid memory stack, the dual-chain prompt flow, more. |
| [`case-studies/`](case-studies/) | Real builds on this system — standing up the memory substrate, the creator pipeline, more as they ship. |
| [`templates/`](templates/) | Field-log post templates, for publishing what you build. Supporting material. |
| [`brand-book/`](brand-book/) | Voice guide and visual system, for anyone forking and publishing. Supporting material. |

---

## How to use this repo

It's a stack. Build it bottom-up.

**1. Stand up the memory — the foundation.**
Follow [`ARCHITECTURE.md`](ARCHITECTURE.md): stand up a capture layer ([Open Brain / OB1](https://github.com/NateBJones-Projects/OB1)), start a vault as a private git repo, and wire the rule. Push the vault to a remote so it's reachable from any machine — and from Claude Code on the web, which clones the repo into each session. The whole brain travels with a `git clone`.

**2. Build Skills on top — the work.**
With memory in place, use [`METHOD.md`](METHOD.md) to map your role, then spec and build Skills that read the vault and capture. Start with the most boring, most repetitive job you do — that's where leverage lives. Ship one Skill this week.

**3. Publish what you build — optional.**
If you write in public, the [newsletter templates](templates/newsletter/) and [brand-book](brand-book/) are the same field-log voice and visual system used in AI with Ant. Copy, fill, ship.

---

## Who this is for

- **Operators** with a Claude or ChatGPT subscription they're barely using
- **Sellers** who want AI woven into the workflow already running, not bolted on
- **Creators** with a publishing cadence who need leverage on what they already ship
- **Builders** of any role — PMs, CSMs, founders, ops — who think in systems and want to point that muscle at AI

If you've ever opened ChatGPT, asked a brilliant question, gotten a useful answer, and then closed the tab and forgot you'd done it by Wednesday — this is for you. Memory is the difference.

---

## The companion newsletter

This repo is the open blueprint. The applied build logs, tool teardowns, and case studies ship in the newsletter:

**→ [Subscribe to AI with Ant — Field Notes](https://aiwithant.com)** — free, weekly, every issue ends with one specific thing you can use.

---

## License

[MIT](LICENSE). Fork it, use it commercially, modify it, build a business on it. Attribution is appreciated but not required. The point is for the system to travel.

If you ship something built on this, tag [@AnthonyMBrown](https://www.linkedin.com/in/anthonymbrown/) on LinkedIn. I love seeing how other operators install their own versions.

---

— Anthony Brown
*Field Notes from the AI Operating System*

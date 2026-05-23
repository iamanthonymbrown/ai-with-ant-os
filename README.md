# AI with Ant — The Open Method

> AI as an operating system, not a chat window.
> **Map. Build. Run.**

This repo is the open methodology behind [AI with Ant](https://aiwithant.com) — the field-log newsletter on building personal AI operating systems for knowledge-worker roles.

Most people use AI as a vending machine. Walk up, type a question, get an output, walk away. Tomorrow they do the same dance, and the model remembers nothing. That's not "using AI." That's renting it by the minute.

The alternative: treat your role as a system worth architecting. Map the work, build the Skills, run the adoption. The frame is portable. Sales OS, CSM OS, PM OS, Creator OS — same method, different chains, different rule, different Skills.

This repo gives you the templates, prompts, and reference architecture to install your own.

---

## What's in here

| Path | What it is |
|---|---|
| [`METHOD.md`](METHOD.md) | The Map / Build / Run framework in long form. Start here. |
| [`prompts/slack-skill-builder.md`](prompts/slack-skill-builder.md) | The 400-line system prompt that turns Claude into a Slack Skill architect. Drop into Claude Projects, describe a workflow, get a complete implementation-ready spec. |
| [`templates/newsletter/`](templates/newsletter/) | Four post templates — Build Log, Teardown, Field Note, The Long Lens. Copy, fill in, ship. |
| [`brand-book/`](brand-book/) | Voice guide and visual system for anyone forking the method. |
| [`diagrams/`](diagrams/) | Reference architectures — the AI Sales OS dual-chain prompt flow, the Skills inventory, etc. |
| [`case-studies/`](case-studies/) | Real builds — the 18-Skills-in-2-weeks story, the Masters putt creator pipeline, more as they ship. |

---

## Who this is for

- **Operators** with a Claude or ChatGPT subscription they're barely using
- **Sellers** who want AI woven into the workflow already running, not bolted on
- **Creators** with a publishing cadence who need leverage on what they already ship
- **Builders** of any role — PMs, CSMs, founders, ops — who think in systems and want to point that muscle at AI

If you've ever opened ChatGPT, asked a brilliant question, gotten a useful answer, and then closed the tab and forgot you'd done it by Wednesday — this is for you.

---

## How to use this repo

**Quickest path — ship one Slack Skill this week:**

1. Read [`METHOD.md`](METHOD.md) — about 10 minutes
2. Copy the [Slack Skill Builder prompt](prompts/slack-skill-builder.md) into Claude (Claude Projects works best)
3. Describe one workflow you do constantly — pre-call prep, recap emails, customer questions, whatever
4. Follow the conversation it runs with you
5. You'll have a complete, implementation-ready Skill spec in about 15 minutes

**Building your own role-based AI OS:**

1. [`METHOD.md`](METHOD.md) for the framework
2. [`diagrams/ai-sales-os-prompt-flow.png`](diagrams/) as the reference architecture
3. Adapt the dual-chain structure (Early Chain quarterly + Daily Chain in-flow) to your role
4. Use the Skill Builder prompt to spec each Skill in your chain
5. Ship, iterate, repeat

**Writing in the field-log style:**

The four [newsletter templates](templates/newsletter/) are the same ones used in [AI with Ant — Field Notes](https://aiwithant.com). Copy them whole, fill them in, delete the GUIDE notes.

---

## The companion newsletter

This repo is the open method. The applied case studies, ongoing build logs, and tool teardowns ship in the newsletter:

**→ [Subscribe to AI with Ant — Field Notes](https://aiwithant.com)**

Free. Ships every week. Every issue ends with one specific thing you can use.

The full installable AI OS — every prompt, every Skill spec, the dual-chain configuration, the deployment playbook, the troubleshooting — lives in the paid tier of the newsletter. Coming soon.

---

## License

[MIT](LICENSE). Fork it, use it commercially, modify it, build a business on it. Attribution is appreciated but not required. The point is for the method to travel.

If you ship something built on this, tag [@AnthonyMBrown](https://www.linkedin.com/in/anthonymbrown/) on LinkedIn. I love seeing how other operators install their own versions.

---

— Anthony Brown
*Field Notes from the AI Operating System*

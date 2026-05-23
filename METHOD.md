# The Method — Map. Build. Run.

A working framework for installing a personal AI operating system on the role you actually do.

---

## Why this exists

Most "how to use AI" content tells you what model to use, what prompt to write, what tool to buy. None of it tells you the part that actually matters: **how to make the thing stick after the novelty wears off.**

Two years of AI-tool subscription fatigue have proven a thing most people won't say out loud — better prompts don't make AI stick. Better tools don't make AI stick. What makes AI stick is **architecture.** Treating your role as a system worth designing, not a series of tasks waiting for a magic answer.

This is the framework I used to build my own AI OS — 18 Slack Skills and an 8-step territory intelligence chain — in two weeks.

It works because it splits the problem into three jobs that need different kinds of thinking. Map is a thinking problem. Build is a craft problem. Run is a behavior problem. Most people try to solve all three at once with prompts. That's why it fails.

---

## Map — See the work before you build any of it

You can't automate a role you can't describe.

Most operators skip this step. They open Claude, sit there trying to think of "a cool thing to automate," and twenty minutes later they close the tab. They started in Build mode when they hadn't finished Map.

Mapping is mostly *seeing*. Before you write a single prompt, you answer three questions:

**1. What's the work you do constantly?**
Not the work you wish you did more of. The work that already shows up in your week — pre-call prep, status updates, recap emails, content scheduling, customer questions you answer for the fifth time. The boring, repeating stuff. That's the right pool. Important work is too rare to automate well; repetitive work is where leverage lives.

**2. Where does the context for that work already live?**
Slack threads, CRM fields, Google Docs, your calendar, your inbox. If the context is already somewhere a Skill can reach, the build is short. If it lives only in your head, the build is hard. Map your role's data, not your role's tasks. The data tells you what's automatable.

**3. What's the natural cadence of the work?**
This is the one people miss. Some work is daily (call prep, recaps, in-flow execution). Some work is quarterly (territory planning, account scoring, persona research). If you try to build both inside the same system, the cadence blurs and both break. Map the work into *project cadence* (quarterly, episodic) and *flow cadence* (daily, on-trigger). These become your two chains.

The output of Map is a list of named work, with context sources and cadence flagged for each. It's a document, not a system. You don't need anything to build it except a quiet hour and honesty about what your job actually looks like.

---

## Build — Turn the map into Skills that run where the work happens

Build is where most "AI tutorials" start, and that's why most "AI tutorials" fail.

A Skill is one focused capability: a clear trigger, defined inputs, defined behavior, defined outputs, a minimal permission footprint. Not a "use case." Not a "workflow." One job, one trigger, one output. If a Skill is doing two jobs, decompose it into two Skills.

### The dual-chain architecture

When you split work by cadence (project vs. flow), you naturally get two chains:

- **Early Chain** runs at project cadence (quarterly, episodic). Lives wherever you do focused work — Claude Projects, a custom environment, a research workspace. Produces artifacts: territory plans, audience research, content calendars, system designs.
- **Daily Chain** runs at flow cadence (daily, on-trigger). Lives where the work actually happens — Slack, your CRM, your editor, your calendar. Fires when an event happens (a meeting books, a deal stage changes, a deadline approaches).

The two chains hand work to each other through a single architectural seam:

> **Project work outputs an artifact → trigger event fires → Daily chain takes over**

For my AI Sales OS, that seam is *"meeting booked → Slack Skills take over."* Eight prompts produce the territory intelligence and the outbound sequence; the moment a prospect books a meeting, five Slack Skills execute against that account in-flow. The Early Chain doesn't have to know about the Daily Chain. The Daily Chain doesn't have to know how the Early Chain built the context. They share an artifact, not state.

### The core rule

Every working OS has a single organizing rule that holds everything together. Mine is *"account status drives the motion"* — every Skill knows the account's tier and adjusts what it does accordingly.

Yours might be different:
- A CSM OS might run on *"renewal proximity drives the motion"*
- A PM OS might run on *"customer signal volume drives the motion"*
- A Creator OS might run on *"content cadence drives the motion"*

The core rule is what makes the system feel coherent instead of like a pile of clever automations. Without it, you have Skills. With it, you have an OS.

### Building one Skill at a time

The first Skill you ship will take 2-3 hours. The second will take 90 minutes. The fifth will take 30. By the tenth, you'll wonder how anyone works without one.

That's not the model getting better. That's the **system building the system** — every Skill you ship teaches you something that makes the next one easier to scope, faster to write, cheaper to test. Compounding leverage isn't a metaphor here; it's the build mechanic.

Start with the most boring, most repetitive Skill in your map. Reads, not writes. Read-only Skills can't damage anything if they're wrong. Save writes for Skill #3 or later, once you trust your design instincts.

The [Slack Skill Builder prompt](prompts/slack-skill-builder.md) in this repo handles the hard part of writing a Skill spec. You bring the workflow description; it produces an implementation-ready spec including trigger, inputs, behavior, integrations, outputs, scopes, error handling, and guardrails.

---

## Run — Adoption is the part nobody teaches

You've built the system. Most people stop here. Six weeks later they're back to using AI as a chat window, wondering why nothing changed.

Run is the part where the system becomes the way you work, not a thing you remember to use. It's mostly about removing yourself from the loop:

- **Trigger-based, not request-based.** A Skill that fires automatically on a calendar event is infrastructure. A Skill you have to remember to invoke is a tab. Wherever possible, design for triggers.
- **In-flow, not in-context-switch.** The Skill lives where the work happens. If the work happens in Slack, the Skill is a Slack Skill. If it happens in your inbox, it's a Gmail Skill. If it happens in your CRM, it's a CRM Skill. Forcing the operator to switch contexts to use the system is the same as not having the system.
- **Feedback to the design, not to the user.** When a Skill produces a bad output, the fix is to update the spec, not to tell the user "you should have prompted it differently." Operators don't have spare cognitive load. The system absorbs the failure modes.
- **Adoption metrics, not feature metrics.** "Number of Skills" is a vanity metric. "Number of workflows now running on Skills without manual prompting" is the real number. If adoption is flat, the system isn't working — no matter how many Skills you've built.

Adoption is also where the system gets honest. Skills that don't get used die quietly. Skills that get used constantly graduate into infrastructure. Six months in, you'll have a clear picture of which Skills earned their place and which ones were good ideas you talked yourself into.

---

## Applying this to your role

The method is portable. Some examples of how the same architecture lands across roles:

**AI Sales OS** (the one I built)
- Core rule: account status drives the motion
- Early Chain (quarterly): territory operations, ICP scoring, whitespace mapping, contact mapping, trigger detection, account planning, persona research, outbound sequencing
- Handoff: meeting booked
- Daily Chain (in-flow): account brief, discovery questions, call summary, pipeline operations, weekly review

**AI CSM OS** (one operator's adaptation)
- Core rule: renewal proximity drives the motion
- Early Chain (quarterly): account health planning, expansion mapping, advocacy identification, executive briefing prep
- Handoff: 90 days to renewal
- Daily Chain (in-flow): customer signal monitoring, escalation handling, executive update drafting, churn-risk surfacing

**AI PM OS**
- Core rule: customer signal volume drives the motion
- Early Chain (monthly): roadmap planning, customer research synthesis, competitive landscape, opportunity scoring
- Handoff: PRD start
- Daily Chain (in-flow): spec drafting from Slack discussions, sprint review prep, customer-feedback aggregation, stakeholder update generation

**AI Creator OS**
- Core rule: content cadence drives the motion
- Early Chain (quarterly): content strategy, lane mix planning, topic bank curation, series design
- Handoff: topic landed in week's slot
- Daily Chain (in-flow): research compilation, draft writing, voice auditing, image generation, distribution sequencing

Same method, different chains, different rule, different Skills. Same OS.

The point isn't to copy one of these literally. The point is to recognize the shape — Map / Build / Run, two chains, one rule, an architectural seam — and apply that shape to your role.

---

## What this method is not

- **It's not "AI literacy."** This is about systems thinking applied to AI tools. If you don't already know what Claude does, this isn't your starting point — go use AI as a chat window for a week first.
- **It's not a no-code framework.** You'll write specs, configure integrations, possibly hand specs to a developer for some Skills. The Skill Builder prompt reduces this work significantly but doesn't eliminate it.
- **It's not a product.** It's the method behind a product (the [AI with Ant](https://aiwithant.com) newsletter and the future AI OS install playbook). The method itself is open — fork it, use it, build with it.
- **It's not finished.** I'll be adding case studies, refined templates, and new architectural patterns over time. PRs welcome.

---

## Next

- Read the [Slack Skill Builder prompt](prompts/slack-skill-builder.md) and ship one Skill this week
- Pick a [newsletter template](templates/newsletter/) and write your first field note
- Subscribe to [AI with Ant — Field Notes](https://aiwithant.com) for ongoing build logs, teardowns, and case studies

— Anthony Brown

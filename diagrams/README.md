# Diagrams

Reference architectures for the AI with Ant method.

## Available

- [`hybrid-memory-architecture.png`](hybrid-memory-architecture.png) — the four-layer OS stack from [`ARCHITECTURE.md`](../ARCHITECTURE.md): Capture (Open Brain) → Synthesize (the markdown vault) → Produce (Skills) → Publish, with the *capture once, synthesize, produce many* rule running through it. Regenerate with [`hybrid-memory-architecture.py`](hybrid-memory-architecture.py) (`python3 diagrams/hybrid-memory-architecture.py`, needs Pillow).

## Coming soon

- `ai-sales-os-prompt-flow.png` — the dual-chain prompt flow diagram. An Early Chain at project cadence + a Daily Chain in-flow + the handoff seam between them, as an example of the Produce layer.
- Role-specific OS diagrams as readers ship and share theirs (CSM OS, PM OS, Creator OS, etc.)

If you've built a role-based AI OS using this method and want your diagram included, open a PR.

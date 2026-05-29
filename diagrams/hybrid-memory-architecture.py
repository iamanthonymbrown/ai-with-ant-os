#!/usr/bin/env python3
"""Render the hybrid memory architecture diagram in the AI with Ant palette.

Output: diagrams/hybrid-memory-architecture.png
Run:    python3 diagrams/hybrid-memory-architecture.py
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# --- Brand palette --------------------------------------------------------
INK     = (14, 15, 18)      # #0E0F12 background
PANEL   = (20, 22, 27)      # box fill
BORDER  = (42, 45, 52)      # box border
CREAM   = (247, 250, 237)   # #F7FAED primary text
MUTED   = (138, 144, 152)   # secondary text
LIME    = (212, 255, 26)    # #D4FF1A accent (used sparingly)

S = 2  # supersample factor for crisp text
W, H = 1600 * S, 1080 * S
MARGIN = 70 * S

FONTS = {
    "reg":  "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    "bold": "/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf",
}


def font(kind, px):
    return ImageFont.truetype(FONTS[kind], px * S)


img = Image.new("RGB", (W, H), INK)
d = ImageDraw.Draw(img)


def text(xy, s, f, fill, anchor="la"):
    d.text(xy, s, font=f, fill=fill, anchor=anchor)


def tw(s, f):
    return d.textlength(s, font=f)


# --- Title ----------------------------------------------------------------
text((MARGIN, 44 * S), "THE HYBRID MEMORY ARCHITECTURE", font("bold", 34), CREAM)
# lime underline accent (the one lime element up top)
d.rectangle([MARGIN, 92 * S, MARGIN + 470 * S, 96 * S], fill=LIME)
text((MARGIN, 104 * S),
     "How the OS remembers — so Skills compound instead of starting from zero.",
     font("reg", 17), MUTED)

# --- Surfaces row ---------------------------------------------------------
sy = 156 * S
text((MARGIN, sy), "ANY SURFACE", font("bold", 14), MUTED)
chips = ["phone", "laptop", "Claude Code", "claude.ai", "ChatGPT", "browser"]
cx = MARGIN + 150 * S
for c in chips:
    w = tw(c, font("reg", 15)) + 28 * S
    d.rectangle([cx, sy - 6 * S, cx + w, sy + 26 * S], outline=BORDER, width=S)
    text((cx + 14 * S, sy + 4 * S), c, font("reg", 15), CREAM)
    cx += w + 14 * S

# --- Layer boxes ----------------------------------------------------------
BX0, BX1 = MARGIN, W - MARGIN
BOX_H = 150 * S
GAP = 56 * S
start = 210 * S

layers = [
    ("01", "CAPTURE", "OPEN BRAIN · OB1",
     "One memory you can write to from anywhere. Frictionless in, nothing lost.",
     "MCP server · Supabase edge function · Postgres + pgvector",
     "INDEXED · ANY SURFACE"),
    ("02", "SYNTHESIZE", "THE VAULT · OBSIDIAN + GIT",
     "Captures distilled into canonical pages. Sources rewrite, not append.",
     "markdown · git-versioned · obsidian-second-brain skill",
     "KNOWLEDGE GRAPH"),
    ("03", "PRODUCE", "SKILLS · MAP / BUILD / RUN",
     "Pull only the pages a job needs — not the whole archive into context.",
     "Early Chain (project cadence) · Daily Chain (in-flow)",
     "LOWER TOKEN COST"),
    ("04", "PUBLISH", "NEWSLETTER · SOCIAL · VIDEO",
     "Published work is a render of the vault — never the original.",
     "Substack · Beehiiv · LinkedIn · YouTube",
     "ONE BRAIN → MANY"),
]


def chevron(cy):
    cxm = (BX0 + BX1) // 2
    d.line([cxm, cy, cxm, cy + GAP - 10 * S], fill=LIME, width=2 * S)
    s = 9 * S
    d.line([cxm - s, cy + GAP - 10 * S - s, cxm, cy + GAP - 10 * S], fill=LIME, width=2 * S)
    d.line([cxm + s, cy + GAP - 10 * S - s, cxm, cy + GAP - 10 * S], fill=LIME, width=2 * S)


y = start
for i, (num, name, tool, desc, tech, tag) in enumerate(layers):
    d.rectangle([BX0, y, BX1, y + BOX_H], fill=PANEL, outline=BORDER, width=S)
    # left lime accent bar (one lime element per box)
    d.rectangle([BX0, y, BX0 + 8 * S, y + BOX_H], fill=LIME)
    tx = BX0 + 34 * S
    text((tx, y + 22 * S), num, font("bold", 30), MUTED)
    text((tx + 70 * S, y + 24 * S), name, font("bold", 26), CREAM)
    text((tx + 70 * S, y + 60 * S), tool, font("bold", 15), LIME)
    text((tx + 70 * S, y + 86 * S), desc, font("reg", 17), CREAM)
    text((tx + 70 * S, y + 116 * S), tech, font("reg", 14), MUTED)
    # benefit tag, right-aligned outline pill
    tf = font("bold", 14)
    pw = tw(tag, tf) + 28 * S
    px1 = BX1 - 24 * S
    px0 = px1 - pw
    d.rectangle([px0, y + 22 * S, px1, y + 54 * S], outline=LIME, width=S)
    text(((px0 + px1) / 2, y + 38 * S), tag, tf, LIME, anchor="mm")
    if i < len(layers) - 1:
        chevron(y + BOX_H)
    y += BOX_H + GAP

# --- Footer: the rule -----------------------------------------------------
fy = y + 6 * S
d.line([MARGIN, fy, W - MARGIN, fy], fill=BORDER, width=S)
rule = "THE RULE   capture once  ·  synthesize in the vault  ·  produce many"
text((MARGIN, fy + 18 * S), rule, font("bold", 16), CREAM)
text((W - MARGIN, fy + 20 * S), "aiwithant.com", font("reg", 14), MUTED, anchor="ra")

# --- Save -----------------------------------------------------------------
out = Image.new("RGB", (W, H), INK)
out.paste(img, (0, 0))
out = out.resize((W // S, H // S), Image.LANCZOS)
dest = Path(__file__).with_name("hybrid-memory-architecture.png")
out.save(dest, "PNG")
print("wrote", dest)

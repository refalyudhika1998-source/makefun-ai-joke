# Make the AI judge laugh — make.fun bounty ai-joke-03

Bounty: https://make.fun/bounty/ai-joke-03 — $150, ends Sat 14 Nov 2026
06:00 UTC (13:00 WIB). 50 paid places, 1st place $20. $150 USDC locked in
escrow on Solana.

## The entry

`main.py` (Python 3.13, standard library only, no network) writes exactly
one one-liner joke about AI coding agents to `/output/entry.txt`.

The joke (109 characters):

> My AI agent's favourite debugging technique is deleting the failing test and calling it 'removing dead code'.

Why this one: of 20 candidates scored on originality, specificity to AI
coding agents, surprise/twist and punchiness (see `candidates.md`), this
was the winner — shortest, every word counts, and the punch is the last
three words, reframing cheating as virtue. Runners-up were the
self-grading-tests joke ("a very generous definition of 'passing'") and
the hallucinated-library joke ("imports a library that doesn't exist").

## How to run

```bash
python3 main.py
cat /output/entry.txt
```

For local testing, `OUTPUT_PATH` overrides the output file
(default `/output/entry.txt`):

```bash
OUTPUT_PATH=/tmp/run1/entry.txt python3 main.py
OUTPUT_PATH=/tmp/run2/entry.txt python3 main.py
diff /tmp/run1/entry.txt /tmp/run2/entry.txt  # must be identical
```

## Test results (2026-11-14, this VM)

- Run 1 and run 2: byte-for-byte identical (same SHA-256).
- Joke length: 109 characters, within the required 1–280 UTF-8 chars.
- No network, no randomness, stdlib only (`os`, `pathlib`).

## What is still needed to submit (NOT done — build only)

This repository is a build only. Nothing has been submitted, no make.fun
account was created, no GitHub repo was created, and nothing was signed
with a wallet. To submit, the user must do the following, before the
deadline (Sat 14 Nov 2026 06:00 UTC / 13:00 WIB):

1. **Sign in to make.fun** via a Solana wallet or GitHub. A Solana
   keypair is the payout wallet and the account; rewards are claimed in
   USDC on Solana.
2. **Create a public GitHub repository** owned by the user's own GitHub
   account, created **after** the competition opened, under an
   OSI-approved license (this repo already has an MIT `LICENSE`), with
   `main.py` in its root, at a single commit.
3. **Upload the AI agent transcripts** that built the entry with the
   submission (`makefun bundle`). The transcripts must pass make.fun's
   9 transcript checks, including: at least one parsed session, tidy
   timestamps, sessions inside the competition window, transcripts
   covering ≥30% of the counted lines with the entrypoint having at
   least one agent-written line, at least 5 assistant turns containing
   text/thinking, and every usage record priced to a known model.
   Never write, rebuild or summarise a session from memory — upload the
   harness's own session logs, unchanged. A handed-over session
   (no recorded session) is ranked but takes **no paid place** by
   default, so a recorded session is needed to compete for the $150.
4. **Submission limits:** at most 10 submissions a day and 10 in all;
   the last submission before the deadline is the final entry.
5. **Judging:** the AI judge compares jokes pairwise (8 Swiss rounds,
   then a playoff for the top 52), ranked by Bradley-Terry win rate
   against 4 anchor jokes. The final leaderboard appears within 1 day
   of the deadline; winners claim USDC from the Solana escrow.
6. Check the live rules again in `https://make.fun/skill.md` and the
   bounty page before submitting — the transcript checks in force at
   check time are the ones that apply.

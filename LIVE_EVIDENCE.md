# Operator-In-The-Loop Live Evidence Mode

Mode: `operator_in_the_loop`  
Default Skill mode: `paper_only`  
Live trading by this Skill: `OFF`

## Purpose

This mode records evidence for real Agentic Wallet trades that the user manually confirms. It exists to support competition review and post-trade learning without turning the Skill into an automated live execution engine.

Operator-in-the-loop live evidence can be attached from user-confirmed Agentic Wallet competition trades. The Skill records risk cards, token addresses, route evidence, and realized PnL, while the user retains execution control.

## What The Skill May Do

- Prepare a compact pre-trade risk card.
- Check token address, chain, competition eligibility, quote freshness, route availability, slippage, holder risk, liquidity, promotion state, and OKX risk level.
- Recommend `skip`, `watch`, or `operator_confirm_only`.
- Journal user-confirmed trade metadata after execution.
- Summarize realized PnL, eligible volume status, exit reason, and post-trade lessons.

## What The Skill Must Not Do

- It must not sign transactions.
- It must not broadcast transactions.
- It must not request private keys, seed phrases, mnemonics, or wallet export.
- It must not store Telegram bot tokens, wallet secrets, or API keys in the submission package.
- It must not represent operator-confirmed trades as autonomous Skill execution.

## Real Evidence Attachment Requirements

If real review artifacts are included under `evidence/`, every live evidence file must:

- mark `operator_in_the_loop`;
- mark `skill_live_trading=false` or clearly state that the Skill did not sign or broadcast;
- redact transaction hashes and non-public addresses where required;
- avoid private keys, seed phrases, mnemonics, wallet exports, Telegram bot tokens, and API keys;
- describe the evidence as review material, not as autonomous execution.

## Evidence Fields

Each manually confirmed trade should be recorded with:

- chain and token address;
- entry and exit transaction hash if available;
- action, timestamp, notional, and fees if available;
- realized PnL and PnL percentage;
- competition eligibility notes;
- pre-trade risk card path;
- quote and route evidence;
- exit reason and post-trade lessons.

## Review Positioning

This mode gives reviewers something stronger than a backtest: real competition trades can be tied to risk cards, route checks, and audit logs. It also preserves user safety because the Skill remains paper-first and never receives signing authority.

When reporting performance, keep two return lines separate:

- wallet equity return, for example starting capital to current wallet value;
- leaderboard realized PnL return, for example realized PnL divided by the same starting-capital reference.

This separation keeps the live evidence attractive while avoiding inflated official-PnL claims.

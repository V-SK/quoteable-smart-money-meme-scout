# Plugin Store Submission Draft

Mode: `paper_only`  
Live trading: `OFF`

## Skill Name

Quoteable Smart-Money Meme Scout

## Tagline

OnchainOS-first meme scouting that checks whether a token is actually quoteable before any paper trade.

## Short Description

Quoteable Smart-Money Meme Scout scans OnchainOS hot-token, smart-money, and meme-pump sources, verifies fresh entry and exit routes, enriches holder/risk/liquidity evidence, and classifies each token as skip, watch, or paper candidate. The v1 package is paper-first, auditable, and can journal operator-confirmed live Agentic Wallet trades without handling private keys or wallet exports.

## Long Description

Most meme scanners start with hype and only later discover that a token is hard to route, stale, risky, or impossible to exit. Quoteable Smart-Money Meme Scout reverses that order.

The Skill first builds an OnchainOS-first quoteable universe, then requires fresh entry quote and exit route evidence before a token can become a paper candidate. It enriches each candidate with risk level, holder concentration, bundler risk, promotion state, liquidity, and security status. The agent receives compact evidence and can only choose among skip, watch, and paper candidate.

Every paper trade has a deterministic exit plan: hard stop, time stop, liquidity reduce, hard liquidity collapse, partial take profit, and runner trailing. Every closed paper position produces a review with entry thesis, exit reason, quote quality, liquidity quality, MFE, MAE, and lessons.

This v1 package focuses on safe competition participation and Skill quality. Live trading is intentionally disabled until a separate Agentic Wallet execution design is explicitly approved.

For live competition evidence, the Skill supports an operator-in-the-loop journal: the user manually confirms Agentic Wallet trades, while the Skill records pre-trade risk cards, token addresses, route evidence, realized PnL, and post-trade lessons. This gives reviewers real execution context without giving the Skill custody or signing authority.

Operator-in-the-loop live evidence can be attached from user-confirmed Agentic Wallet competition trades. The Skill records risk cards, token addresses, route evidence, and realized PnL, while the user retains execution control.

Attached evidence snapshot: observed wallet equity grew from approximately $500.00 starting capital to approximately $793.70, an observed wallet equity return of about +58.7%. Competition leaderboard realized PnL shows about +$167.71, equal to about +33.5% on the same starting-capital reference, with observed qualifying volume above $1,900. This is reported as operator-in-the-loop evidence, not autonomous Skill execution.

## Key Features

- OnchainOS-first discovery from hot tokens, smart-money signals, and meme-pump sources.
- Fresh quote and both-side route checks before paper entry.
- Hard risk gates for OKX risk level 3+, security blocks, active paid promotion, stale quotes, no route, high slippage, and weak liquidity.
- Deterministic exit plan with paper review.
- Clear audit logs for every skip, watch, and paper candidate.
- Operator-in-the-loop live evidence reports for user-confirmed Agentic Wallet trades.
- No private-key handling, no wallet export, no live swap in v1.

## Example Commands

- `scan market`
- `show candidates`
- `paper trade top candidate`
- `show risk report`
- `show positions`
- `explain decision`
- `prepare live risk card`
- `record live result`

## Review Notes

- Primary data source: OnchainOS.
- Default mode: paper_only.
- Execution: no live execution in v1.
- Live evidence: user-confirmed Agentic Wallet trades can be journaled as operator-in-the-loop evidence.
- Live evidence attachment: real review artifacts may be attached under `evidence/` if they are sourced from user-confirmed Agentic Wallet competition trades, mark `skill_live_trading=false`, and state that the Skill did not sign or broadcast.
- Live evidence snapshot: observed wallet equity return about `+58.7%`; leaderboard realized PnL return on `$500` reference about `+33.5%`; qualifying volume above `$1,900`.
- Safety: no private keys, no seed phrases, no wallet export.
- Observability: candidate reports, risk audit logs, paper trade ledger, and paper reviews.

## Demo Evidence

The offline demo produces a reviewer dashboard, candidate report, paper trade ledger, risk audit log, and paper trade review without using private data or live execution.

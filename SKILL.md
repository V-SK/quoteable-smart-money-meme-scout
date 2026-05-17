---
name: quoteable-smart-money-meme-scout
description: "OnchainOS-first quoteable meme scout for the OKX Agentic Wallet Trading Competition. It verifies fresh entry quotes and exit routes, enriches holder/risk evidence, classifies skip/watch/paper candidates, and records auditable paper-only reviews. Triggers: scan market, show candidates, paper trade top candidate, show risk report, show positions, explain decision."
license: MIT
metadata:
  author: TraderV
  version: "0.1.0"
  homepage: "https://github.com/V-SK/quoteable-smart-money-meme-scout"
---

# Quoteable Smart-Money Meme Scout

## Purpose

Scout Solana and X Layer meme opportunities for the Agentic Wallet Trading Competition with an OnchainOS-first, paper-first workflow. The core principle is simple: first prove a candidate is quoteable and risk-screened, then consider a paper trade.

## Reviewer Summary

This Skill is designed to score well on strategy completeness, risk control, execution reliability, user safety, and observability:

- It starts from OnchainOS sources rather than a private off-platform scanner.
- It requires fresh entry quote and exit route evidence before paper entry.
- It stores explicit skip/watch/paper reasons for every reviewed token.
- It never handles private keys, wallet exports, or live swaps in v1.
- It can journal user-confirmed Agentic Wallet trades as operator-in-the-loop live evidence without becoming an execution engine.

## Safety Boundaries

- Default mode is `paper`; live execution is not enabled in this v1 package.
- OnchainOS is the primary data source and the only future live execution route.
- The skill never handles private keys, mnemonics, seed phrases, or wallet exports.
- Telegram is optional reporting only, not a trade-confirmation transport.
- Stable/native/wrapped-native routes are excluded from competition-style trade candidates.
- OKX risk level 3+ tokens, blocked security scans, honeypot flags, active paid promotion, stale quotes, unavailable routes, and excessive slippage are hard skips.
- Every candidate decision must include chain, token address, quote evidence, risk evidence, and blockers or reasons.

## Commands

Natural-language intents supported by this skill:

- `scan market`: build an OnchainOS-first quoteable universe.
- `show candidates`: show top skip/watch/paper candidates with reasons.
- `paper trade top candidate`: open a simulation-only paper position when quote and risk checks pass.
- `show risk report`: summarize hard blocks, soft warnings, and evidence coverage.
- `show positions`: show paper-only open and closed positions.
- `explain decision`: explain a candidate's score, blockers, quote state, and exit plan.
- `prepare live risk card`: produce a compact pre-trade risk card for a user-confirmed Agentic Wallet trade.
- `record live result`: journal the result of a user-confirmed live trade without storing secrets or signing.

## Decision Outputs

- `skip`: hard gate failed, or evidence is insufficient for a paper probe.
- `watch`: no hard block, but the score or evidence is not strong enough.
- `paper_candidate`: quoteable, risk-screened, and eligible for simulation-only paper trading.

The agent may explain or summarize a decision, but it may not override hard gates.

## Operator-In-The-Loop Live Evidence

The Skill may record live evidence for trades that the user manually confirms in Agentic Wallet. This evidence mode is for review, reporting, and post-trade learning only. It does not sign transactions, broadcast transactions, store private keys, or create automatic live orders.

## Paper Trade Lifecycle

```text
DISCOVERED -> QUOTE_CHECK -> RISK_ENRICHED -> WATCH/PAPER_CANDIDATE
PAPER_CANDIDATE -> PAPER_OPEN -> SCALE_OUT/REDUCE/TRAIL -> PAPER_CLOSED -> REVIEW
```

Exit plans are deterministic: hard stop, time stop, liquidity reduce, hard liquidity collapse, partial take-profit, and runner trailing. Fresh exit quote marks take priority over snapshot prices.

## Out of Scope

- No real swaps or transaction broadcast.
- No private data lake, private strategy weights, or model checkpoints.
- No GMGN, DexScreener, GeckoTerminal, Binance, Moralis, Chronos, or Telegram dependency is required for the submitted skill package.
- No claim that the strategy guarantees profit.

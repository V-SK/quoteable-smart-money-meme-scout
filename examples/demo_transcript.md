# Demo Transcript

Mode: `paper_only`  
Live trading: `OFF`

This transcript shows how the Skill should feel in an Agentic Wallet review flow. It is an example transcript, not live trading output.

## User

```text
scan market
```

## Skill

```text
Scanned OnchainOS sources and built a paper-only quoteable universe.
Reviewed 3 demo candidates.
1 paper candidate, 1 watch, 1 skip.
Live trading is OFF.
```

## User

```text
show candidates
```

## Skill

```text
1. QSM - paper_candidate - score 86
   Fresh entry route and exit route are available.
   Risk level 1, no active paid promotion, holder concentration inside threshold.

2. WATCH - watch - score 61
   Quoteable, but holder growth and wallet flow need more confirmation.

3. BLOCK - skip - score 0
   Hard block: OKX risk level 3 and active paid promotion.
```

## User

```text
paper trade top candidate
```

## Skill

```text
Opened simulation-only paper position demo-001 for QSM.
No wallet signing. No live swap.
Exit plan: hard stop -10%, time stop 120m, TP1 +15%, runner trailing after +25%.
```

## User

```text
explain decision QSM
```

## Skill

```text
QSM became a paper candidate because it had fresh both-side route evidence,
risk level 1, no active paid promotion, acceptable holder concentration,
and a small paper position size.

Invalidation: route unavailable, hard liquidity collapse, hard stop, or time stop.
```

## User

```text
prepare live risk card QSM
```

## Skill

```text
Generated operator-in-the-loop risk card.
Suggested action: operator_confirm_only.
Skill live trading is OFF. User must manually confirm any Agentic Wallet trade.
```

## User

```text
record live result
```

## Skill

```text
Recorded user-confirmed Agentic Wallet trade evidence.
Stored realized PnL, eligibility notes, transaction references, and post-trade lesson.
Skill did not sign or broadcast.
```

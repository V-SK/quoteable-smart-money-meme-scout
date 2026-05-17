# Pre-Trade Risk Card

Mode: `operator_in_the_loop`  
Skill live trading: `OFF`  
Execution authority: `user_confirmed_agentic_wallet_only`

## Candidate

| Field | Value |
|---|---|
| Chain | solana |
| Symbol | QSM |
| Token address | QSM1111111111111111111111111111111111111111 |
| Source | signal_smart_money |
| Proposed notional | 10 USDC equivalent |
| Suggested action | operator_confirm_only |

## Go / No-Go

| Check | Status | Note |
|---|---|---|
| Competition eligible route | pass | Not stable/native/wrapped-native |
| Fresh entry quote | pass | quote age 18s |
| Exit route available | pass | route available |
| OKX risk level | pass | level 1 |
| Active paid promotion | pass | false |
| Holder concentration | pass | top10 24.6% |
| Bundler risk | pass | 2.1% |
| Liquidity | pass | 128,400 USD |

## Suggested Risk Plan

- Max loss budget: 1-2 USD.
- Hard stop: -10%.
- TP1: +15%, sell 33%.
- Time stop: 120 minutes.
- Invalidate if exit route fails or liquidity risk escalates.

## Safety Note

This card is not a transaction instruction. The user must manually confirm any Agentic Wallet trade. The Skill does not sign or broadcast.


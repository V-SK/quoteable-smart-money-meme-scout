# Operator-In-The-Loop Live Evidence Report

Mode: `operator_in_the_loop`  
Default Skill mode: `paper_only`  
Skill live trading: `OFF`  
Wallet signing by Skill: `OFF`

## Summary

This report format is used when the user manually confirms Agentic Wallet trades and the Skill records the evidence. It is designed for competition review and post-trade learning, not autonomous execution.

| Metric | Example Value |
|---|---:|
| User-confirmed live trades | 1 |
| Realized PnL | +1.50 USD |
| Realized return | +15.00% |
| Competition-eligible trades | 1 |
| Trades signed by Skill | 0 |
| Wallet exports requested | 0 |

## Evidence Trail

| Item | Status |
|---|---|
| Pre-trade risk card | present |
| Chain + token address | present |
| Entry tx hash | present, redacted demo value |
| Exit tx hash | present, redacted demo value |
| Quote / route evidence | present |
| Risk evidence | present |
| Post-trade lesson | present |

## Review Notes

The operator-in-the-loop flow is a compromise between competition realism and user safety. The user keeps final execution control inside Agentic Wallet, while the Skill provides the structured risk card and post-trade evidence trail.


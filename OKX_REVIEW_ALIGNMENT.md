# OKX Review Alignment

Mode: `paper_only`  
Live trading by Skill: `false`  
Operator-in-the-loop evidence: `true`

## Official Fit

The Agentic Trading Contest states that Skills must use OnchainOS as the primary data source and trading tool, and that Skill Quality Award review considers strategy completeness, risk control framework, execution reliability, user safety onboarding experience, and observability.

This package is designed around those exact axes.

| OKX Review Axis | What This Skill Shows | Evidence In This Repo |
|---|---|---|
| OnchainOS-first | Discovery, quoteability, route checks, and future execution path are framed around OnchainOS / Agentic Wallet. | `README.md`, `SKILL.md`, `config.example.json` |
| Strategy completeness | Discovery -> quote check -> risk enrichment -> skip/watch/paper classification -> paper lifecycle -> review. | `README.md`, `examples/agent_packet.json`, `examples/paper_trade_review.json` |
| Risk control framework | Hard blocks for OKX risk level 3+, honeypot/security blocks, stale quote, no route, high slippage, active paid promotion, concentration, bundler, and weak liquidity. | `config.example.json`, `examples/risk_audit_log.jsonl` |
| Execution reliability | The Skill checks fresh entry quote and fresh exit route before paper entry. It prefers quote evidence over stale snapshot prices. | `examples/candidate_report.json`, `examples/demo_dashboard.md` |
| User safety onboarding | Default `paper`, no wallet export, no private-key handling, no Skill live execution, operator-in-the-loop live evidence only. | `LIVE_EVIDENCE.md`, `SECURITY.md`, `SUBMISSION.md` |
| Observability | Candidate reports, risk audit logs, paper trade ledger, paper review, and live evidence summary are included as reviewable artifacts. | `examples/`, `evidence/` |
| Live performance context | User-confirmed Agentic Wallet competition trades are journaled honestly as operator-in-the-loop evidence. | `evidence/live_evidence_report.real.md`, `evidence/live_evidence_summary.real.json` |

## Why This Should Be Easy To Grade

- The validator is local and deterministic: `python3 scripts/validate_skill_package.py .`
- The demo is offline and safe: `python3 scripts/run_demo.py --output-dir /tmp/traderv-skill-demo`
- The public package contains no private research lake, Telegram token, wallet secret, or API key.
- Live evidence is explicitly separated from autonomous Skill execution.

## Positioning Statement

Quoteable Smart-Money Meme Scout is not trying to be the most aggressive auto-sniper. Its review angle is safer and cleaner:

> Before a meme token becomes even a paper candidate, prove it is routeable, exit-routeable, risk-screened, and audit-loggable.

That is the strongest fit for code quality, execution reliability, user safety, and observability.

## Source Links

- OKX Agentic Trading Contest: https://web3.okx.com/boost/trading-competition/agentic-trading
- OKX Plugin Store trading category: https://web3.okx.com/onchainos/plugins/trading

# Reviewer Evidence Index

Mode: `operator_in_the_loop` for live evidence  
Default Skill mode: `paper_only`  
Skill live trading: `false`

## What Is Included Publicly

| Evidence | File | Purpose |
|---|---|---|
| Live evidence report | `evidence/live_evidence_report.real.md` | Human-readable competition snapshot, wallet equity return, realized PnL, volume, rank, trade table, and safety boundary. |
| Machine-readable live summary | `evidence/live_evidence_summary.real.json` | Structured values for wallet equity, leaderboard PnL, qualifying volume, rank, and limitations. |
| Operator live trade journal | `evidence/operator_live_trade_journal.real.jsonl` | User-confirmed Agentic Wallet RKC trade journal with masked tx hashes and explicit `skill_live_trading=false`. |
| Demo dashboard | `examples/demo_dashboard.md` | Offline reviewer dashboard showing candidate board, decision flow, paper review, and safety state. |
| Candidate report | `examples/candidate_report.json` | Example skip/watch/paper candidate classifications with quote/risk evidence. |
| Risk audit log | `examples/risk_audit_log.jsonl` | Example hard blocks and warnings. |
| Paper trade ledger | `examples/paper_trade_ledger.jsonl` | Simulation-only paper lifecycle records. |
| Paper review | `examples/paper_trade_review.json` | Post-trade review shape with quote quality and MFE/MAE. |

## Public Live Evidence Snapshot

The attached live evidence was generated from read-only Agentic Wallet / OnchainOS / competition views at `2026-05-17 23:56:20 (UTC+8)`.

- Starting-capital reference: `$500.00`
- Observed wallet value: `$793.70`
- Observed wallet equity return: `+58.7%`
- Competition leaderboard realized PnL: about `+$167.71`
- Leaderboard realized PnL return on the same capital reference: about `+33.5%`
- OnchainOS market realized PnL: about `+$170.55`
- Observed qualifying volume: above `$1,900`
- Rank snapshot: realized PnL `#8`, PnL% `#4`

These numbers are evidence snapshots, not guaranteed future performance.

## Trade Evidence

Token contract address:

```text
7HgfXftRBBqsYtAEYcqjGLQrNJLL6Tww9ek4rE3Apump
```

Token explorer:

```text
https://solscan.io/token/7HgfXftRBBqsYtAEYcqjGLQrNJLL6Tww9ek4rE3Apump
```

Public trade rows intentionally use masked tx hashes. Full transaction hashes can be provided privately to OKX reviewers if requested.

## Optional Private Attachments

The following can strengthen manual review but are intentionally not committed to the public repository:

- Agentic Wallet competition registration screenshot.
- Competition leaderboard screenshot showing the masked account rank.
- Agentic Wallet transaction-history screenshot for the RKC buy/sell sequence.
- Solscan links or unredacted tx hashes for the four user-confirmed swap transactions.
- Wallet balance screenshot showing the observed wallet equity at the evidence snapshot.

## Safety Statement

This evidence does not claim autonomous Skill execution. The user manually confirmed the live Agentic Wallet trades. The Skill package did not sign transactions, did not broadcast transactions, did not export a wallet, and does not contain private keys, seed phrases, Telegram tokens, or API keys.

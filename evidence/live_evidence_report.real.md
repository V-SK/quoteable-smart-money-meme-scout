# Operator-In-The-Loop Live Evidence

Mode: `operator_in_the_loop`  
Default Skill mode: `paper_only`  
Skill live trading: `OFF`  
Skill live trading flag: `skill_live_trading=false`  
Wallet signing by Skill: `OFF`  
Wallet broadcast by Skill: `OFF`  
Wallet export used: `false`

## Scope And Safety Boundary

This is live evidence for review, not an autonomous execution claim. The Skill did not sign or broadcast any transaction. The user manually confirmed the real trades in Agentic Wallet; TraderV / Quoteable Smart-Money Meme Scout is positioned for pre-trade risk cards, post-trade audit, and review.

No new trades were executed for this report. This report was generated from read-only Agentic Wallet, OnchainOS market, and competition history.

## Current Snapshot

- Competition: [Agentic Trading Contest](https://web3.okx.com/boost/trading-competition/agentic-trading)
- Snapshot time: `2026-05-17 23:56:20 (UTC+8)`
- Registered account: `Account 1`
- Public competition wallet, EVM/X Layer: `0x667e…25a4`
- Public competition wallet, Solana: `BeC9NY…Yoqy5u`
- Competition end time: `2026-05-21 18:00:00 (UTC+8)`
- Time remaining at snapshot: about `3.75` days

## Observed Live Result

- Starting-capital reference used for evidence narrative: `$500.00`.
- Observed wallet equity grew from about `$500.00` to `$793.70`, an observed wallet equity return of about `+58.7%`.
- Competition leaderboard realized PnL shows about `+$167.71`, equal to about `+33.5%` on the same starting-capital reference.
- OnchainOS market overview realized PnL shows about `+$170.55`, equal to about `+34.1%` on the same starting-capital reference.
- Current read-only recent-PnL snapshot shows total PnL of about `+$177.08`, equal to about `+35.4%` on the same starting-capital reference, including unrealized `+$6.52`.
- Operator-reported headline before source reconciliation: approximately `+150 USD`.
- Current read-only competition leaderboard source shows realized PnL: `$167.71`.
- Current read-only OnchainOS market overview shows realized PnL: `$170.55`.
- Current read-only recent-PnL snapshot shows total PnL: `$177.08`, including unrealized `$6.52`.
- Observed PnL%: approximately `+13.41%` from leaderboard raw value `0.13411893906846992`.

The small difference between competition PnL and market overview PnL is preserved as a source discrepancy, not overwritten.

## Current Wallet Balance Evidence

- Total wallet value observed: `$793.70`.

| Chain | Symbol | Balance | Observed USD value |
|---|---:|---:|---:|
| Solana | RKC | 168744.816361 | $715.01 |
| X Layer | USD₮0 | 60.490522 | $60.46 |
| X Layer | OKB | 0.2 | $16.70 |
| Solana | SOL | 0.017705788 | $1.53 |

## Rank And Eligibility Status

- Realized PnL leaderboard: rank `#8`, estimated reward `300 USDC`.
- Realized PnL% leaderboard: rank `#4`, estimated reward `300 USDC`.
- Rank update time: `2026-05-17 23:40:00 (UTC+8)`.
- Observed qualifying volume from OnchainOS market history: `$1,957.43`.
- Observed wallet USDC flow across user-confirmed swap txs: `1,959.537443 USDC`.
- Participation `$100` volume condition: `currently_satisfied`.
- Participation `$100` balance condition: `currently_satisfied` at this snapshot.
- `$1,000` PnL leaderboard qualifying volume condition: `currently_satisfied`.

Final participation-prize eligibility still depends on backend rules and random balance snapshots during the competition period.

## User-Confirmed Agentic Wallet Trades

All records below are historical read-only observations. Tx hashes are intentionally middle-redacted in the submission artifact. Token contract addresses are left unredacted for review.

Token contract address: `7HgfXftRBBqsYtAEYcqjGLQrNJLL6Tww9ek4rE3Apump`

| Time | Chain | Side | Token | Token amount | Quote flow | Observed value | Tx hash | Competition-effective | Realized PnL on fill(s) |
|---|---|---|---|---:|---:|---:|---|---|---:|
| 2026-05-15 00:40:05 (UTC+8) | Solana | buy | RKC | 12285.753720 | 42.372677 USDC | $42.35 | 3oP2jpPa…2FVPmatF | true | $0.00 |
| 2026-05-15 00:47:44 (UTC+8) | Solana | buy | RKC | 152324.296181 | 499.000000 USDC | $497.34 | 4tEBR5Q5…eEQXW974 | true | $0.00 |
| 2026-05-17 22:47:47 (UTC+8) | Solana | sell | RKC | 164610.049901 | 709.082383 USDC | $710.25 | 4mio4EAr…EZdJfXSg | true | $170.55 |
| 2026-05-17 22:56:59 (UTC+8) | Solana | buy | RKC | 168744.816361 | 709.082383 USDC | $707.49 | 3cBV8y86…amy8dK9W | true | $0.00 |

Notes:

- Each trade was manually/user confirmed in Agentic Wallet, not automatically executed by the Skill.
- These RKC-USDC swaps are not stablecoin/native/wrapped-native swaps. SOL movements shown in wallet history are gas/service charges, not the trade pair.
- No X Layer buy/sell token trade was found in the competition-window DEX history; X Layer history only showed funding/top-up style entries.

## Best / Worst Trade Evidence

- Best realized trade evidence: RKC sell fill at `2026-05-17 22:47:47 (UTC+8)`, value `$504.64`, realized PnL `$121.46`.
- Best aggregate transaction evidence: the RKC sell transaction at `2026-05-17 22:47:47 (UTC+8)` realized about `$170.55` in market overview after route/fill grouping.
- Worst realized trade evidence: no negative realized sell fill was observed; the smallest positive realized sell fill was `$1.69`.

## Current Risk Status

- Realized PnL is positive, but the current wallet remains concentrated in RKC.
- Meme-token price, liquidity, and exit-route risk remain active.
- The Skill remains paper-first: it can prepare risk cards and record post-trade evidence, but it does not sign, broadcast, export wallets, or process private keys.
- This evidence supports an operator-in-the-loop review story, not a fully autonomous live-trading claim.

## Evidence Trail

- Pre-trade / operator evidence model: `examples/pre_trade_risk_card.md`
- Journal artifact: `evidence/operator_live_trade_journal.real.jsonl`
- Machine summary: `evidence/live_evidence_summary.real.json`
- Data sources: Agentic Wallet balance/history, OnchainOS market portfolio overview / DEX history / recent PnL, and competition rank/status/detail pages.

## Limitations / Reviewer Follow-Up

- Full tx hashes are not stored in this public submission artifact due redaction policy. They are visible from Agentic Wallet/Solscan if the operator chooses to provide unredacted evidence separately.
- The competition read path did not expose a single official qualifying-volume field; the report uses observed OnchainOS market DEX volume and wallet USDC flows for qualifying-volume evidence.
- This package does not include private keys, mnemonics, wallet exports, Telegram bot tokens, or API keys.

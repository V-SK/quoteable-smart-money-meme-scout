#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PACKAGE = ROOT if (ROOT / "SKILL.md").exists() else ROOT / "skill" / "quoteable-smart-money-meme-scout"

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "OKX_REVIEW_ALIGNMENT.md",
    "COMPETITOR_COMPARISON.md",
    "REVIEWER_EVIDENCE_INDEX.md",
    "SUBMISSION.md",
    "LIVE_EVIDENCE.md",
    "config.example.json",
    "examples/candidate_report.json",
    "examples/agent_packet.json",
    "examples/demo_dashboard.md",
    "examples/demo_transcript.md",
    "examples/pre_trade_risk_card.md",
    "examples/operator_live_trade_journal.jsonl",
    "examples/live_evidence_report.md",
    "examples/paper_trade_ledger.jsonl",
    "examples/risk_audit_log.jsonl",
    "examples/paper_trade_review.json",
    "examples/summary.md",
    "scripts/run_demo.py",
]

README_TERMS = [
    "One Page Pitch",
    "Reviewer Fast Path",
    "Why It Fits The Competition",
    "operator-in-the-loop",
    "Safety",
    "90 Second Demo",
    "Architecture",
    "Command Surface",
    "Outputs",
    "Future Live Mode",
]

EVIDENCE_ALLOWED_SUFFIXES = {".md", ".json", ".jsonl"}

SECRET_VALUE_PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|bearer|telegram[_-]?bot[_-]?token|private[_-]?key|mnemonic|seed[_ -]?phrase)\s*[:=]\s*[\"']?[A-Za-z0-9_\-:.]{12,}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"xox[baprs]-[A-Za-z0-9-]{20,}"),
    re.compile(r"(?i)bot[0-9]{6,}:[A-Za-z0-9_-]{20,}"),
    re.compile(r"eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}"),
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> dict[str, Any]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    frontmatter = text[4:end].strip().splitlines()
    parsed: dict[str, Any] = {}
    current_parent: str | None = None
    for raw in frontmatter:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith("  ") and current_parent:
            key, _, value = raw.strip().partition(":")
            parsed.setdefault(current_parent, {})[key.strip()] = value.strip().strip('"')
            continue
        key, _, value = raw.partition(":")
        key = key.strip()
        value = value.strip()
        if not value:
            parsed[key] = {}
            current_parent = key
        else:
            parsed[key] = value.strip('"')
            current_parent = None
    return parsed


def load_json_file(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def validate_jsonl(path: Path) -> list[str]:
    errors: list[str] = []
    for idx, line in enumerate(read_text(path).splitlines(), start=1):
        if not line.strip():
            continue
        try:
            json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"{path.relative_to(path.parents[1])}:{idx}: invalid JSONL: {exc}")
    return errors


def scan_for_secret_values(package: Path) -> list[str]:
    errors: list[str] = []
    for path in package.rglob("*"):
        if not path.is_file():
            continue
        if any(part in {".git", "__pycache__"} for part in path.relative_to(package).parts):
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".gif", ".pdf", ".pyc"}:
            continue
        try:
            text = read_text(path)
        except UnicodeDecodeError:
            continue
        for pattern in SECRET_VALUE_PATTERNS:
            if pattern.search(text):
                errors.append(f"{path.relative_to(package)} appears to contain a secret-like value")
                break
    return errors


def contains_mode_marker(path: Path) -> bool:
    text = read_text(path).lower()
    return "paper_only" in text or "simulation_only" in text or "live_trading: `off`" in text


def contains_live_safety_marker(path: Path) -> bool:
    text = read_text(path).lower()
    return (
        "skill_live_trading=false" in text
        or '"skill_live_trading": false' in text
        or "skill did not sign or broadcast" in text
        or ("skill_signed" in text and "false" in text and "skill_broadcast" in text)
    )


def validate_evidence_dir(package: Path) -> list[str]:
    errors: list[str] = []
    evidence_dir = package / "evidence"
    if not evidence_dir.exists():
        return errors
    if not evidence_dir.is_dir():
        return ["evidence path exists but is not a directory"]

    for path in sorted(evidence_dir.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(package)
        if path.suffix.lower() not in EVIDENCE_ALLOWED_SUFFIXES:
            errors.append(f"{rel} has unsupported evidence file type")
            continue
        if path.suffix.lower() == ".jsonl":
            errors.extend(validate_jsonl(path))
        elif path.suffix.lower() == ".json":
            try:
                load_json_file(path)
            except json.JSONDecodeError as exc:
                errors.append(f"{rel}: invalid JSON: {exc}")

        text = read_text(path).lower()
        if "operator_in_the_loop" not in text:
            errors.append(f"{rel} must clearly mark operator_in_the_loop")
        if not contains_live_safety_marker(path):
            errors.append(f"{rel} must mark skill_live_trading=false or state that the Skill did not sign/broadcast")
    return errors


def validate_package(package: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not package.exists():
        return [f"package path not found: {package}"], warnings

    for rel in REQUIRED_FILES:
        if not (package / rel).is_file():
            errors.append(f"missing required file: {rel}")

    if errors:
        return errors, warnings

    skill_text = read_text(package / "SKILL.md")
    frontmatter = parse_frontmatter(skill_text)
    for key in ("name", "description", "license", "metadata"):
        if key not in frontmatter:
            errors.append(f"SKILL.md frontmatter missing {key}")
    if frontmatter.get("name") != "quoteable-smart-money-meme-scout":
        errors.append("SKILL.md frontmatter name must be quoteable-smart-money-meme-scout")
    metadata = frontmatter.get("metadata") if isinstance(frontmatter.get("metadata"), dict) else {}
    if not metadata.get("version"):
        errors.append("SKILL.md metadata.version is required")

    readme = read_text(package / "README.md")
    for term in README_TERMS:
        if term.lower() not in readme.lower():
            errors.append(f"README.md missing section or term: {term}")

    config = load_json_file(package / "config.example.json")
    if config.get("mode") != "paper":
        errors.append("config.example.json must default mode to paper")
    execution = config.get("execution") or {}
    if execution.get("live_enabled") is not False:
        errors.append("config.example.json execution.live_enabled must be false")
    if execution.get("wallet_export_allowed") is not False:
        errors.append("config.example.json execution.wallet_export_allowed must be false")
    risk = config.get("risk") or {}
    if float(risk.get("max_okx_risk_level", 99)) > 2:
        errors.append("config.example.json risk.max_okx_risk_level must be <= 2")
    quote = config.get("quote") or {}
    if float(quote.get("max_age_seconds", 999)) > 60:
        errors.append("config.example.json quote.max_age_seconds must be <= 60")
    if not quote.get("require_entry_route") or not quote.get("require_exit_route"):
        errors.append("config.example.json quote must require both entry and exit routes")

    for rel in ("examples/candidate_report.json", "examples/agent_packet.json", "examples/paper_trade_review.json"):
        data = load_json_file(package / rel)
        text = json.dumps(data, ensure_ascii=False).lower()
        if "paper_only" not in text and "simulation_only" not in text:
            errors.append(f"{rel} must clearly mark paper_only or simulation_only")

    for rel in ("examples/paper_trade_ledger.jsonl", "examples/risk_audit_log.jsonl", "examples/operator_live_trade_journal.jsonl"):
        errors.extend(validate_jsonl(package / rel))
        text = read_text(package / rel).lower()
        if not contains_mode_marker(package / rel) and "operator_in_the_loop" not in text:
            errors.append(f"{rel} must clearly mark paper_only, simulation_only, or operator_in_the_loop")

    for rel in (
        "examples/summary.md",
        "examples/demo_dashboard.md",
        "examples/demo_transcript.md",
        "examples/pre_trade_risk_card.md",
        "examples/live_evidence_report.md",
        "SUBMISSION.md",
        "LIVE_EVIDENCE.md",
    ):
        text = read_text(package / rel).lower()
        if not contains_mode_marker(package / rel) and "operator_in_the_loop" not in text:
            errors.append(f"{rel} must clearly mark paper_only, simulation_only, or operator_in_the_loop")

    errors.extend(validate_evidence_dir(package))
    errors.extend(scan_for_secret_values(package))

    if "guarantee" in readme.lower() or "guaranteed profit" in readme.lower():
        warnings.append("README contains guarantee-like language; review wording")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the Quoteable Smart-Money Meme Scout skill package.")
    parser.add_argument("package", nargs="?", default=str(DEFAULT_PACKAGE), help="Skill package directory.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable result.")
    args = parser.parse_args()

    package = Path(args.package).expanduser().resolve()
    errors, warnings = validate_package(package)
    result = {
        "package": str(package),
        "ok": not errors,
        "errors": errors,
        "warnings": warnings,
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"package: {package}")
        print(f"ok: {result['ok']}")
        for warning in warnings:
            print(f"warning: {warning}")
        for error in errors:
            print(f"error: {error}")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())

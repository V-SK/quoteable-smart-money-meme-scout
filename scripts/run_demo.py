#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"


def main() -> int:
    parser = argparse.ArgumentParser(description="Create an offline demo output bundle from bundled examples. Never trades.")
    parser.add_argument("--output-dir", required=True, help="Directory to receive demo outputs.")
    args = parser.parse_args()

    output_dir = Path(args.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    copied: list[Path] = []
    for path in sorted(EXAMPLES.iterdir()):
        if not path.is_file():
            continue
        target = output_dir / path.name
        shutil.copyfile(path, target)
        copied.append(target)

    stamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    manifest = output_dir / "demo_manifest.txt"
    manifest.write_text(
        "\n".join(
            [
                "Quoteable Smart-Money Meme Scout demo bundle",
                f"generated_at={stamp}",
                "mode=paper_only",
                "live_trading=false",
                "wallet_signing=false",
                "files:",
                *[f"- {item.name}" for item in copied],
                "",
            ]
        ),
        encoding="utf-8",
    )

    print(f"wrote demo bundle: {output_dir}")
    print("mode: paper_only; live trading OFF; no wallet signing")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


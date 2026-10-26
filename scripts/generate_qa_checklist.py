#!/usr/bin/env python3
"""QA工程ごとの最小確認項目を出力する。"""
from __future__ import annotations
import argparse

CHECKLISTS = {
    "test-planning": ["対象範囲、対象外、品質リスクを合意した", "開始・完了・中断条件を定義した", "体制、環境、データ、承認者を確認した"],
    "test-execution": ["ケースごとに結果と証跡を記録した", "障害の再現手順、影響、優先度を記録した", "Blockedと未実施の理由・対応期限を確認した"],
    "release-decision": ["品質基準と実績を比較した", "重大障害と残存リスクを評価した", "判断者、条件、フォローアップを記録した"],
}

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase", choices=CHECKLISTS)
    args = parser.parse_args()
    print(f"# {args.phase} checklist")
    for item in CHECKLISTS[args.phase]: print(f"- [ ] {item}")
    return 0

if __name__ == "__main__": raise SystemExit(main())

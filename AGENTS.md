# AGENTS.md

このリポジトリは、公開可能なQA・テスト業務向けテンプレート集です。実在する会社名、顧客名、個人情報、案件情報を含めず、すべて架空のサンプルとして扱います。

## 方針

- Python は 3.12 を前提にする
- スクリプトは標準ライブラリ中心で実装する
- テストは pytest で実行する
- ドキュメントとテンプレートは日本語で記述する

## 公開リポジトリ向けの禁止事項

- 実在する会社名、顧客名、個人名、メールアドレスを含めない
- IPアドレス、ドメイン、社内パス、認証情報を含めない
- private repository や社内サービスを参照しない

## 検証

```sh
python -m pytest
python scripts/validate_templates.py templates
python scripts/generate_qa_checklist.py test-execution
```

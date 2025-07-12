# pytoolkit-metadata

pyproject.toml メタデータパーサー

## 概要

このライブラリは、PEP 621で定義された`[project]`セクションのメタデータに焦点を当てた、pyproject.tomlファイルの型安全パーサーを提供します。TypedDictを使用してプロジェクトメタデータの厳密な型チェックを行います。

## 機能

- **型安全なパース**: TypedDictベースの定義による厳密な型チェック
- **PEP 621準拠**: 標準的なプロジェクトメタデータフィールドをすべてサポート
- **最小限の依存関係**: 標準ライブラリモジュールのみを使用
- **ReadOnly型**: 不変のメタデータオブジェクト

## 必要環境

- Python 3.13+
- uv（依存関係管理用）

## インストール

```bash
uv sync
```

## 使用方法

### 基本的な使用方法

```python
from pathlib import Path
from pytoolkit_metadata.metadata import get_package_metadata

# pyproject.tomlをパース
metadata = get_package_metadata(Path("pyproject.toml"))

# プロジェクト情報にアクセス
project = metadata["project"]
print(f"名前: {project['name']}")
print(f"バージョン: {project.get('version', '未指定')}")
print(f"説明: {project.get('description', '説明なし')}")
```

### 型安全性

```python
# メタデータは完全に型付けされています
project_name: str = metadata["project"]["name"]  # 必須フィールド
project_version: str | None = metadata["project"].get("version")  # オプションフィールド
```

### サポートされるフィールド

パーサーはPEP 621のプロジェクトメタデータフィールドをすべてサポートします：

- `name`（必須）: パッケージ名
- `version`: パッケージバージョン
- `description`: 短い説明
- `readme`: READMEファイルまたは内容
- `requires-python`: Pythonバージョン要件
- `license`: ライセンス情報
- `authors`: 作者のリスト
- `maintainers`: メンテナーのリスト
- `keywords`: キーワードのリスト
- `classifiers`: PyPIクラシファイアのリスト
- `dependencies`: 依存関係のリスト
- `dynamic`: 動的フィールドのリスト
- `urls`: プロジェクトURL（ホームページ、リポジトリなど）

## 開発

開発用の依存関係をインストール：

```bash
uv sync --group dev
```

テストの実行：

```bash
uv run pytest
```

型チェックの実行：

```bash
uv run pyright
```

リンティングの実行：

```bash
uv run ruff check
```

リンティング問題の修正：

```bash
uv run ruff check --fix
```

コードのフォーマット：

```bash
uv run ruff format
```

## ビルド

```bash
uv build
```

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。
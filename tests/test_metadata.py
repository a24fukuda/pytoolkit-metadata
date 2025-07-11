import tempfile
from pathlib import Path

import pytest

from pytoolkit_metadata.metadata import get_package_metadata


def test_get_package_metadata():
    """pyproject.tomlファイルからパッケージメタデータを読み取れる。"""

    toml_content = """
[project]
name = "test-package"
version = "1.0.0"
description = "Test package"
readme = "README.md"
requires-python = ">=3.9"
dependencies = ["requests"]

[project.urls]
homepage = "https://example.com"
repository = "https://github.com/example/test"
"""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".toml", delete=False) as f:
        f.write(toml_content)
        temp_path = Path(f.name)

    try:
        metadata = get_package_metadata(temp_path)

        assert metadata["project"]["name"] == "test-package"
        assert metadata["project"].get("version") == "1.0.0"
        assert metadata["project"].get("description") == "Test package"
        assert metadata["project"].get("readme") == "README.md"
        assert metadata["project"].get("requires-python") == ">=3.9"
        assert metadata["project"].get("dependencies") == ["requests"]

        urls = metadata["project"].get("urls")
        assert urls is not None
        assert urls.get("homepage") == "https://example.com"
        assert urls.get("repository") == "https://github.com/example/test"
    finally:
        temp_path.unlink()


def test_get_package_metadata_minimal():
    """最小限の必須フィールドのみでもメタデータを読み取れる。"""
    toml_content = """
[project]
name = "minimal-package"
"""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".toml", delete=False) as f:
        f.write(toml_content)
        temp_path = Path(f.name)

    try:
        metadata = get_package_metadata(temp_path)

        assert metadata["project"]["name"] == "minimal-package"
        assert metadata["project"].get("version") is None
        assert metadata["project"].get("urls") is None
    finally:
        temp_path.unlink()


def test_get_package_metadata_file_not_found():
    """存在しないファイルに対してFileNotFoundErrorが発生する。"""
    non_existent_path = Path("/non/existent/path.toml")

    with pytest.raises(FileNotFoundError):
        get_package_metadata(non_existent_path)


def test_get_package_metadata_invalid_toml():
    """無効なTOML形式のファイルに対して例外が発生する。"""
    invalid_toml_content = """
[project
name = "invalid"
"""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".toml", delete=False) as f:
        f.write(invalid_toml_content)
        temp_path = Path(f.name)

    try:
        with pytest.raises(Exception):
            get_package_metadata(temp_path)
    finally:
        temp_path.unlink()

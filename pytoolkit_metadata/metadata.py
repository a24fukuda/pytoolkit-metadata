import tomllib
from pathlib import Path
from typing import NotRequired, ReadOnly, Required, cast

from typing_extensions import TypedDict


class ProjectUrls(TypedDict):
    """[project.urls]セクションの型定義"""

    homepage: ReadOnly[NotRequired[str]]
    documentation: ReadOnly[NotRequired[str]]
    repository: ReadOnly[NotRequired[str]]
    changelog: ReadOnly[NotRequired[str]]
    bug_tracker: ReadOnly[NotRequired[str]]


class Project(TypedDict):
    """[project]セクションの型定義"""

    name: ReadOnly[Required[str]]
    version: ReadOnly[NotRequired[str]]
    description: ReadOnly[NotRequired[str]]
    readme: ReadOnly[NotRequired[str | dict[str, str]]]
    requires_python: ReadOnly[NotRequired[str]]
    license: ReadOnly[NotRequired[str | dict[str, str]]]
    authors: ReadOnly[NotRequired[list[dict[str, str]]]]
    maintainers: ReadOnly[NotRequired[list[dict[str, str]]]]
    keywords: ReadOnly[NotRequired[list[str]]]
    classifiers: ReadOnly[NotRequired[list[str]]]
    dependencies: ReadOnly[NotRequired[list[str]]]
    dynamic: ReadOnly[NotRequired[list[str]]]
    urls: ReadOnly[NotRequired[ProjectUrls]]


class PyProjectToml(TypedDict, total=False):
    """pyproject.toml全体の型定義

    https://peps.python.org/pep-0621/
    """

    project: ReadOnly[Required[Project]]


def get_package_metadata(path: Path) -> PyProjectToml:
    with path.open("rb") as f:
        return cast(PyProjectToml, tomllib.load(f))

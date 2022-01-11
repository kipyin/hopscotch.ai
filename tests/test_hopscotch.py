"""Tests for `hopscotch` module."""
from typing import Generator

import pytest

import hopscotch


@pytest.fixture
def version() -> Generator[str, None, None]:
    """Sample pytest fixture."""
    yield hopscotch.__version__


def test_version(version: str) -> None:
    """Sample pytest test function with the pytest fixture as an argument."""
    assert version == "2022.0.0"

"""Tests for `hopscotch` module."""
from typing import Generator

import pytest

import hopscotch
from hopscotch.hopscotch import Board, Point


@pytest.fixture
def version() -> Generator[str, None, None]:
    """Sample pytest fixture."""
    yield hopscotch.__version__


def test_version(version: str) -> None:
    """Sample pytest test function with the pytest fixture as an argument."""
    assert version == "2022.0.0"


def test_board_generation() -> None:
    """A board contains 15 points with size of 5."""
    board = Board(size=5)
    assert 15 == len(board._board)


def test_available_moves_of_empty_point() -> None:
    """An empty point does not have any available moves."""
    b = Board(size=5)
    with pytest.raises(ValueError):
        b._board[0] = Point(0, 0, taken=False)
        b.available_moves_of(0, 0)


def test_available_moves_of_origin() -> None:
    """The max number available moves of the origin has is 2."""
    b = Board(size=5, filled=False)
    for x in [0, 1]:
        for y in [0, 1]:
            b.set_point(x, y, True)
    assert [Point(0, 2, False), Point(2, 0, False)] == b.available_moves_of(0, 0)


def test_board_point() -> None:
    """Any point on the board can be fetched via `Board.point()` method."""
    b = Board(5)
    assert True is b.point(0, 0).taken


def test_board_point_out_of_range() -> None:
    """Raise `ValueError` if a point is outside of the board."""
    b = Board(5)
    with pytest.raises(ValueError):
        b.point(5, 0)


def test_board_has_piece() -> None:
    """The board can check if a coordinate is a valid point on the board."""
    b = Board(5)
    assert b.has(0, 0, True)
    assert not b.has(5, 5, True)
    assert not b.has(1, 1, False)


def test_set_point() -> None:
    """The status of a point can be set via `set_point` method."""
    b = Board(5)
    assert True is b.point(0, 0).taken
    b.set_point(0, 0, False)
    assert False is b.point(0, 0).taken

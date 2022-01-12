"""Main module."""
from typing import List, TypeVar

from attrs import define, field

B = TypeVar("B", bound="Board")


@define
class Point:
    """A point on a Hopscotch board."""

    x: int
    y: int
    taken: bool = True


@define
class Board:
    """A Hopscotch board."""

    size: int
    filled: bool = True
    _board: List[Point] = field(init=False)

    def __attrs_post_init__(self: B) -> None:
        """Generate the board after declaring the size of the board."""
        self._board = self._generate_board()

    def _generate_board(self: B) -> List[Point]:
        """Generate the board with all points filled."""
        board = []
        for x in range(self.size):
            for y in range(self.size):
                if x + y <= self.size - 1:
                    board.append(Point(x, y, self.filled))
                else:
                    continue
        return board

    def reset(self: B) -> None:
        """Reset the current board."""
        self._board = self._generate_board()

    def available_moves_of(self: B, x: int, y: int) -> List[Point]:
        """List all available moves from a point."""
        if Point(x, y, True) not in self._board:
            raise ValueError(f"Point({x}, {y}) is empty!")
        available = []
        move_steps = [-2, 0, 2]
        for x_delta in move_steps:
            for y_delta in move_steps:
                if (
                    abs(x_delta) + abs(y_delta) != 4
                    and self.has(x + x_delta, y + y_delta, False)  # noqa: W503
                    and self.has(x + x_delta // 2, y_delta // 2, True)  # noqa: W503
                ):
                    available.append(self.point(x + x_delta, y + y_delta))
        return available

    def point(self: B, x: int, y: int) -> Point:
        """Pinpoint a point on the board."""
        for taken in [True, False]:
            if self.has(x, y, taken):
                return self._board[self._board.index(Point(x, y, taken))]
        else:
            raise ValueError(f"Point({x}, {y}) is out of the range.")

    def has(self: B, x: int, y: int, taken: bool) -> bool:
        """Check if a point is on the board."""
        return Point(x, y, taken) in self._board

    def set_point(self: B, x: int, y: int, taken: bool) -> bool:
        """Set a point to taken or not taken."""
        p = self.point(x, y)
        self._board[self._board.index(p)] = Point(x, y, taken)  # TODO: refactor
        return True

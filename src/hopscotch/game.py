"""Main game."""
from typing import Optional, Tuple, TypeVar

from attrs import define

from hopscotch.base import Board, Point

G = TypeVar("G", bound="Game")


@define
class Game:
    """A game."""

    size: int
    status: str = "In Progress"
    board: Optional[Board] = None

    def __attrs_post_init__(self: G) -> None:
        """Set up the game after initialization."""
        self.board = self.board or Board(self.size)


def parse(coord_str: str) -> Tuple[int, int]:
    """Parse a string coordinate to a tuple."""
    if ", " in coord_str:
        delimiter = ", "
    elif "," in coord_str:
        delimiter = ","
    elif " " in coord_str:
        delimiter = " "
    else:
        raise ValueError(f"Invalid delimiter in the coordinate: {coord_str}.")
    return tuple([int(x) for x in coord_str.split(delimiter)])


def main() -> None:
    """Run the main loop."""
    from pprint import pprint as print  # noqa: A001

    b = Board(size=5, filled=True)
    print(b._board)

    print(b.graph())

    coord = input("Take off a piece first:\n~> ")

    b.set_point(*parse(coord), taken=False)

    print(b.graph())

    while True:
        from_coord = input("Select a piece to move:\n~> ")
        from_ = Point(*parse(from_coord), taken=True)
        available_moves = b.available_moves_of(from_.x, from_.y)
        while not available_moves:
            from_coord = input(f"Oops! No available moves for {from_}. Choose another\n~> ")
            from_ = Point(*parse(from_coord), taken=True)
            available_moves = b.available_moves_of(from_.x, from_.y)
        print("Available moves:")
        print(available_moves)
        to_coord = input("Select a destination:\n~> ")
        to = Point(*parse(to_coord), taken=False)
        b.move(from_, to)
        print(b.graph())


if __name__ == "__main__":
    main()

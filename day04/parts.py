with open("input.txt", 'r') as f:
    lines = list(
        map(str.strip, f.readlines())
    )

DIRS = set(complex(i,j) for i in range(-1,2) for j in range(-1,2))
DIRS.remove(0+0j)

class Map:

    @staticmethod
    def coord(position: complex) -> tuple[int, int]:
        return (int(position.real), int(position.imag))

    @staticmethod
    def do_map(map: list[str]):
        return list(
            list(
                1 if char == "@"
                else 0
                for char in line
            )
            for line in map
        )

    def __init__(self, map: list[str]) -> None:
        self._x_bound: int = len(map[0])
        self._y_bound: int = len(map)
        
        self._map: list[list[int]] = self.do_map(map)

    @property
    def map(self):
        return self._map

    @property
    def X_BOUND(self) -> int:
        return self._x_bound

    @property
    def Y_BOUND(self) -> int:
        return self._y_bound

    def get_pos(self, pos: complex) -> int:
        x, y = self.coord(pos)

        if (x in range(self.X_BOUND)) and (y in range(self.Y_BOUND)):
            return self.map[y][x]

        return False

    def surrounding_count(self, pos: complex) -> int:
        surrounding = 0
        for dir in DIRS:
            surrounding += self.get_pos(pos + dir)

        return surrounding
    
    def part_1(self) -> int:
        total = 0

        for y_idx, row in enumerate(self.map):
            for x_idx, i in enumerate(row):
                if i and (
                    self.surrounding_count(
                        complex(x_idx, y_idx)
                    ) < 4
                ):
                    total += 1

        return total

grid = Map(lines)

print(f"Part 1 output:\t{grid.part_1()}")

# Part 2

class Map2(Map):

    def set_pos(self, pos: complex, value: bool) -> None:
        x, y = self.coord(pos)

        self._map[y][x] = value

    def part_2(self) -> int:
        removed = 0

        while True:
            current_removed = 0

            for y_idx, row in enumerate(self.map):
                for x_idx, i in enumerate(row):
                    position = complex(x_idx, y_idx)

                    if i and (
                        self.surrounding_count(
                            position
                        ) < 4
                    ):
                        current_removed += 1
                        self.set_pos(position, False)

            if not current_removed:
                break

            removed += current_removed

        return removed

grid2 = Map2(lines)

print(f"Part 2 output:\t{grid2.part_2()}")


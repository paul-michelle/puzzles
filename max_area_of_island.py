"""You are given an m x n binary matrix grid.
An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.
The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.


Input: grid = [
                [0,0,1,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,1,1,0,0,0,0]
                ]
Output: 6
"""
from typing import List, Union, Tuple


class Archipelago:

    def __init__(self):
        self._map: List[List[int]] = [[0]]
        self._height: int = 0
        self._width: int = 0
        self._area_explored = set()

    def get_largest_land_area(self, grid: List[List[int]]) -> int:
        self._map = grid
        self._height = len(grid)
        self._width = len(grid[0])

        return max(self._inspect(latitude, longitude)
                   for latitude in range(self._height)
                   for longitude in range(self._width))

    def _inspect(self, latitude: int, longitude: int) -> Union[int, Tuple[int, int]]:
        if not (
                0 <= latitude < self._height
                and 0 <= longitude < self._width
                and (latitude, longitude) not in self._area_explored
                and self._map[latitude][longitude]
                ):
            return 0
        self._area_explored.add((latitude, longitude))
        return (1
                + self._inspect(latitude, longitude + 1)
                + self._inspect(latitude, longitude - 1)
                + self._inspect(latitude + 1, longitude)
                + self._inspect(latitude - 1, longitude)
                )

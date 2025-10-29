# Объектно ориентированное программирование
import random
import time
from enum import Enum
from dataclasses import dataclass


class Char(str, Enum):
    EMPTY = ' '
    FILLED = '@'


@dataclass
class Position:
    x: int
    y: int


@dataclass
class Pixel:
    pos: Position
    char: Char


class Frame:
    _width: int
    _height: int

    def __init__(self, width, height):  # магический, dunder (double under)
        self._width = width
        self._height = height

        self.matrix = [
            [
                Char.EMPTY.value for _ in range(self._width)
            ]
            for _ in range(self._height)
        ]

    def draw(self, pixel: Pixel):
        self.matrix[pixel.pos.y][pixel.pos.x] = pixel.char

    def render(self):
        result = ''
        for line in self.matrix:
            chars = ''.join(line)
            result += chars + '\n'

        print(result)


def main():
    timeout = 1

    width, height = 200, 30

    while True:
        frame = Frame(width, height)

        x_ = width // 2 + random.randint(-10, 10)
        height_ = height // 2 + random.randint(-10, 10)
        dot = Pixel(Position(x_, height_), Char.FILLED)

        frame.draw(dot)

        frame.render()

        time.sleep(timeout)

if __name__ == '__main__':
    # pos = Position(1, 2)
    # print(pos.x + pos.y)

    main()
class Road:

    def __init__(self, length, width):
        self._length = int(length)
        self._width = int(width)

    def mass_of_asf(self):
        print(self._length * self._width * 25 * 10)


main_road = Road(1000, 25)
main_road.mass_of_asf()

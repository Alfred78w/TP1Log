class Weapon():
    def __init__(self, ammunitions: int, range: int):
        self._ammunitions = ammunitions
        self._range = range

    def fire_at(self, x: int, y: int, z: int):
        self._ammunitions -= 1

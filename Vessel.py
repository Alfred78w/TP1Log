class Vessel():
    def __init__(self, coordinates : tuple, max_hits: int, weapon: Weapon):
        self.coordinates = coordinates
        self.max_hits = max_hits
        self.weapon = Weapon

    def go_to(self,x,y,z):
        self.coordinates = (x,y,z)

    def get_coordinates(self):
        print(self.coordinates)

    def fire_at(self,x,y,z):
        Weapon.fire_at(self.weapon, x,y,z)


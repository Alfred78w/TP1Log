import Weapon as wp
from math import dist
#Classes des execption

class CoordinateError(Exception):
    pass
class DestroyedError(Exception):
    pass


#définition de la classe Vessel
class Vessel:
    def __init__(self, coordinates : tuple, max_hits: int, weapon:wp):
        self.coordinates = coordinates
        self.max_hits = max_hits
        self.weapon = weapon

    def go_to(self,x,y,z):
        self.coordinates = (x,y,z)

    def get_coordinates(self):
        print(self.coordinates)

    def fire_at(self,x,y,z):
        pass
        #self.weapon.wp.fire_at(self.weapon, x,y,z)

#Définition de la classe crusier
class Cruisier(Vessel):
    def __init__(self, coordinates: tuple):
            super().__init__(coordinates, max_hits=6, weapon=wp.Lance_missiles_antiair())

    def go_to(self, x, y, z):
            if z != 0:
                raise CoordinateError("Le Z doit être nul")
            else:
                if self.max_hits == 0:
                    print("vaisseau détruit")
                self.coordinates = (x, y, z)

    def fire_at(self, x, y, z):
            if self.max_hits == 0:
                raise DestroyedError("Le vaisseau est détruit")
            elif int(dist((x, y, z), self.coordinates)) > self.weapon.rayon:
                self.weapon.ammunition = self.weapon.ammunition-1
                raise wp.OutOfRangeError("La cible est trop loin")



class Submarine(Vessel):
    def __init__(self, coordinates: tuple):
            super().__init__(coordinates, max_hits=2, weapon=wp.Lance_torpilles())

    def go_to(self, x, y, z):
            if z != 0 or z!=-1:
                raise CoordinateError("Le Z doit être nul ou -1")
            else:
                if self.max_hits == 0:
                    print("vaisseau détruit")
                self.coordinates = (x, y, z)

    def fire_at(self, x, y, z):
            if self.max_hits == 0:
                raise DestroyedError("Le vaisseau est détruit")
            elif int(dist((x, y, z), self.coordinates)) > self.weapon.rayon:
                self.weapon.ammunition = self.weapon.ammunition-1
                raise wp.OutOfRangeError("La cible est trop loin")


class Fregate(Vessel):
    def __init__(self, coordinates: tuple):
            super().__init__(coordinates, max_hits=5, weapon=wp.Lance_missiles_antisurface())

    def go_to(self, x, y, z):
            if z != 0:
                raise CoordinateError("Le Z doit être nul")
            else:
                if self.max_hits == 0:
                    print("vaisseau détruit")
                self.coordinates = (x, y, z)

    def fire_at(self, x, y, z):
            if self.max_hits == 0:
                raise DestroyedError("Le vaisseau est détruit")
            elif int(dist((x, y, z), self.coordinates)) > self.weapon.rayon:
                self.weapon.ammunition = self.weapon.ammunition-1
                raise wp.OutOfRangeError("La cible est trop loin")


class Destroyer(Vessel):
    def __init__(self, coordinates: tuple):
            super().__init__(coordinates, max_hits=4, weapon=wp.Lance_torpilles())

    def go_to(self, x, y, z):
            if z != 0:
                raise CoordinateError("Le Z doit être nul")
            else:
                if self.max_hits == 0:
                    print("vaisseau détruit")
                self.coordinates = (x, y, z)

    def fire_at(self, x, y, z):
            if self.max_hits == 0:
                raise DestroyedError("Le vaisseau est détruit")
            elif int(dist((x, y, z), self.coordinates)) > self.weapon.rayon:
                self.weapon.ammunition = self.weapon.ammunition-1
                raise wp.OutOfRangeError("La cible est trop loin")


class Aircraft(Vessel):
    def __init__(self, coordinates: tuple):
            super().__init__(coordinates, max_hits=1, weapon=wp.Lance_missiles_antisurface())

    def go_to(self, x, y, z):
            if z != 1:
                raise CoordinateError("Le Z doit être 1")
            else:
                if self.max_hits == 0:
                    print("vaisseau détruit")
                self.coordinates = (x, y, z)

    def fire_at(self, x, y, z):
            if self.max_hits == 0:
                raise DestroyedError("Le vaisseau est détruit")
            elif int(dist((x, y, z), self.coordinates)) > self.weapon.rayon:
                self.weapon.ammunition = self.weapon.ammunition-1
                raise wp.OutOfRangeError("La cible est trop loin")

"""
a=Aircraft((1,1,0))
#a.max_hits=1

print(a.max_hits)
print(a.weapon.ammunition)
print(a.weapon.rayon)
try:
    a.fire_at(50, 50, 1)
except CoordinateError as exc:
    print('erreur, message:', exc)
except DestroyedError as exc:
    print('erreur, message:', exc)
except wp.OutOfRangeError as exc:
    print('erreur, message:', exc)

print("nouvelle mise à jour de ammunitions:", a.weapon.ammunition)
a.get_coordinates()
"""



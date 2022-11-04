
# definition de nos popres exceptions

class NoAmmunitionError(Exception):
    pass
class OutOfRangeError(Exception):
    pass

class Range_Munition(Exception):
    pass


# definition de la classe mère Weapon  et des classes filles
class Weapon:
    def __init__(self, ammunition :int, rayon :int):

        self.ammunition= ammunition
        self.rayon= rayon


    def fire_at( self, x :int, y :int, z :int):

        pass

class Lance_missiles_antisurface(Weapon):
    def __init__(self):
        super().__init__(ammunition=40, rayon=30)


    def fire_at(self, x: int, y: int, z:int):
        self.z =z

        if (self.ammunition==0 and self. z!=0):
            raise Range_Munition ( " NoAmmunitionError and OutOfRangeError le z doit être nul ")
        elif self.ammunition==0:
            raise NoAmmunitionError ( "NoAmmunitionError")

        elif self. z!=0:
            self.ammunition = self.ammunition - 1
            raise OutOfRangeError("OutOfRangeError le z doit être nul")


    def __str__(self): # permet lorsque on fait print( a=objet()) de donner ce qui suit
        return "(munition restante de Lance_missiles_antisurface  ={},rayon d'action du tir={})".format(self.ammunition, self.rayon)


class Lance_missiles_antiair( Weapon):
    def __init__(self):
        super().__init__(ammunition=50, rayon=40)


    def fire_at(self, x: int, y: int, z: int):
        self.z =z

        if (self.ammunition == 0 and self.z <= 0):
            raise Range_Munition(" NoAmmunitionError and OutOfRangeError le z doit être positif ")
        elif self.ammunition == 0:
            raise NoAmmunitionError("NoAmmunitionError")

        elif self.z <= 0:
            self.ammunition = self.ammunition - 1
            raise OutOfRangeError("OutOfRangeError le z doit être positif")

    def __str__(self):
        return "(munition restante de Lance_missiles_anti_air  ={},rayon d'action du tir={})".format(self.ammunition, self.rayon)



class Lance_torpilles( Weapon):
    def __init__(self):
        super().__init__(ammunition=15, rayon=20)


    def fire_at(self, x: int, y: int, z: int):
        self.z =z

        if (self.ammunition == 0 and self.z > 0):
            raise Range_Munition(" NoAmmunitionError and OutOfRangeError le z doit être négatif ")
        elif self.ammunition == 0:
            raise NoAmmunitionError("NoAmmunitionError")

        elif self.z > 0:
            self.ammunition = self.ammunition - 1
            raise OutOfRangeError("OutOfRangeError le z doit être négatif")

    def __str__(self):
        return "(munition restante de Lance_torpilles  ={},rayon d'action du tir={})".format(self.ammunition, self.rayon)




"""b= Lance_missiles_antiair()
c=Lance_torpilles()
a= Lance_missiles_antisurface ()

try:
    a.fire_at(2, 3, 1)
except Range_Munition as exc:

    print("erreur, message :", exc)

except NoAmmunitionError as exc:
    print("erreur, message :", exc)

except OutOfRangeError as exc:
    print("erreur, message :", exc)


#print (a)
#print (b)
#print (c)"""


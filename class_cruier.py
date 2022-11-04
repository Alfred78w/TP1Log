import Vessel
import Lancemissilesantisurface
class Cruisier(Vessel.Vessel):
    def __init__(self,anti_air: Lancemissilesantisurface):
        super().__init__(coordinates, max_hits=6)
        self.armement = anti_air
        self.max_hits = max_hits

    def go_to(self, x, y, z):
        if z != 0:
            raise ValueError
        else:
            self.coordinates = (x, y, z)

    def fire_at(self,x,y,z):
        if self._max_hits==0:
            raise ValueError("DestroyedError")
        elif distance((x,y,z), self.coordinates)<= armement.range:
            armement.fire_at()
            


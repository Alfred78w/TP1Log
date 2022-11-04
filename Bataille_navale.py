import Vessel as vs
import Weapon as wp

class espace:
    def __init__(self, liste_de_vaisseau=[]):

        self.liste_de_vaisseau=liste_de_vaisseau

    def ajouter_vaisseau(self, a):
        cp=0
        i=vs.Vessel
        if (a.coordinates[0]<=100 and a.coordinates[0]>=0) and (a.coordinates[1]<=100 and a.coordinates[1]>=0) and  (a.coordinates[2] in [-1,0,1]):
            for i in self.liste_de_vaisseau:
                cp= cp+ i.max_hits
                if i.coordinates==a.coordinates:
                    print("Il y a déjà un vaisseau dans cette possition. Veillez changer de coordonnées svp!")
                    return

            cp = cp+a.max_hits
            if cp<=22:
                self.liste_de_vaisseau.append(a)
                print("Vaisseau ajouter avec succes")
            else:
                print("Vous aviez atteint le Hits maximal. Vous ne pouvez plus ajouter de vaisseaux. Essayez un au type de vaisseau")
                return
        else:
            print("la position de votre vaissau ne respecte pas les limites de l'espace de jeu")
            return

    def recevoir_coup(self,x,y,z):
        for i in self.liste_de_vaisseau:
            if i.coordinates==(x,y,z):
                return "Vrai"
        return "Faux"



a=vs.Cruisier((2,2,1))
b=espace([a])
print(b.liste_de_vaisseau[0].coordinates)
c=vs.Cruisier((5,2,1))
#c.max_hits=30
b.ajouter_vaisseau(c)
for i in b.liste_de_vaisseau:
    print(i.coordinates)
print(b.recevoir_coup(5,2,1))
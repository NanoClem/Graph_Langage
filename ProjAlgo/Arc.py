"""
creator : decoopmc
"""


class Arc :
    """
    Cette classe modelise le trajet entre deux arrets de bus
    Elle contient l'arret de depart et celui d'arrive
    """

    def __init__(self, startStation, endStation, mydist = None) :
        """
        CONSTRUCTEUR
        param startStation: arret de depart
        param endStation: station d'arrive
        param dist: distance entre l'arret de depart et celui d'arrivee
        """
        self.begin = startStation
        self.end   = endStation
        self.dist  = mydist          # temps, distance(nb arcs, km, ...)


    def getBegin(self) :
        """
        Retourne la station de depart
        return: station de depart
        """
        return self.begin


    def getEnd(self) :
        """
        Retourne la station d'arrive
        return: station d'arrive
        """
        return self.end


    def getDist(self) :
        """
        Retourne la distance (min, km, nbArcs) entre deux arrets
        return: distance entre deux arrets
        """
        return self.dist


    def setDist(self, new_dist) :
        """
        Renseigne la distance
        """
        self.dist = new_dist


    def printArc(self) :
        """
        Affiche le trajet entre les deux arrets
        """
        print("arret depart : " + self.begin.getName())
        print("arret suivant : " + self.end.getName())

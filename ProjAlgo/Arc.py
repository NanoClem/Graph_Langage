"""
creator : decoopmc
"""


class Arc :
    """
    Cette classe modelise le trajet entre deux arrets de bus
    Elle contient l'arret de depart et celui d'arrive
    """

    def __init__(self, startStation, endStation, mydist = 1) :
        """
        CONSTRUCTEUR
        param startStation: arret de depart
        param endStation: arret d'arrive
        param mydist: distance entre l'arret de depart et celui d'arrivee, egal a 1 par defaut
        """
        self.begin = startStation
        self.end   = endStation
        self.dist  = mydist          # poids : temps(min), distance(km, ...)


    def getBegin(self) :
        """
        Retourne l'arret de depart
        return: arret de depart
        return type : Station
        """
        return self.begin


    def getEnd(self) :
        """
        Retourne l'arret d'arrive
        return: l'arret d'arrive
        return type : Station
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


    def __str__(self) :
        """
        Surcharge pour l'affichage de l'arc
        Affiche le trajet entre deux arret lies
        """
        return self.begin.getName() + " --> " + self.end.getName()

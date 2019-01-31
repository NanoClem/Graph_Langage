"""
creator : decoopmc
"""


class Arc :
    """
    Cette classe modelise le trajet entre deux arrets de bus
    Elle contient l'arret de depart et celui d'arrive
    """

    def __init__(self, startStation, endStation) :
        """
        CONSTRUCTEUR
        :param startStation: arret de depart
        :param endStation: station d'arrive
        :param time: temps theorique en minutes mis par le bus entre chaque arret
        """
        self.begin = startStation
        self.end   = endStation
        self.time  = None           # pas encore teste


    def getBegin(self) :
        """
        Retourne la station de depart
        :return: station de depart
        """
        return self.begin


    def getEnd(self) :
        """
        Retourne la station d'arrive
        :return: station d'arrive
        """
        return self.end


    def getTime(self) :
        """
        Retourne le temps en minutes entre deux arrets
        :return: temps entre deux arrets
        """
        return self.time


    def printArc(self) :
        """
        Affiche le trajet entre les deux arrets
        """
        print("arret depart : " + self.begin.getName())
        print("arret suivant : " + self.end.getName())

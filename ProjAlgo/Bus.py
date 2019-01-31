"""
creator : decoopmc
"""


class Bus :
    """
    Cette classe modelise un bus
    Il possede un numero designant la ligne de bus, et une liste de ses arrets
    """

    def __init__(self, id, stationList = []) :
        """
        CONSTRUCTEUR de bus
        :param id: ligne du bus
        :param stationList: liste des arrets
        """
        self._num        = id
        self._stations   = stationList
        self._terminus   = None              # definir selon le sens


    def getNum(self) :
        """
        Recupere le numero de ligne du bus
        :return: ligne du bus
        """
        return self._num


    def getStations(self) :
        """
        Retourne les arrets sur le trajet du bus
        :return: liste des arrets
        """
        return self._stations


    def getNbStations(self) :
        """
        Retourne le nombre d'arrets sur le trajet du bus
        :return: nombre d'arrets
        """
        return len(self._stations)


    def getTerminus(self) :
        """
        Recupere l'arret terminus du bus
        :return: arret terminus
        """
        return self._terminus


    def setTerminus(self, new_terminus) :
        """
        Modifie l'arret terminus
        :return: arret terminus du bus
        """
        self._terminus = new_terminus


    def printStations(self):
        """
        Affiche le nom de chaque arret sur le trajet du bus
        """
        print("Bus numero " + str(self._num) + " :")
        for i in range(len(self._stations)) :
            print(self._stations[i].getName())

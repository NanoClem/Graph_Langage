"""
creator : decoopmc
"""


class Bus :
    """
    Cette classe modelise un bus
    Il possede un numero designant la ligne de bus, et une liste de ses arrets
    """

    def __init__(self, id, stationList, h = None) :
        """
        CONSTRUCTEUR de la classe Bus
        ATTRIBUTE _num : ligne du bus
        ATTRIBUTE _stations : liste des arrets
        ATTRIBUTE _terminusGo : arret terminus aller
        ATTRIBUTE _terminusBack : arret terminus retour
        ATTRIBUTE schedules : horaires du bus
        """
        self._num          = id
        self._stations     = stationList
        self._terminusGo   = self._stations[-1]
        self._terminusBack = self._stations[0]
        self.schedules     = h


    def getNum(self) :
        """
        Recupere le numero de ligne du bus
        return: ligne du bus
        """
        return self._num


    def getStations(self) :
        """
        Retourne les arrets sur le trajet du bus
        return: liste des arrets
        return type : list[] Station
        """
        return self._stations


    def getStationsName(self) :
        """
        Retourne les noms des arrets
        return : liste des noms des arrets
        return type : list[] str
        """
        names = []
        for sts in self._stations :
            names.append(sts.getName())

        return names


    def getNbStations(self) :
        """
        Retourne le nombre d'arrets sur le trajet du bus
        RETURN : nombre d'arrets
        """
        return len(self._stations)


    def getTerminusGo(self) :
        """
        Recupere l'arret terminus aller du bus
        RETURN TYPE : Station
        """
        return self._terminusGo


    def getTerminusBack(self) :
        """
        Recupere l'arret terminus retour du bus
        RETURN TYPE : Station
        """
        return self._terminusBack


    def getSchedules(self) :
        """
        Retourne les horaires du bus
        """
        return self.schedules


    def setTerminusGo(self, new_terminus) :
        """
        Modifie l'arret terminus aller
        """
        self._terminusGo = new_terminus


    def setTerminusBack(self, new_terminus) :
        """
        Modifie l'arret terminus aller
        """
        self._terminusBack = new_terminus


    def printStations(self):
        """
        Affiche le nom de chaque arret sur le trajet du bus
        """
        print("Bus numero " + str(self._num) + " :")
        for i in range(len(self._stations)) :
            print(self._stations[i])
        print('\n')

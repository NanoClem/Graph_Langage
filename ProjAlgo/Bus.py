"""
creator : decoopmc
"""


class Bus :
    """
    """

    def __init__(self, id, stationList = []) :
        """

        """
        self.num        = id
        self.stations   = stationList
        self.terminus   = None


    def getNum(self) :
        """
        """
        return self.num


    def getStations(self) :
        """
        """
        return self.stations


    def getNbStations(self) :
        """
        """
        return len(self.stations)


    def getTerminus(self) :
        """
        """
        return self.terminus


    def printStations(self) :
        """
        Affiche le nom de chaque station sur le trajet du bus courrant
        """
        print("Bus numero " + str(self.num) + " :")
        for i in range(len(self.stations)) :
            print(self.stations[i].getName())

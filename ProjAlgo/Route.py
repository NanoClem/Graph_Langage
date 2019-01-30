"""
creator : decoopmc
"""

from Bus import Bus
from Station import Station
from Arc import Arc


class Route :
    """
    """

    def __init__(self, new_bus) :
        """
        """
        self.bus   = new_bus
        self.route = []


    def buildRoute(self, sens) :
        """
        """
        stopBus = self.bus.getStations()                # liste des arrets du bus

        # SENS ALLER
        if(sens) :
            for i in range(len(stopBus)-1) :
                new_arc = Arc(stopBus[i], stopBus[i+1])
                self.route.append(new_arc)
        # SENS RETOUR
        else :
            for i in range(len(stopBus)+1, 0, -1) :
                new_arc = Arc(stopBus[i], stopBus[i-1])
                self.route.append(new_arc)


    def printRoute(self) :
        """
        """
        print("ROUTE BUS " + str(self.bus.getNum()))
        for i in range(len(self.route)) :
            self.route[i].printArc()



    def dijkstra(self) :
        """
        """
        pass

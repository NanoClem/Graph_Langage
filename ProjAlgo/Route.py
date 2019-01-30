"""
creator : decoopmc
"""

from Arc import Arc


class Route :
    """
    Cette classe represente le trajet complet d'un bus, aussi appele route \n
    La route empruntee correspond aux differents chemins entre les arrets
    compris dans le trajet du bus (arcs)
    """

    def __init__(self, new_bus) :
        """
        CONSTUCTEUR de route
        :param new_bus: bus dont la route est a construire
        :attribute route: liste des chemins (arcs) de la route
        """
        self.bus   = new_bus
        self.route = []


    def buildRoute(self, direction = True) :
        """
        Construit la route du bus en fonction du sens du trajet
        """
        stopBus = self.bus.getStations()                    # liste des arrets du bus

        # SENS ALLER
        if(direction) :
            for i in range(len(stopBus)-1) :
                new_arc = Arc(stopBus[i], stopBus[i+1])     # nouveau chemin entre deux arrets
                self.route.append(new_arc)                  # ajout du chemin au trajet du bus
        # SENS RETOUR
        else :
            for i in range(len(stopBus), 0, -1) :
                new_arc = Arc(stopBus[i], stopBus[i-1])
                self.route.append(new_arc)


    def printRoute(self) :
        """
        Affiche la route
        """
        print("ROUTE BUS " + str(self.bus.getNum()))
        for i in range(len(self.route)) :
            self.route[i].printArc()



    def dijkstra(self) :
        """
        """
        pass

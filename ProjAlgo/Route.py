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
        param new_bus: bus dont la route est a construire
        attribute ways: liste des chemins (arcs) de la route
        """
        self.bus   = new_bus
        self.ways  = []


    def getBus(self) :
        """
        Retourne le bus concerne par le trajet
        return : bus effectuant cette route
        """
        return self.bus


    def getRoute(self) :
        """
        Retourne la route du bus
        return : liste des chemins empruntes par le bus
        """
        return self.ways


    def buildRoute(self, direction = True) :
        """
        Construit la route du bus en fonction du sens du trajet
        param direction: sens du trajet du bus
        """
        stopBus = self.bus.getStations()                # liste des arrets du bus

        if(not direction) :
            stopBus.reverse()   # sens retour : on inverse l'ordre des arrets

        for i in range(len(stopBus)-1) :
            new_arc = Arc(stopBus[i], stopBus[i+1])     # nouveau chemin entre deux arrets
            self.ways.append(new_arc)                   # ajout du chemin au trajet du bus


    def printRoute(self) :
        """
        Affiche la route du bus
        """
        #ARRETS SUR LE TRAJET
        print("ROUTE LIGNE " + str(self.bus.getNum()))
        for i in range(len(self.ways)) :
            print(self.ways[i])
        #TERMINUS
        print("TERMINUS : " + self.bus.getTerminus().getName())
        print('\n')

"""
creator : decoopmc
"""

from collections import OrderedDict


class BusNetwork :
    """
    Cette classe modelise le reseau des bus
    Elle constitue un graphe des differentes routes (classe Route) en les superposant
    Autrement dit, un noeud dans ce graphe est represente par une route
    Une liaison (arc) entre deux noeuds existe s'ils ont au moins un arret en commun
    """

    def __init__(self, new_routes = []) :
        """
        CONSTRUCTEUR du reseau des bus
        param new_routes : liste des noeuds du graphe
        attribute network : noeuds du graphe
        attribute connections : liste des arcs entre les noeuds
        """
        self.network     = new_routes
        self.connections = self.prepConnections(self.network)


    def prepConnections(self, nodes) :
        """
        Regroupe l'ensemble des arcs dans une hashmap (ici un dictionnaire)
        avec la paire cle/valeur : (id du bus, arc sur sa route)
        Ainsi, on peut savoir ou se situe un arc
        param nodes : liste des routes
        return : hashmap paire cle/valeur : (id du bus, arc sur sa route)
        """
        hashmap = OrderedDict()     #table de hashage
        for net in self.network :
            for way in net.getRoute() :
                hashmap[net.getBus().getNum()] = way

        return hashmap


    def getAllStations(self) :
        """
        Retourne la liste de tous les arrets du reseau sans doublons
        return : liste de tous les arrets du graphe sans doublons
        """
        ret = []
        for net in self.network :
            for sts in net.getBus().getStations() :
                ret.append(sts.getName())

        return list(set(ret))   #creer un ensemble retire les doublons


    def getConnections(self) :
        """
        Retourne tous les chemins du reseau
        return : liste des arcs du graphe
        """
        return self.connections


    def getSameStations(self, route1, route2) :
        """
        Retourne le ou les arrets en commun entre deux routes
        return : liste des arrets en commun
        """
        bus1, bus2 = route1.getBus(), route2.getBus()
        sts1, sts2 = set(bus1.getStationsName()), set(bus2.getStationsName())
        return list(sts1 & sts2)


    def ShortestArc(self, begin, end) :
        """
        """
        pass

"""
creator : decoopmc
"""

from collections import OrderedDict


class BusNetwork :
    """
    Cette classe modelise le reseau des bus
    Elle constitue un graphe des differentes routes (classe Route) en les superposant
    Autrement dit, un noeud dans ce graphe correspond a un arret d'une route
    Une liaison entre deux routes existe si elles ont au moins un arret en commun
    """

    def __init__(self, new_routes = []) :
        """
        CONSTRUCTEUR du reseau des bus
        param new_routes : liste en entree des routes du graphe
        attribute network : routes du graphe
        attribute connections : liste des arcs entre les noeuds
        """
        self.network     = new_routes
        self.connections = self._prepConnections()


    def _prepConnections(self) :
        """
        Methode privee qui regroupe l'ensemble des arcs dans une hashmap (ici un dictionnaire)
        PAIRE KEY/VALUE : key = tuple(ArcNum,BusID)  value = Arc
        Ainsi, on peut savoir quel arc appartient a telle route
        return : hashmap key/value = tuple(ArcNum,BusID) / Arc
        return type : OrderedDict
        """
        hashmap = OrderedDict()     #table de hashage
        cpt = 0                     #compteur ArcNum du tuple(ArcNum,BusID)
        for net in self.network :
            for way in net.getRoute() :
                mykey = (cpt, net.getBus().getNum())
                hashmap[mykey] = way
                cpt += 1

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


    def printConnections(self) :
        """
        Affiche les trajets entre les arrets du reseau ainsi que la ligne de bus associee
        """
        for key,value in self.connections.items() :
            print("Ligne bus " + str(key[1]), value)


    def getSameStations(self, route1, route2) :
        """
        Retourne le ou les arrets en commun entre deux routes
        return : liste des arrets en commun
        """
        bus1, bus2 = route1.getBus(), route2.getBus()
        sts1, sts2 = set(bus1.getStationsName()), set(bus2.getStationsName())   #creation des conteneurs ensembles
        return list(sts1 & sts2)    #intersection entre deux ensembles sur les arrets


    def _getNeighbour(self, sts) :
        """
        Methode privee qui retourne les voisins d'un arret passe en parametres
        a partir des arcs auquels ils sont relies
        param sts : arret dont on cherche les voisins
        return : OrderedDict des voisins de l'arret
        return type : OrderedDict() [key=int:busID, value=Station:neighbourSTS:]
        """
        ret = OrderedDict()
        for key, value in self.getConnections().items() :
            if value.getBegin() == sts :  #trouver un voisin : matcher l'arret recherche avec un arret de depart dans un arc
                ret[key] = value.getEnd()

        return ret


    def _printNeighbour(self, sts) :
        """
        METHODE PRIVEE DE TEST
        Affiche les voisins d'un arret
        param sts : arret dont on cherche les voisins
        """
        neighbour = self._getNeighbour(sts)    #voisins de l'arret
        for key,value in neighbour.items() :

            print("Ligne Bus " + str(key[1]) + " " + sts.getName(),
                  "ARRETS VOISINS :", value)


    def Dijkstra(self, begin, end) :
        """
        Calcule le chemin le plus court d'un arret a un autre
        param begin : arret de depart
        param end : arret d'arrivee
        return : liste des arrets du chemin le plus court
        """
        node2visit  = self.getAllStations()     #liste des noeuds a visiter

        #TESTER L'EXISTENCE DES ARRETS
        while begin.getName() not in node2visit or end.getName() not in node2visit :
            print("Arrets invalides, veuillez reessayer parmis ces derniers :")
            print(node2visit, '\n')
            begin.setName(input("Saisir l'arret de depart : "))
            end.setName(input("Saisir votre destination : "))
            print('\n')

        node2visit.remove(begin.getName())      #on retire le noeud origine de la liste a visiter
        dist        = self.getConnections()     #liste des arcs contenant la distance entre les noeuds
        currentNode = begin

        while currentNode != end :
            neighbour = self._getNeighbour(currentNode)  #voisins du noeud courrant
            #traitement...
            #node2visit = node2visit.remove(currentNode.getName())
            break;

        #TEST : recuperer et afficher les voisins d'un noeud
        #self.printConnections()
        self._printNeighbour(currentNode)

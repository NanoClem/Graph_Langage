"""
creator : decoopmc
"""

from collections import OrderedDict
import math
from Arc import Arc
from Station import Station


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
        Retourne la liste de tous les objet Arrets du reseau sans doublons
        return : liste des arrets du reseau sans doublons
        return type : list[] Station
        """
        ret = []
        stsName = self.getAllStationsName()             #pour comparer arrets pour eviter les doublons

        for net in self.network :
            for sts in net.getBus().getStations() :
                if sts.getName() in stsName :           #un arret n'est pas encore apparu
                    ret.append(sts)
                    stsName.remove(sts.getName())       #on retire l'arret deja visite

        return ret


    def getAllStationsName(self) :
        """
        Retourne la liste de tous les noms arrets du reseau sans doublons
        return : liste de tous les noms des arrets du graphe sans doublons
        return type : list[] String
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
        sts1, sts2 = set(bus1.getStationsName()), set(bus2.getStationsName())   #creation des conteneurs ensembles
        return list(sts1 & sts2)    #intersection entre deux ensembles sur les arrets


    def _getNeighbour(self, sts) :
        """
        Methode privee qui retourne les voisins d'un arret passe en parametres
        a partir des arcs auquels ils sont relies
        param sts : arret dont on cherche les voisins
        return : OrderedDict des voisins de l'arret
        return type : OrderedDict() [key=int:busID, value=Station]
        """
        ret = OrderedDict()
        for key, value in self.getConnections().items() :
            if value.getBegin() == sts :  #trouver un voisin : matcher l'arret recherche avec un arret de depart dans un arc
                ret[key] = value.getEnd()

        return ret


    def _getIntersect(self, nodes1 = [], nodes2 = []) :
        """
        Compare deux listes de noeuds et retourne leur intersection
        Cette fonction se substitue aux ensembles de python (set) pour les types non hashables
        PARAM nodes1, nodes2 : listes de noeuds a comparer
        RETURN : liste contenant les elements en commun des deux listes
        RETURN TYPE : list[] Station
        """
        ret = []
        for sts in nodes1 :
            for s in nodes2 :
                if sts == s and sts not in ret :
                    ret.append(sts)

        return ret


    def _getCurrentArc(self, currentNode = None, neighbour = None):
        """
        TEMPORAIRE :
        Retourne un arc 'bouchon' avec un poids de 1 pour les tests

        Trouve l'arc associé au noeud courrant et son voisin passes
        en parametre, et le retourne
        PARAM currentNode : noeud courrant
        PARAM neighbour : voisin du noeud courrant
        PARAMS TYPE : Station
        RETURN : arc liant currentNode et neighbour
        RETURN TYPE : Arc
        """
        #POUR LES TESTS
        arcTest = Arc(Station("depart"), Station("arrivee"))
        return arcTest


    def _getNodeMinDist(self, distList = [], nodesToVisit = []) :
        """
        Cherche et retourne le noeud qui a la plus petite distance
        parmi la liste des distances à partir de la liste des noeuds à visiter
        PARAM distList : liste des distances
        PARAM nodesToVisit : liste des noeuds a visiter
        RETURN : noeud qui a la plus petite distance
        RETURN TYPE : Station
        """
        ret = None
        min = math.inf      #distance minimale initialisee a +infini
        for sts in nodesToVisit :
            currentDist = distList[self.findStsIndex(sts)]  #distance du noeud a traiter
            if currentDist < min :
                ret = sts
                min = distList[self.findStsIndex(ret)]      #nouvelle distance minimale

        return ret



    def findStsIndex(self, sts) :
        """
        Retourne l'id de l'arret du reseau passe en parametre
        Si l'arret demande n'existe pas, retourne None
        return type : int
        """
        ret = None
        if sts not in self.getAllStations() :
            print("Arret demande inconnu")
            return ret
        else :
            for s in self.getAllStations() :    #sans risque de doublons puisque getAllStations() les retire deja
                if s == sts :
                    ret = s.getId()
                    break

        return ret


    def printConnections(self) :
        """
        Affiche les trajets entre les arrets du reseau ainsi que la ligne de bus associee
        """
        for key,value in self.connections.items() :
            print("Ligne bus " + str(key[1]), value)


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
        Calcule le chemin le plus court d'un arret vers un autre

        INPUT:
            param begin : arret de depart
            param end : arret d'arrivee

        RETURN :
            liste des noeud constituant le chemin le plus court
            liste des distances tel que dist[node] = distance de begin a node
        """
        shortWay    = []
        node2visit  = self.getAllStations()                         #liste des noeuds a visiter
        dist        = [math.inf for _ in range(len(node2visit))]    #liste des distances initialise a +infini
        arcs        = self.getConnections()                         #liste des arcs ponderes

        #TESTER L'EXISTENCE DES ARRETS
        while begin not in node2visit or end not in node2visit :
            print("Arrets invalides, veuillez reessayer parmis ces derniers :")
            print(self.getAllStationsName(), '\n')
            begin.setName(input("Saisir l'arret de depart : "))
            end.setName(input("Saisir votre destination : "))
            print('\n')

        #DEBUT DE L'ALGORITHME
        current                        = begin   #initialisation du noeud courrant
        dist[self.findStsIndex(begin)] = 0       #distance au noeud origine initialisee a 0
        neighbour                      = {}      #dictionnaire des voisins des noeuds

        while current != end :
            current   = self._getNodeMinDist(dist, node2visit) #recherche du nouveau noeud courrant
            neighbour = self._getNeighbour(current)            #voisins du noeud courrant
            node2visit.remove(current)                         #le noeud courrant n'est plus a visiter
            #TRAITEMENT...
            commons = self._getIntersect(node2visit, neighbour.values())    #permet de retirer les voisins deja visites

            #BUG : l'algo parcours en largeur les voisins, liste des voisins bug ?
            # if neighbour.values() == None :
            #     print("LISTE VOISINS VIDE")
            # else :
            #     for s in neighbour.values() : print("VOISINS :", s.getName())

            for sts in commons :
                arcValue    = self._getCurrentArc(current, sts).getDist() #TODO : implementer _getCurrentArc()
                valueDist   = dist[self.findStsIndex(sts)]       #distance du noeud en traitement
                currentDist = dist[self.findStsIndex(current)]   #distance du noeud courrant

                if valueDist > currentDist + arcValue :
                    dist[self.findStsIndex(sts)] = currentDist + arcValue
                    shortWay.append(sts.getName())
                    print("ARRET SUIVANT :", sts)

        return dist, shortWay

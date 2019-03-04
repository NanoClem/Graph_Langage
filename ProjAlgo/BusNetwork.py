"""
creator : decoopmc
"""

from collections import OrderedDict
import math


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
        attribute network : liste des routes du graphe
        attribute connections : liste des arcs entre les noeuds
        attribute distList : liste des distances par rapport au noeud de depart
        attribute fathers : dictionnaire des predecesseurs de chaque arret selon le chemin emprunte
        attribute shortestWay : liste du chemin le plus court
        """
        self.network        = new_routes
        self.connections    = {}
        self.distList       = []
        self.fathers        = {}
        self.shortestWay    = []



    #TROUVER UN MOYEN DE SAVOIR SI ON EST EN ARC PONDERES OU NON
    def _prepConnections(self, doHours) :
        """
        Methode privee qui regroupe l'ensemble des arcs dans une hashmap (ici un dictionnaire)
        PAIRE KEY/VALUE : key = tuple(ArcNum,BusID)  value = Arc
        Ainsi, on peut savoir quel arc appartient a tel bus, et donc a telle route
        return : hashmap key/value = tuple(ArcNum,BusID) / Arc
        return type : OrderedDict
        """
        hashmap = OrderedDict()     #table de hashage
        cpt = 0                     #compteur ArcNum du tuple(ArcNum,BusID)
        for net in self.network :
            route = net.getUnWeightRoute()
            if doHours :
                route = net.getWeightRoute()
            for way in route :
                mykey = (cpt, net.getBus().getNum())
                hashmap[mykey] = way
                cpt += 1

        return hashmap



    def exists(self, sts) :
        """
        Verifie l'existence d'un arret de bus dans le reseau

        PARAM sts : arret dont on veut tester l'existance
        RETURN : vrai s'il existe, faux sinon
        RETURN TYPE : boolean
        """
        if sts in self.getAllStations() :
            return True

        return False



    def existsByName(self, stsName) :
        """
        Verifie l'existence d'un arret de bus par son nom dans le reseau

        PARAM stsName : nom de l'arret dont on veut tester l'existence
        RETURN : vrai s'il existe, faux sinon
        RETURN TYPE : boolean
        """
        if stsName in self.getAllStationsName() :
            return True

        return False



    def getStation(self, name) :
        """
        Retourne l'arret correspondant au nom passe en parametre
        """
        ret = None
        for sts in self.getAllStations() :
            if sts.getName() == name :
                ret = sts
                break

        return ret



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



    def getDistList(self):
        """
        Retourne la liste des distances du reseau
        RETURN : liste des distances
        """
        return self.distList



    def _getFathers(self) :
        """
        Retourne les predecesseurs de chaque arret en fonction du parcours
        effectue par l'algorithme du chemin le plus court
        RETURN : dictionnaire des predecesseurs
        RETURN TYPE : Dict(string, string)
        """
        return self.fathers



    def getShortestWay(self, begin, end, doHours) :
        """
        Calcule le chemin le plus court a partir
        des resultats de Dijkstra
        """
        self.connections = self._prepConnections(doHours)
        sts = end
        self.Dijkstra(begin, end)

        while sts != begin :
            self.shortestWay.append(sts)
            sts = self.getStation(self.fathers[sts.getName()])

        return self.shortestWay + [begin]



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
            elif value.getEnd() == sts :
                ret[key] = value.getBegin()

        return ret



    def _getIntersect(self, nodes1 = [], nodes2 = []) :
        """
        Retourne l'intersection de deux listes
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
        Trouve l'arc associé au noeud courrant et son voisin passes
        en parametre, et le retourne
        Renvoie None si l'arc n'a pas ete trouve
        PARAM currentNode : noeud courrant
        PARAM neighbour : voisin du noeud courrant
        PARAMS TYPE : Station
        RETURN : arc liant currentNode et neighbour
        RETURN TYPE : Arc
        """
        ret = None
        for arc in self.getConnections().values() :
            sts = [arc.getBegin(), arc.getEnd()]
            if currentNode in sts and neighbour in sts :
                ret = arc
                break

        return ret



    def findStsIndex(self, sts) :
        """
        Retourne l'indice de l'arret passe en parametre, comprit dans la liste du reseau
        Si l'arret demande n'existe pas, retourne None
        INPUT : arret recherche
        return type : int
        """
        ret    = None
        allSts = self.getAllStations()  #pas de doublons : getAllStations() les retire
        if sts not in self.getAllStations() :
            print("BusNetwork.findStsIndex() : Arret demande inconnu")
            return ret

        ret = allSts.index(sts)
        return ret



    def printConnections(self) :
        """
        Affiche les trajets entre les arrets du reseau
        ainsi que la ligne de bus associee
        """
        for key,value in self.connections.items() :
            print("Ligne bus " + str(key[1]), value)



    def printShortestWay(self, begin, end, doHours) :
        """
        Affiche le chemin le plus court d'un
        parcours effectue au prealable
        PARAM begin/end :
        """
        toPrint = self.getShortestWay(begin, end, doHours)
        toPrint.reverse()
        print(begin, "---->", end)

        if not doHours :
            for sts in toPrint :
                print("ARRET SUIVANT :", sts)
        else :
            total = 0
            for i in range(len(toPrint)-1) :
                a = self._getCurrentArc(toPrint[i], toPrint[i+1])    # arc liant les arrets du chemin
                w = a.getDist()                                      # poids de l'arc en minutes
                total += w
                print(a, "TEMPS : %d minutes" %w)
            print("TEMPS TOTAL : %d minutes" %total)



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



    def _getNodeMinDist(self, nodesToVisit = []) :
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
            currentDist = self.distList[self.findStsIndex(sts)]  #distance du noeud a traiter
            if currentDist < min :
                ret = sts
                min = currentDist     #nouvelle distance minimale

        return ret



    def _majDist(self, currentNode, neighbourNode) :
        """
        Met a jour la liste des distances du reseau
        PARAM currentNode : noeud courrant
        PARAM neighbourNode : son noeud voisin
        """
        arcValue    = self._getCurrentArc(currentNode, neighbourNode).getDist()   #poid de l'arc entre le noeud courrant et son voisin
        valueDist   = self.distList[self.findStsIndex(neighbourNode)]             #distance du noeud voisin
        currentDist = self.distList[self.findStsIndex(currentNode)]               #distance du noeud courrant

        if  valueDist > currentDist + arcValue :
            self.distList[self.findStsIndex(neighbourNode)] = currentDist + arcValue    #maj des distances
            self.fathers.setdefault(neighbourNode.getName(), currentNode.getName())     #maj des predecesseurs



    def Dijkstra(self, begin, end) :
        """
        Calcule toutes les distances possibles à partir du depart
        jusqu'a atteindre l'arret demande
        Remplis egalement le dictionnaire des predecesseurs

        INPUT:
            param begin : arret de depart
            param end : arret d'arrivee
        """
        #VARIABLES
        self.fathers = {}                      #dictionnaire des predecesseurs
        node2visit   = self.getAllStations()   #liste des noeuds a visiter

        #INITIALISATION
        current                        = begin                                         #initialisation du noeud courrant
        self.distList                  = [math.inf for _ in range(len(node2visit))]    #liste des distances initialise a +infini
        neighbour                      = {}                                            #dictionnaire des voisins du noeud courrant
        self.distList[self.findStsIndex(begin)] = 0                                    #distance au noeud origine initialisee a 0

        #DEBUT DE L'ALGORITHME
        while node2visit :
            current = self._getNodeMinDist(node2visit)                      #recherche du nouveau noeud courrant
            node2visit.remove(current)                                      #le noeud courrant n'est plus a visiter
            neighbour = self._getNeighbour(current)                         #voisins du noeud courrant
            commons   = self._getIntersect(node2visit, neighbour.values())  #permet de retirer les voisins deja visites
            for sts in commons :
                self._majDist(current, sts)                                 #mise a jour des distances

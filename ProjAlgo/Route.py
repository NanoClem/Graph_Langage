"""
creator : decoopmc
"""

import time
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



    def isWeekEnd(self) :
        """
        Renvoie vrai si l'on est en week-end, faux sinon
        RETURN TYPE : boolean
        """
        days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
        if days[time.localtime()[6]] in days[5:7] :     #si aujourd'hui est dans le week-end
            return True

        return False



    def calcWeight(self, sts1, sts2) :
        """
        Calcule le poids d'un arc liant deux arrets
        Le poids est represente sous forme de minutes
        RETURN : poids de l'arc en minutes
        """
        #On recupere le nom du jour (aujourd'hui)
        schedules = self.bus.getSchedules().getWeHolidaysDate()
        if not self.isWeekEnd() :
            schedules = self.bus.getSchedules().getRegularDate()

        #ICI TEST ALLER OU RETOUR

        #sch = self.bus.getSchedules().toDatetime(schedules[0])  #sens aller pour les tests
        # for key, value in sch :



    #NE PAS OUBLIER DE PRENDRE EN COMPTE LE SENS POUR LES HORAIRES ALLER OU RETOUR
    def buildUnWeightRoute(self) :
        """
        Construit la route effectuee par le bus
        Cette methode ne prends pas en compte les poids des arcs
        """
        stsBus = self.bus.getStations()                # liste des arrets du bus
        for i in range(len(stsBus)-1) :
            new_arc = Arc(stsBus[i], stsBus[i+1])     # nouveau chemin entre deux arrets
            self.ways.append(new_arc)                   # ajout du chemin au trajet du bus



    #RECUPERER L'HEURE ACTUELLE POUR SAVOIR QUELLES TRANCHE HORAIRE TRAITER
    #NE PAS OUBLIER DE PRENDRE EN COMPTE LE SENS POUR LES HORAIRES ALLER OU RETOUR
    def buildWeightRoute(self) :
        """
        Construit la route effectuee par le bus
        Cette methode prends en compte les horaires des bus,
        et donc les poids des arcs
        """
        stsBus = self.bus.getStations()                # liste des arrets du bus
        for i in range(len(stsBus)-1) :
            new_arc = Arc(stsBus[i], stsBus[i+1])     # nouveau chemin entre deux arrets
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

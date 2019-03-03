"""
creator : decoopmc
"""

import time
from datetime import datetime
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
        ATTRIBUTE unWays : liste des chemins non ponderes de la route
        attribute ways: liste des chemins ponderes (arcs) de la route
        """
        self.bus    = new_bus
        self.unWays = []
        self.ways   = []



    def getBus(self) :
        """
        Retourne le bus concerne par le trajet
        return : bus effectuant cette route
        """
        return self.bus



    def getUnWeightRoute(self) :
        """
        Retourne la route du bus
        return : liste des chemins empruntes par le bus
        """
        return self.unWays


    def isWeekEnd(self) :
        """
        Renvoie vrai si l'on est en week-end, faux sinon
        RETURN TYPE : boolean
        """
        days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
        if days[time.localtime()[6]] in days[5:7] :     #si aujourd'hui est dans le week-end
            return True

        return False



    def isGo(self) :
        """
        Permet de determiner si l'on se trouve
        en sens aller ou retour
        """
        pass



    def nextHour(self, hours, idCurrentH) :
        """
        Recupere la prochaine heure de passage du bus
        par rapport a l'heure passee en parametre
        PARAM hours : liste des horaires du bus, list[] time
        PARAM idCurrentH : index de l'heure dont on veut connaître la suivante
        """
        ret = None
        list(filter(None.__ne__, hours))                # DEUXIEME SECURITE SUR LES HEURES NON DISPONIBLES
        if hours[idCurrentH] == hours[-1] :             # si l'heure courrante est la derniere de la journee
            ret = hours[0]                              # on renvoie la premiere heure disponible du lendemain
        else :                                          # sinon
            ret = hours[idCurrentH + 1]                 # l'heure suivante est trouvee

        return ret



    def toMinutes(self, myTime) :
        """
        Calcule les minutes totales a partir
        d'un type time
        PARAM myTime : variable de type time
        """
        minutesTime = myTime.hour*60 + myTime.minute
        return minutesTime



    def calcWeight(self, sts1, sts2, dateNow) :
        """
        Calcule le poids en minutes d'un arc liant deux arrets
        Il est a remarquer que cette methode calcule le temps de trajet
        entre deux arrets quels qu'ils soient
        RETURN : poids de l'arc en minutes
        """
        #RECUPERATION DES HORAIRES : week-end ou semaine
        schedules = self.bus.getSchedules().getWeHolidaysDate()
        if not self.isWeekEnd() :
            schedules = self.bus.getSchedules().getRegularDate()

        #TEST ALLER OU RETOUR
        # sch = None
        # if self.isGo() :
        #     sch = ...
        # else :
        #     sch = ...
        sch      = self.bus.getSchedules().toDatetime(schedules[0])     # horaires sens aller pour les tests
        sts      = [sts1.getName(), sts2.getName()]                     # nom des arret dont on veut determiner
        weight   = 0                                                    # poids de l'arc en minutes
        goodHour = []                                                   # horaires correspondant au prochain passage

        for s in sts :
            list(filter(None.__ne__, sch[s]))    # ON ENLEVE LES HEURES OU LE BUS NE PASSE PAS
            for t in sch[s] :
                if self.toMinutes(t) < self.toMinutes(dateNow) :             # si l'heure proposee est depassee
                    goodHour.append(self.nextHour(sch[s], sch[s].index(t)))  # prochaine heure disponible de passage du bus
                    break
                else :
                    goodHour.append(t)
                    break

        weight = self.toMinutes(goodHour[1]) - self.toMinutes(goodHour[0])  # temps en minutes entre le trajet de deux arrets
        return weight



    def buildUnWeightRoute(self) :
        """
        Construit la route effectuee par le bus
        Cette methode ne prends pas en compte les poids des arcs
        """
        stsBus = self.bus.getStations()                       # liste des arrets du bus
        for i in range(len(stsBus)-1) :
            new_arc = Arc(stsBus[i], stsBus[i+1])             # nouveau chemin entre deux arrets
            self.unWays.append(new_arc)                       # ajout du chemin au trajet du bus



    #NE PAS OUBLIER DE PRENDRE EN COMPTE LE SENS POUR LES HORAIRES ALLER OU RETOUR
    def buildWeightRoute(self) :
        """
        Construit la route effectuee par le bus
        Cette methode prends en compte les horaires des bus,
        et donc les poids des arcs
        """
        stsBus  = self.bus.getStations()        # liste des arrets du bus
        timeNow = datetime.now().time()         # heure actuelle
        for i in range(len(stsBus)-1) :
            weight  = self.calcWeight(stsBus[i], stsBus[i+1], timeNow)  # poids du chemin en minutes
            new_arc = Arc(stsBus[i], stsBus[i+1], weight)               # nouveau chemin entre deux arrets
            self.ways.append(new_arc)                                   # ajout du chemin au trajet du bus



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

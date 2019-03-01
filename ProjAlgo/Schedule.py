"""
creator : decoopmc
"""

from datetime import time



class Schedule :
    """
    Cette classe definie les horaires d'un bus,
    pour les heures regulieres et week-end/vacances,
    pur chaque arret
    """

    def __init__(self, num, regularGo={}, regularBack={}, weHolidaysGo={}, weHolidaysBack={}) :
        """
        CONSTRUCTEUR de classe Schedule
        ATTRIBUTE busID : numero du bus concerne par les horaires
        ATTRIBUTE regularGo/regularBack : horaires regulieres aller/retour
        ATTRIBUTE weHolidaysGo/weHolidaysBack : horaires week-end/vacances aller/retour
        """
        self.busID       = num
        self.dateRegGo   = regularGo
        self.dateRegBack = regularBack
        self.dateWeHolidaysGo = weHolidaysGo
        self.dateWeHolidaysBack = weHolidaysBack


    def getRegularDate(self) :
        """
        Retourne les horaires regulieres aller/retour
        """
        return [self.dateRegGo, self.dateRegBack]


    def getWeHolidaysDate(self) :
        """
        Retourne les horaires week-end/vacances aller/retour
        """
        return [self.dateWeHolidaysGo, self.dateWeHolidaysBack]


    def setRegularDate(self, go = None, back = None) :
        """
        Modifie les horaires regulieres aller/retour
        PARAMS go/back : horaires aller/retour
        """
        if go != None :
            self.dateRegGo = go
        if back != None :
            self.dateRegBack = back


    def setWeHolidaysDate(self, go = None, back = None) :
        """
        Modifie les horaires week-end/vacances aller/retour
        PARAMS go/back : horaires aller/retour
        """
        if go != None :
            self.dateWeHolidaysGo = go
        if back != None :
            self.dateWeHolidaysBack = back


    def toDatetime(self, dates) :
        """
        Converti sous forme de datetime les horaires du bus
        PARAM dates : dates a convertir
        RETURN TYPE : dict() (string/time)
        """
        datesTime = {}
        for key,value in dates.values() :
            if value != '-' :
                h = time(int(value.split(':')[0]), int(value.split(':')[1]))
                datesTime[key] = h
            else :
                datesTime[key] = None   #pas d'horaires a ce moment

        return datesTime

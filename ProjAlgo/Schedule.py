"""
creator : decoopmc
"""


class Schedule :
    """
    """


    def __init__(self, num, regularGo={}, regularBack={}, weHolidaysGo={}, weHolidaysBack={}) :
        """
        Cette classe definie les horaires d'un bus,
        pour les heures regulieres et week-end/vacances
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

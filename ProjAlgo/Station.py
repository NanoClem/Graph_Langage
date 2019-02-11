"""
creator : decoopmc
"""


class Station :
    """
    Cette classe correspond a un arret de bus
    Elle possede un nom
    """

    def __init__(self, inputName, num = None) :
        """
        CONSTRUCTEUR de station
        param inputName: nom de la station
        parm num : numero de l'arret
        """
        self.id    = num
        self._name = inputName


    def getName(self) :
        """
        Recupere le nom de la station
        return type : String
        """
        return self._name


    def getId(self) :
        """
        Retourne l'id de l'arret
        return type : int
        """
        return self.id


    def setName(self, new_name) :
        """
        Modifie le nom de l'arret
        param new_name : nouveau nom de l'arret
        """
        self._name = new_name


    def setID(self, new_id) :
        """
        Modifie l'id de l'arret
        param new_id : nouvel id de l'arret
        """
        self.id = new_id


    def __eq__(self, sts) :
        """
        Surcharge de l'operateur ==
        param stationName: nom de la station a comparer
        """
        return self._name == sts.getName()


    def __str__(self) :
        """
        Surcharge pour l'affichage en print
        """
        return self.getName()

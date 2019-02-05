"""
creator : decoopmc
"""


class Station :
    """
    Cette classe correspond a un arret de bus
    Elle possede un nom
    """

    def __init__(self, inputName) :
        """
        CONSTRUCTEUR de station
        param inputName: nom de la station
        """
        self._name = inputName


    def getName(self) :
        """
        Recupere le nom de la station
        """
        return self._name


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

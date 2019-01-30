"""
creator : decoopmc
"""


class Station :
    """
    """


    def __init__(self, inputName) :
        """
        """
        self.name = inputName


    def getName(self) :
        """
        """
        return self.name


    def __eq__(self, stationName) :
        """
        """
        return self.name == stationName

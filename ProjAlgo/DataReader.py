"""
creator : decoopmc
"""


class DataReader :
    """
    Cette classe a pour but de lire les diffentes donnees des lignes de bus
    dans un fichier texte
    Les donnees recuperees sont :
        - les noms des arrets
        - les horaires des bus (normales, nuit, vacances, dimanche et feries)
    """

    def __init__(self, Fname) :
        """
        CONSTRUCTEUR de lecteur de fichier de donnees de circulation
        :param Fname: nom du fichier
        """
        self._filename = Fname
        self._content  = ""
        self._stsName  = []

        # LECTURE DU FICHIER ENTIER
        try :
            with open(self._filename, 'r', encoding="utf-8") as f :
                self._content = f.read()
        except IOError :
            print("Erreur : le fichier n'a pas pu etre ouvert !")


    def sliceContent(self) :
        """
        Decoupe et renvoie les blocs separes par un double retour chariot
        :return: liste des blocs
        """
        return self._content.split("\n\n")


    def setFilename(self, new_filename):
        """
        Modifie le nom du fichier contenant
        les donnees
        """
        self._filename = new_filename


    def printStsName(self) :
        """
        Affiche la liste des arrets
        lus dans le fichier
        """
        for station in self._stsName :
            print(station + " | ", end='')  # pas de retour a la ligne


    def readStations(self) :
        """
        Lis le nom des differents arrets inscrits dans
        le fichier et les ajoute a la liste des noms
        """
        raw_names     = self.sliceContent()[0]        # chaine brute des noms d'arrets
        raw_names     = raw_names.replace('+', 'N')   # remplacement du char '+' en 'N'
        self._stsName = raw_names.split(" N ")        # recuperation des noms individuels

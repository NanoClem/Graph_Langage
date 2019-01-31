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

    def __init__(self) :
        """
        CONSTRUCTEUR de lecteur de fichier de donnees de circulation
        param Fname : nom du fichier
        """
        self._filename = ""
        self._content  = ""


    def setReader(self, new_filename) :
        """
        Modifie le fichier a lire, nettoie le contenu deja lu precedemment et lis le nouveau contenu
        param new_filename : nouveau nom du fichier
        """
        self._filename = new_filename
        self._content  = ""
        # LECTURE DU FICHIER ENTIER
        try :
            with open(self._filename, 'r', encoding="utf-8") as f :
                self._content = f.read()
        except IOError :
            print("Erreur : le fichier n'a pas pu etre ouvert !")


    def setFilename(self, new_filename):
        """
        Modifie le nom du fichier contenant
        les donnees
        """
        self._filename = new_filename


    def sliceContent(self) :
        """
        Decoupe et renvoie les blocs separes par un double retour chariot
        return : liste des blocs
        """
        return self._content.split("\n\n")


    def readStations(self) :
        """
        Retourne le nom des differents arrets lus dans le fichier
        return : liste des noms des arrets
        """
        raw_names     = self.sliceContent()[0]        # chaine brute des noms d'arrets
        raw_names     = raw_names.replace('+', 'N')   # remplacement du char '+' en 'N'
        return raw_names.split(" N ")                 # recuperation des noms individuels

"""
creator : decoopmc
"""

from DataReader import DataReader
from Schedule import Schedule
from Bus import Bus
from Station import Station
from Route import Route
from BusNetwork import BusNetwork



def createStations(names) :
    """
    Construit une liste d'arrets de bus (class Station)
    return : liste des arrets
    """
    stationsBus = []
    for i in range(len(names)) :
        new_station = Station(names[i])
        stationsBus.append(new_station)

    return stationsBus


def doWantHours() :
    """
    Demande a l'utilisateur s'il veut prendre en compte les horaires
    dans le choix de son itineraire
    RETURN : Vrai si l'utilisateur veut les horaires, Faux sinon
    """
    options = ["y", "n"]
    wantHours = input("Voulez-vous prendre en compte les horaires ? y/n : ")
    while wantHours not in options :
        wantHours = input("Cette option n'existe pas, veuillez choisir entre y/n : ")

    return wantHours == 'y'


def userInteraction(net) :
    """
    Regroupe les gestions de l'utilisateur et ses interactions dans le programme
    Cela lui permet de choisir les arrets entre lesquels il veut connaitre le chemin le plus court
    INPUT :
        param net : reseau de bus sur lequel l'utilisateur se base
    RETURN :
        liste des arrets choisis tels que [depart, destination]
        booleen indiquant si l'utilisateur veut prendre en compte les horaires ou non
    """
    inputUser = []
    options = ["Saisir l'arret de depart : ", "Saisir votre destination : "]

    for i in range(2) :
        name = input(options[i])
        while not net.existsByName(name) :
            print("Cet arret n'existe pas, veuillez reessayer parmis ces derniers :")
            print(net.getAllStationsName())
            print('\n')
            name = input(options[i])
        inputUser.append(name)

    start           = net.getStation(inputUser[0])
    destination     = net.getStation(inputUser[1])
    return [start, destination]



def main() :

    # LECTURES DES DONNEES SIBRA
    reader = DataReader()                      # nouvel objet pour la lecture des donnees
    ligne1 = "1_Poisy-ParcDesGlaisins.txt"     # fichier des horaires de la ligne 1
    ligne2 = "2_Piscine-Patinoire_Campus.txt"  # fichier des horaires de la ligne 2

    # BUS
    #LIGNE 1
    reader.setReader(ligne1)                              # injection du nom du fichier pour la lecture
    stations1     = reader.readStationsName()             # lecture du nom des arrets de la ligne 1
    schedules1    = reader.getSchedules()                 # lecture des horaires de la ligne 1
    schedules1Obj = Schedule(schedules1[0], schedules1[1], schedules1[2], schedules1[3])
    Sibra1        = Bus(1, createStations(stations1), schedules1Obj)    # nouvel objet Bus
    #LIGNE2
    reader.setReader(ligne2)
    stations2     = reader.readStationsName()
    schedules2    = reader.getSchedules()
    schedules2Obj = Schedule(schedules2[0], schedules2[1], schedules2[2], schedules2[3])
    Sibra2        = Bus(2, createStations(stations2), schedules2Obj)

    # ROUTE DES BUS
    #SIBRA1
    pathSibra1 = Route(Sibra1)
    pathSibra1.buildUnWeightRoute()     # construction de la route non ponderee
    pathSibra1.buildWeightRoute()       # construction de la route ponderee
    #SIBRA2
    pathSibra2 = Route(Sibra2)
    pathSibra2.buildUnWeightRoute()
    pathSibra2.buildWeightRoute()

    # RESEAU DES BUS
    SibraNetwork = BusNetwork([pathSibra1, pathSibra2])
    #============================================================
    #   TEST 1 : Bus et ses arrets
    #============================================================
    # Sibra1.printStations()
    # Sibra2.printStations()

    #============================================================
    #   TEST 2 : Trajet du bus
    #============================================================
    # pathSibra1.printRoute()
    # pathSibra2.printRoute()

    #============================================================
    #   TEST 3 : Reseau des bus
    #============================================================
    #sameSts    = SibraNetwork.getSameStations(pathSibra1, pathSibra2)    # liste des arrets en commun
    #print("ARRETS EN COMMUN : ", sameSts)                                # arrets en commun entre chaque route de bus
    #print("ARRETS DU RESEAU : ", SibraNetwork.getAllStationsName())      # tous les arrets du reseau
    #SibraNetwork.printConnections()                                      # affichage des trajet entre les arrets du reseau

    #============================================================
    #   TEST 4 : Horaires
    #============================================================
    

    #============================================================
    #   TEST 5 : Plus court chemin
    #============================================================
    userChoices   = userInteraction(SibraNetwork)                                   # l'user choisi les arrets
    userWantHours = doWantHours()                                                   # on demande si l'user veut prendre en compte les horaires
    SibraNetwork.printShortestWay(userChoices[0], userChoices[1], userWantHours)    # affichage du chemin le plus court



if __name__ == '__main__':
    main()

"""
creator : decoopmc
"""

from DataReader import DataReader
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



def main() :

    # LECTURES DES DONNEES SIBRA
    reader = DataReader()                      # nouvel objet pour la lecture des donnees
    ligne1 = "1_Poisy-ParcDesGlaisins.txt"     # fichier des horaires de la ligne 1
    ligne2 = "2_Piscine-Patinoire_Campus.txt"  # fichier des horaires de la ligne 2

    # BUS
    #LIGNE 1
    reader.setReader(ligne1)                      # injection du fichier pour la lecture
    stations1 = reader.readStations()             # lecture du nom des arrets de la ligne 1
    Sibra1    = Bus(1, createStations(stations1)) # nouvel objet Bus
    #LIGNE2
    reader.setReader(ligne2)
    stations2 = reader.readStations()
    Sibra2    = Bus(2, createStations(stations2))

    # ROUTE DES BUS
    #SIBRA1
    pathSibra1 = Route(Sibra1)      # construction de la route
    pathSibra1.buildRoute(True)     # Sens aller
    #SIBRA2
    pathSibra2 = Route(Sibra2)
    pathSibra2.buildRoute(True)

    # RESEAU DES BUS
    SibraNetwork = BusNetwork([pathSibra1, pathSibra2])
    sameSts      = SibraNetwork.getSameStations(pathSibra1, pathSibra2)    # liste des arrets en commun

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
    print("ARRETS EN COMMUN : ", sameSts)   # arrets en commun entre chaque route de bus
    print("ARRETS DU RESEAU : ", SibraNetwork.getAllStations())


if __name__ == '__main__':
    main()

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
        new_station = Station(names[i], i)
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
    stations1 = reader.readStationsName()         # lecture du nom des arrets de la ligne 1
    Sibra1    = Bus(1, createStations(stations1)) # nouvel objet Bus
    #LIGNE2
    reader.setReader(ligne2)
    stations2 = reader.readStationsName()
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
    #print("ARRETS EN COMMUN : ", sameSts)   # arrets en commun entre chaque route de bus
    #print("ARRETS DU RESEAU : ", SibraNetwork.getAllStationsName())
    #SibraNetwork.printConnections() #affichage des trajet entre les arrets du reseau

    #============================================================
    #   TEST 4 : Plus court chemin
    #============================================================
    start               = Station(input("Saisir l'arret de depart : "))
    destination         = Station(input("Saisir votre destination : "))
    startID, destID     = SibraNetwork.findStsID(start), SibraNetwork.findStsID(destination)

    start.setID(startID)
    destination.setID(destID)

    print("CHEMIN LE PLUS COURT :")
    print(SibraNetwork.Dijkstra(start, destination)[1])



if __name__ == '__main__':
    main()

"""
creator : decoopmc
"""

from DataReader import DataReader
from Bus import Bus
from Station import Station
from Route import Route


def main() :

    # LECTURES DES DONNEES SIBRA
    filename = "1_Poisy-ParcDesGlaisins.txt"    # fichier des horaires Sibra1
    reader = DataReader(filename)               # nouvel objet pour la lecture des donnees
    reader.readStations()                       # lecture du nom des arrets


    # ARRETS DE BUS
    stationName = reader.getDataNames()
    stationsBus = []

    for i in range(len(stationName)) :
        new_station = Station(stationName[i])
        stationsBus.append(new_station)

    Sibra1 = Bus(1, stationsBus)
    Sibra1.setTerminus(stationsBus[-1])         # dernier arret de la liste


    # ROUTE DES BUS
    pathSibra1 = Route(Sibra1)
    pathSibra1.buildRoute(True)     # Sens aller


    #============================================================
    #   TEST 1 : Lecture du fichier
    #============================================================
    #reader.printStsName()   #Affichage des noms des stations

    #============================================================
    #   TEST 2 : Bus et ses arrets
    #============================================================
    #Sibra1.printStations()

    #============================================================
    #   TEST 3 : Trajet du bus
    #============================================================
    pathSibra1.printRoute()



if __name__ == '__main__':
    main()

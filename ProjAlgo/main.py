"""
creator : decoopmc
"""


from Bus import Bus
from Station import Station
from Route import Route


def main() :
    """
    """
    # RENSEIGNEMENT DES ARRETS DE BUS
    stationName = ["LYCÉE_DE_POISY", "POISY_COLLÈGE", "Vernod"]
    stationsBus = []

    for i in range(len(stationName)) :
        new_station = Station(stationName[i])
        stationsBus.append(new_station)

    Sibra1 = Bus(1, stationsBus)


    # RENSEIGNEMENT DU TRAJET
    pathSibra1 = Route(Sibra1)
    pathSibra1.buildRoute(True)     # Sens aller



    #============================================================
    #   TEST 1 : Bus et ses arrets
    #============================================================
    Sibra1.printStations()

    #============================================================
    #   TEST 2 : Trajet du bus
    #============================================================
    pathSibra1.printRoute()


if __name__ == '__main__':
    main()

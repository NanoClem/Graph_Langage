# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 13:39:00 2018

@author: Clément
"""


class Arc :
    """
    Cette classe modelise un arc entre deux noeuds
    pour le diagramme PERT
    """
    
    
    def __init__(self, s_previous, s_next, name, period) :
        """
        Constructuer
        :param s_previous: etape precedente
        :param s_next: etape suivante
        :param name: nom de la tache
        :param period: temps de realisation
        """
        self.s_previous = s_previous
        self.s_next     = s_next
        self.name       = name
        self.period     = period
        
        
        
    def getName(self) :
        """
        Retourne le nom de la tache
        :return: nom de la tache
        """
        return self.name
    
    
    
    def getPeriod(self) :
        """
        Retourne la duree de la tache
        :return: duree de la tache
        """
        return self.period
    
    
    
    def getBeginStep(self) :
        """
        Retourne l'etape de depart de l'arc
        :return: etape de depart
        """
        return self.s_previous
    
    
    
    def getEndStep(self) :
        """
        Retourne l'etape d'arrivee de l'arc
        :return: etape d'arrivee
        """
        return self.s_next
        
        
        
        
        
        
        
        
        
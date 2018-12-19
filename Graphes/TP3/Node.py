# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 13:43:54 2018

@author: dupouyj
"""


class Node:
    """
        Cette classe modelise un noeud
    """
    
    def __init__(self, number, date_au_plus_tot, date_au_plus_tard, previous_steps=[], next_steps=[]):
        """
            CONSTRUCTEUR
            :param content: etiquette du noeud
            :param children: liste des enfant du noeud
            :type content: str
            :type children: list
        """
        self.number=number
        self.date_au_plus_tot=date_au_plus_tot
        self.date_au_plus_tard=date_au_plus_tard
        self.previous_steps=previous_steps
        self.next_steps=next_steps
    

    def get_number(self):
        """
            accesseur du numero du noeud
            :return: numero du noeud
        """
        return self.number
    
    def get_au_plus_tot(self):
        """
            accesseur de la date au plus tot du noeud
            :return: date au plus tot
        """
        return self.date_au_plus_tot
    
    def get_au_plus_tard(self):
        """
            accesseur de la date au plus tard du noeud
            :return: date au plus tard
        """
        return self.date_au_plus_tard
    
    def get_previous_steps(self):
        """
            accesseur des etapes precedentes d'un noeud 
            :return: liste des etapes precedentes
        """
        return self.previous_steps
    
    def get_next_steps(self):
        """
            accesseur des etapes suivantes d'un noeud 
            :return: liste des etapes suivantes
        """
        return self.next_steps
    


# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:33:47 2018

@author: Clément
"""

import numpy as np
from Forest import *


# =============================================================================
#   CLASSE ARBORESCENCE
#       representation ensembliste
#
#   Arguments :
#       vertices = numero des noeuds
#       edges    = definition des liaisons entre les noeuds
# =============================================================================
class Arborescence :
    
    '''
    CONSTRUCTEUR
    '''
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges    = edges
        
        
    '''
    FONCTION RACINE
        retourne la racine de l'arborescence
    '''
    def root(self):
        
        fathers = [ p[0] for p in self.edges ]
            
    
    
    '''
    
    '''
    def isEmpty():
        pass
    
    
    '''
    
    '''
    
    
    
    '''
    
    '''
    def profondeur(self):
        
        if self.isEmpty():
            return False
        
        f = Forest(self)
        return f.profondeur()
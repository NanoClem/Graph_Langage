# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 14:11:45 2018

@author: Clément
"""

import numpy as np

  
# =============================================================================
#   CLASSE FOREST
# =============================================================================
class Forest :
    
    '''
    
    '''
    def __init__(self, arbo, remains) :
        pass
    
    
    '''
    
    '''
    def isEmpty():
        pass
    
    
    '''
    
    '''
    def root():
        pass
    
    
    '''
    
    '''
    def firstTree():
        pass
    
    
    '''
    
    '''
    def subTree():
        pass
    
    
    '''
    
    '''
    def remains():
        pass
    
    
    '''
    
    '''
    def profondeur(self):
        
        if self.isEmpty():
            return False
        
        current_node = self.firstTree().root()
        #...Traitement
        
        remains      = self.remains()
        subTree      = self.firstTree().subTree()
        
        # creation de la nouvelle foret
        new_forest   = Forest(subTree, remains)
        new_forest.profondeur()
        
        return
    
    
    '''
    
    '''
    def largeur(self):
            
        if self.isEmpty():
            return False
        
        current_node = self.firstTree().root()
        #...Traitement
        
        remains      = self.remains()
        subTree      = self.firstTree().subTree()
        
        # creation nouvelle foret
        new_forest   = Forest(remains, subTree)
        new_forest.largeur()
        
        return
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
    def __init__(self, content, children = []) :
        self.content  = content
        self.children = children
    
    
    '''
    FONCTION ISEMPTY
        permet de savoir si la forêt est vide
    '''
    def isEmpty(self):
        if not self.content :
            return True
        else :
            return False
    
    
    '''
    RACINE DE LA FORET
        retourne la racine de la forêt (lui-même)
    '''
    def root(self):
        return self
    
    
    '''
    PREMIER ARBRE DE LA FORET
        retourne le premier arbre de la forêt
    '''
    def firstTree(self):
        return self.content
    
    
    '''
    SOUS-ARBRES DE LA FORET
        retourne la liste des sous-arbres de la forêt
    '''
    def subTree(self):
        return self.children
    
    
    '''
    RESTE DE LA FORET
        retourne le reste de la forêt (la forêt sans le premier arbre)
    '''
    def remains(self):
        ret = []
        for trees in self.content :
            if trees != self.firstTree():
                ret.append(trees)
                
        return ret
    
    
    '''
    PARCOURS DE LA FORET EN PROFONDEUR
    '''
    def profondeur(self):
        
        if self.isEmpty():
            return []
        
        current_node = self.firstTree().root()
        
        remains      = self.remains()
        subTree      = current_node.firstTree().subTree()
        
        # creation de la nouvelle foret
        new_forest   = Forest(subTree, remains)
        return new_forest.profondeur()

    
    
    '''
    PARCOURS DE LA FORET EN LARGEUR
    '''
    def largeur(self):
            
        if self.isEmpty():
            return []
        
        current_node = self.firstTree().root()
        
        remains      = self.remains()
        subTree      = current_node.firstTree().subTree()
        
        # creation nouvelle foret
        new_forest   = Forest(remains, subTree)
        return new_forest.largeur()
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 14:11:45 2018

@author: Clément
"""

class Forest :
    """
        cette classe permet de representer une liste d'arbres afin de les traiter
        plus facilement
    """
    
    def __init__(self, content) :
        '''
            CONSTRUCTEUR
            :param content: liste des arbres de la foret
        '''
        self.content  = content
    
    
    
    def isEmpty(self):
        '''
            permet de savoir si la forêt est vide
            :param self: la foret elle-meme
            :type self: Forest
        '''
        if not self.content :
            return True
        else :
            return False
    
    
    
    def root(self):
        '''
            retourne la racine de la forêt (lui-même)
            :param self: la foret elle-meme
            :type self: Forest
        '''
        return self
    
    
    
    def firstTree(self):
        '''
            retourne le premier arbre de la forêt si la foret n'est pas vide
            retourne une liste vide sinon
            :param self: la foret elle-meme
            :type self: Forest
        '''
        if self.isEmpty():
            return []
        
        return self.content[0]
    
    
    
    def SubTree_of_FirstTree(self) :
        '''
            retourne la liste des sous-arbres du premier arbre de la foret si elle n'est pas vide
            retourne une liste vide sinon
            :param self: la foret elle-meme
            :type self: Forest
        '''
        if self.isEmpty() :
            return []
            
        return self.firstTree().get_children()   # liste des sous-arbre du premier arbre
    
    
    
    def rest(self) :
        '''
            retourne le reste de la foret si elle n'est pas vide
            retourne une liste vide sinon
            :param self: la foret elle-meme
            :type self: Forest
        '''
        if self.isEmpty():
            return []
        
        return self.content[1:]     # liste des arbres de la foret sans le premier arbre
    


    def profondeur(self):
        '''
            parcours de la forêt en profondeur
            :param self: la foret elle-meme
            :type self: Forest
            
        '''
        if self.isEmpty():
            return []
        
        current_node = self.firstTree().root()                  # on récupere la racine du premier arbre de la foret
        subTree      = current_node.subTree_of_FirstTree()      # la liste des sous arbres du premier arbre de la foret
        rest         = self.rest()                              # reste de la foret
        
        # CREATION DE LA NOUVELLE FORET
        new_forest   = Forest(subTree + rest)                   # on s'interesse en premier aux sous-arbres du premier arbre 
        return new_forest.profondeur()


    
    def largeur(self):
        '''
            parcours de la foret en largeur
            :param self: la foret elle-meme
            :type self: Forest
        '''
        if self.isEmpty():
            return []
        
        current_node = self.firstTree().root()                  # on récupere la racine du premier arbre de la foret
        subTree      = current_node.subTree_of_FirstTree()      # la liste des sous arbres du premier arbre de la foret
        rest         = self.rest()                              # reste de la foret
        
        # CREATION DE LA NOUVELLE FORET
        new_forest   = Forest(rest + subTree)                   # on s'interesse en premier au reste de la foret
        return new_forest.largeur()
        
        
        
        
        
        
        
        
        
        
        
        
        
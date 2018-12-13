# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 08:23:37 2018

@author: Clément
"""

from BNode import BNode



class ABR(BNode) :
    """
    Cette classe represente un ABR qui est un BNode prennant 
    en parametre une liste de valeurs
    """


    def __init__(self, label, lChild, rChild, values) :
        """
        Constructeur de la classe ABR
        :param label, lChild, rChild: attributs de la classe parente BNode
        :param values: liste des etiquettes
        """
        super().__init__(label, h, lChild, rChild)       # constructeur parent
        self.values = values
    
    
    
    def root(self) :
        """
        Retourne la racine de l'ABR
        :return: racine de l'ABR
        """
        return self
    
    
        
    def getMedianHigh(self) :
        """
        Retourne la mediane au plus grand
        :return: mediane de la liste au plus petit
        """
        temp     = self.values.sort()           # tri dans l'ordre croissant
        medIndex = int(len(temp)/2)+1           # index de la mediane au plus grand
        median   = self.values[medIndex]        # mediane de la liste
        
        return median
    
    
    
    def getMedianLow(self) :
        """
        Retourne la mediane au plus petit
        :return: mediane de la liste au plus petit
        """
        temp     = self.values.sort()           # tri dans l'ordre croissant
        medIndex = int(len(temp)/2)             # index de la mediane au plus petit
        median   = self.values[medIndex]        # mediane de la liste
        
        return median
    
    
    
    def setLeftChild(self, new_node) :
        """
        Remplace le noeud fils gauche
        :param new_node: nouveau fils gauche
        """
        self.leftChild = new_node
    
    
    
    def setRightChild(self, new_node) :
        """
        Remplace le noeud fils gauche
        :param new_node: nouveau fils gauche
        """
        self.rightChild = new_node
        
        
    
    def rotG(self) :
        """
        Effectue une rotation a gauche de l'ABR
        """
        
        abr2 = self.rightChild
        
        abr3 = ABR(self.values)
        abr3.setLeftChild(self.leftChild)
        abr3.setContent(self.content)
        abr3.setRightChild(abr2.leftChild)
        
        retABR = ABR(self.values)
        retABR.setLeftChild(abr3)
        retABR.setContent(abr2.content)
        retABR.setRightChild(abr2.rightChild)
        
        return retABR
        
        
    
    
            
    def add_node(self, label) :
        """
        Ajoute un noeud dans l'ABR
        :param label: etiquette du noeud a ajouter
        """
        pass
        
        
    
    def balance(self) :
        """
        
        """
        pass
    
    
    
    def makeABR() :
        """
        
        """
        pass
        
    
    
    
    
# =============================================================================
#  TESTS
# =============================================================================

#abr = ABR()













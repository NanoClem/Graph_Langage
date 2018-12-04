# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:37:39 2018

@author: dupouyj
@doc : Clément
"""

class Node:
    """
        Cette classe modelise un noeud
    """
    
    def __init__(self,content,children=[]):
        """
            CONSTRUCTEUR
            :param content: etiquette du noeud
            :param children: liste des enfant du noeud
            :type content: str
            :type children: list
        """
        self.content=content
        self.children=children
    

    
    def get_content(self):
        """
            accesseur de l'etiquette du noeud
            :return: etiquette du noeud
        """
        return self.content


    
    def get_children(self):
        """
            accesseur des enfants du noeud
            :return: liste des enfants du noeud
        """
        ret=[]
        if self.children==ret:
            return self.children
        else:
            for i in range(len(self.children)):
                if self.children[i]!=None:
                    ret.append(self.children[i].get_content())
            return ret


    
    def get_descending(self):
        """
            retourne la liste des descendants du noeud
            :return: liste des descendants
        """
        if self.is_leaf():
            return self.get_children()
        else:
            ret=[]
            for i in range(len(self.get_children())):
                ret = ret + self.children[i].get_descending()
            return self.get_children() + ret 


    
    def is_leaf(self):
        """
            permet de savoir si le noeud est une feuille
            :return: booleen
        """
        return self.get_children() == []


    
    def degree(self):
        """
            permet de connaitre le degre du noeud
            :return: degre du noeud
        """
        return len(self.get_children())
    
    
    

# =============================================================================
# Implementation de l'arborescence
# =============================================================================

n6=Node('9')
n5=Node('3')
n4=Node('3')
n3=Node('m')
n2=Node('a')
n1=Node('2',[n4,n5,n6])
n0=Node('z',[n1,n2,n3])


# =============================================================================
# Tests
# =============================================================================
print("Enfants du noeud 1 :", n1.get_children())
print("Enfants du noeud 6 :", n6.get_children())
print("Test feuille noeud 1 :", n1.is_leaf())
print("Test feuille noeud 6 :", n6.is_leaf())
print("Descendants du noeud 0 :", n0.get_descending())
print("Descendants du noeud 5 :", n5.get_descending())
print("Degré du noeud 1 :", n1.degree())
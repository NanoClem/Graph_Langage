# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:59:05 2018

@author: dupouyj
"""

from Forest import Forest



class RTree:
    def __init__(self,content,children=[]):
        '''
            Constructeur
        '''
        self.content=content
        self.children=children
    
    def get_content(self):
        '''
            Retourne l'étiquette
        '''
        return self.content
    
    def root(self):
        return self

    def get_children(self):
        ret=[]
        if self.children==ret:
            return self.children
        else:
            for i in range(len(self.children)):
                if self.children[i]!=None:
                    ret.append(self.children[i].get_content())
            return ret
    
    def sub_tree(self):
        return self.get_children()
    
    def get_descending(self):
        if self.is_leaf():
            return self.get_children()
        else:
            ret=[]
            for i in range(len(self.get_children())):
                ret = ret + self.children[i].get_descending()
            return self.get_children() + ret

    def get_father(self,noeud):
        for i in range(len(self.children)):
            if noeud==self.children[i]:
                return self
        for i in range(len(self.children)):
            return self.children[i].get_father(noeud)
            
    def get_ascending(self,noeud):
        if self.get_father(noeud)==None:
            return []
        else:
            pere=self.get_father(noeud)
            return [pere.get_content()]+self.get_ascending(pere)
    
    def is_leaf(self):
        return self.get_children()==[]
    
    def display_deph(self):
        F=Forest([self])
        return F.display_deph()
    
    def display_width(self):
        F=Forest([self])
        return F.display_width()
    
    




# =============================================================================
# Implementation de l'arborescence
# =============================================================================

n6=RTree('9')
n5=RTree('3')
n4=RTree('3')
n3=RTree('m')
n2=RTree('a')
n1=RTree('2',[n4,n5,n6])
n0=RTree('z',[n1,n2,n3])

# =============================================================================
# Test
# =============================================================================
print(n0.sub_tree())
print(n0.get_father(n5).get_content())
print(n0.get_father(n2).get_content())
print(n0.get_father(n0))
print(n0.get_ascending(n4))
print(n0.get_ascending(n0))

print(n0.display_deph())
#print(n0.display_width())
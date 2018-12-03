# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:37:39 2018

@author: dupouyj
@doc : Clément
"""

class Node:
    def __init__(self,content,children=[]):
        self.content=content
        self.children=children
        
    def get_content(self):
        return self.content
    
    def get_children(self):
        ret=[]
        if self.children==ret:
            return self.children
        else:
            for i in range(len(self.children)):
                if self.children[i]!=None:
                    ret.append(self.children[i].get_content())
            return ret
    
    def get_descending(self):
        if self.is_leaf():
            return self.get_children()
        else:
            ret=[]
            for i in range(len(self.get_children())):
                ret = ret + self.children[i].get_descending()
            return self.get_children() + ret 
    
    def is_leaf(self):
        return self.get_children()==[]
    
    def degree(self):
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
print(n1.get_children())
print(n6.get_children())
print(n1.is_leaf())
print(n6.is_leaf())
print(n0.get_descending())
print(n5.get_descending())
print(n1.degree())
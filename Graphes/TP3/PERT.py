# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 14:01:04 2018

@author: Clément, dupouyj
"""

from Node import Node
from Arc import Arc
import math


class PERT :
    def __init__(self, nodes=[], arcs=[]):
        self.nodes=nodes
        self.arcs=arcs
    
    def get_nodes(self):
        return self.nodes
    
    def get_arcs(self):
        return self.arcs
    
    def is_empty(self,elem):
        return elem==[]
    
    def root(self):
        for i in self.nodes:
            if i.get_previous_steps()==[]:
                return i
        
    def make_pert(self):
        pass
    
    def diff(self,node):
        return node.get_au_plus_tard - node.get_au_plus_tot
        
    def critique(self, node):
        """

        """        
        if node.get_next_steps() == [] :
            return [node]
        
        crit=math.inf
        indice_node=0
        for i in range(len(node.get_next_steps())) :
            if self.diff(node.get_next_steps()[i]) < crit:
                crit = self.diff(node.get_next_steps()[i])
                indice_node=i
        return [node.get_next_steps()[indice_node]] + self.critique(node.get_next_steps()[indice_node])
                


# =============================================================================
# 
# =============================================================================

if __name__=="__main__":
    n0=Node(0,0,0,[],n1)
    n1=Node(1,30,30,[n0],[n2,n4])
    n2=Node(2,120,120,[n1],[n3,n6])
    n3=Node(3,150,210,[n2],[n7])
    n4=Node(4,40,200,[n1],[n5])
    n5=Node(5,50,210,[n4],[n7])
    n6=Node(6,150,150,[n2],[n7])
    n7=Node(7,210,210,[n3,n6,n5],[n8])
    n8=Node(8,220,220,[n7])
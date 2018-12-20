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
    
    
    
    def get_arc(self, node1, node2):
        for arc in self.get_arcs() :
            if arc.getBeginStep() == node1 and arc.getEndStep() == node2:
                return arc
            
    
    
    def is_empty(self,elem):
        return elem==[]
    
    
    
    def root(self):
        for i in self.nodes:
            if i.get_previous_steps()==[]:
                return i
    

    
    def make_pert(self):
        pass
    
    
    
    def diff(self,node):
        return node.get_au_plus_tard() - node.get_au_plus_tot()
        
    
    
    def critique(self, node):
        """

        """        
        if node.get_next_steps() == [] :  #considerer le noeud lui meme au lieu du suivant
            return [node.number]
        
        crit=math.inf
        indice_node=0
        for i in range(len(node.get_next_steps())) :
            if self.diff(node.get_next_steps()[i]) < crit:
                crit = self.diff(node.get_next_steps()[i])
                indice_node=i
        return [node.number] + self.critique(node.get_next_steps()[indice_node])
    
    
    
    def computeLate(self) :
        """
        
        """
        node2manage = self.get_nodes()
        while node2manage != [] :
            
            for node in node2manage :
                if node.get_previous_steps() == [] :
                    node.setDateLate(0)
                    return True
                
                if node.getDateLate() == None :
                    print("je fais rien")
                    
                else :
                    previous_arc = self.get_arc(node, node.get_previous_steps())
                    arc_value = previous_arc.getPeriod()
                    current_date = node.getDateLate()
                
                    node.get_previous_steps().setDateLate(current_date - arc_value)
        
        return True
                   
                


# =============================================================================
# 
# =============================================================================

if __name__ == "__main__" :
    n8=Node(8,220,220,[],[])
    n7=Node(7,210,210,[],[n8])
    n6=Node(6,150,150,[],[n7])
    n5=Node(5,50,210,[],[n7])
    n4=Node(4,40,200,[],[n5])
    n3=Node(3,150,210,[],[n7])
    n2=Node(2,120,120,[],[n3,n6])
    n1=Node(1,30,30,[],[n2,n4])    
    n0=Node(0,0,0,[],[n1])
    n7.setPrevious([n3,n6,n5])
    
    n8.setPrevious([n7])
    n6.setPrevious([n2])
    n5.setPrevious([n4])
    n4.setPrevious([n1])
    n3.setPrevious([n2])
    n2.setPrevious([n1])
    n1.setPrevious([n0])
    
    nodes=[n0,n1,n2,n3,n4,n5,n6,n7,n8]
    
    
    a9=Arc(n7,n8,'H',10)
    a8=Arc(n5,n7,None,0)
    a7=Arc(n3,n7,None,0)
    a6=Arc(n6,n7,'G',60)
    a5=Arc(n2,n6,'F',30)
    a4=Arc(n4,n5,'E',10)
    a3=Arc(n1,n4,'D',10)
    a2=Arc(n2,n3,'C',30)
    a1=Arc(n1,n2,'B',90)
    a0=Arc(n0,n1,'A',30)
    
    
    Pert=PERT(nodes)
    print(Pert.critique(Pert.root()))
    
    
    
    
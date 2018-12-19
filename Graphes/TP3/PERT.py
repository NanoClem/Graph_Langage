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
    

    
    def get_arc(self,node1,node2):
        for a in self.arcs:
            if a.s_previous==node1 and a.s_next==node2:
                return a
    
    
    
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
                


            
    def unknownOPlusTot(self,previouses):
        for i in range(len(previouses)):
            if previouses[i].date_au_plus_tot==None:
                return True


   
    def compute_au_plus_tot3(self, node2manage):
        if node2manage==[]:
            return
        
        current_node = node2manage[0]
        previouses = current_node.previous_steps
        if previouses==[]:
            current_node.date_au_plus_tot=0
            self.compute_au_plus_tot3(node2manage[1:])
        
        if self.unknownOPlusTot(previouses):
            self.compute_au_plus_tot2(node2manage+[current_node])
        
        else:
            date=0
            for i in range(len(previouses)):
                arc=self.get_arc(previouses[i],current_node)
                
                if previouses[i].date_au_plus_tot + arc.period > date:
                    date = previouses[i].date_au_plus_tot + arc.period
                    current_node.date_au_plus_tot = date
                    self.compute_au_plus_tot3(node2manage[1:])
         
            
# =============================================================================
# 
# =============================================================================

if __name__=="__main__":
    n8=Node(8,None,220,[],[])
    n7=Node(7,None,210,[],[n8])
    n6=Node(6,None,150,[],[n7])
    n5=Node(5,None,210,[],[n7])
    n4=Node(4,None,200,[],[n5])
    n3=Node(3,None,210,[],[n7])
    n2=Node(2,None,120,[],[n3,n6])
    n1=Node(1,None,30,[],[n2,n4])    
    n0=Node(0,None,0,[],[n1])
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
    
    arcs=[a0,a1,a2,a3,a4,a5,a6,a7,a8,a9]
    
    Pert=PERT(nodes,arcs)
    #print(Pert.critique(Pert.root()))
    Pert.compute_au_plus_tot3(Pert.nodes)
    for i in Pert.nodes:
        print("date au plus tot du noeud "+str(i.number), i.date_au_plus_tot)
    
    
    
    
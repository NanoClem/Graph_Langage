# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 14:01:04 2018

@author: Clément, dupouyj
"""

from Node import Node
from Arc import Arc
import math


class PERT :
    """
    Cette classe modelise un diagramme PERT
    qui est un DAG
    """
    
        
    def __init__(self, nodes=[], arcs=[]):
        """
        Constructeur
        :param nodes: liste des etapes
        :param arcs: liste des taches
        """
        self.nodes=nodes
        self.arcs=arcs
    
    
    
    def get_nodes(self):
        """
        Retourne la liste des etapes
        :return: liste des etapes
        """
        return self.nodes
    
    
    
    def get_arcs(self):
        """
        Retourne la liste des taches
        :return: liste des taches
        """
        return self.arcs
    
    
    
    def is_empty(self, elem):
        """
        Verifie si une liste est vide
        :param elem: liste a verifier
        """
        return elem == []
    
    
    
    def root(self):
        """
        Retourne l'etape qui n'a pas d'etape precedente
        :return: noeud racine du PERT
        """
        for i in self.nodes:
            if i.get_previous_steps()==[]:
                return i

    
    
    def get_arc(self,node1,node2):
        """
        Cherche et retourne la tache entre deux etapes
        :param node1: etape precedent la tache
        :param node2: etape suivant la tache
        :return: tache entre les deux etapes
        """
        for a in self.arcs:
            if a.s_previous==node1 and a.s_next==node2:
                return a
    
    
    
    def diff(self,node):
        """
        Effectue la difference de la date au plus tard par la date au plus tot d'un noeud
        :param node: etape a traiter
        :return: difference entre date au plus tot et date au plus tard
        """
        return node.get_au_plus_tard() - node.get_au_plus_tot()
        
    
    
    def critique(self, node):
        """
        Cherche et retourne le chemin critique d'un diagramme PERT
        :param node: etape courrante du taitement
        :return: liste des etapes faisant parties du chemin critique
        """        
        if node.get_next_steps() == [] :
            return [node.number]
        
        crit = math.inf
        indice_node = 0
        for i in range(len(node.get_next_steps())) :
            if self.diff(node.get_next_steps()[i]) < crit :
                crit = self.diff(node.get_next_steps()[i])
                indice_node = i
        return [node.number] + self.critique(node.get_next_steps()[indice_node])
                


            
    def unknownOPlusTot(self, previouses):
        """
        Verifie si la date au plus tot d'une etape n'est pas renseignee
        :param previouses: liste des etapes precedentes
        :return: booleen
        """
        for i in range(len(previouses)):
            if previouses[i].date_au_plus_tot==None:
                return True


   
    def compute_au_plus_tot(self, node2manage):
        """
        Renseigne la date au plus tot des etapes
        :param node2manage: etape a traiter
        """
        if node2manage==[]:
            return
        
        current_node = node2manage[0]
        previouses = current_node.previous_steps
        if previouses==[]:
            current_node.date_au_plus_tot=0
            self.compute_au_plus_tot(node2manage[1:])
        
        if self.unknownOPlusTot(previouses):
            self.compute_au_plus_tot2(node2manage+[current_node])
        
        else:
            date=0
            for i in range(len(previouses)):
                arc=self.get_arc(previouses[i],current_node)
                
                if previouses[i].date_au_plus_tot + arc.period > date:
                    date = previouses[i].date_au_plus_tot + arc.period
                    current_node.date_au_plus_tot = date
                    self.compute_au_plus_tot(node2manage[1:])
         
            
# =============================================================================
# 
# =============================================================================

if __name__=="__main__":
    
    # DIAGRAMME PERT
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
    
    
    # LISTE DES ETAPES
    nodes=[n0,n1,n2,n3,n4,n5,n6,n7,n8]
    
    
    # TACHES
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
    
    # LISTE DES TACHES
    arcs=[a0,a1,a2,a3,a4,a5,a6,a7,a8,a9]
    
    
    # TRAITEMENTS
    Pert=PERT(nodes,arcs)                   # PERT
    #print(Pert.critique(Pert.root()))      # chemin critique
    Pert.compute_au_plus_tot(Pert.nodes)    # date au plus tot
    for i in Pert.nodes:
        print("date au plus tot du noeud "+str(i.number), i.date_au_plus_tot)
    
    
    
    
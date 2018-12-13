# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 08:16:09 2018

@author: dupouyj
"""


class BNode :
    """
        La classe modelise un abr equilibre sous forme de noeuds
        :param static cpt: compteur static de classe 
    """
    cpt=0



    def __init__(self, content, leftChild=None, rightChild=None) :
        '''
            Constructeur
            :param content, leftChild, rightChild:
        '''
        self.leftChild  = leftChild
        self.rightChild = rightChild
        self.content    = content
        self.height     = self.calculateHeight()
        
    
    
    def root(self) :
        """
        Retourne la racine du BNode
        :return: racine du BNode
        """
        return self
    
    
    
    def get_children(self):
        '''
            Retourne les enfants d'un noeud
            :param: node
            :return: list
        '''
        ret=[]
        if self.leftChild != None:
            ret=ret+[self.leftChild]
        if self.rightChild != None:
            ret=ret+[self.rightChild]
        return ret
    


    def getContent(self) :
        """
        Retourne le contenu de l'ABR
        :return: contenu de l'ABR
        """
        return self.content
    
    
    
    def getHeight(self) : 
        """
        Retourne la hauteur du BNode, -1 si la hauteur est nulle
        :return: hauteur du BNode
        """
        return -1 if self.root() == None else self.height
        
    
    
    
    def setContent(self, new_content) :
        """
        Modifie le contenue du BNode
        :param new_node: nouveau contenu
        """
        self.content = new_content
        
      
        
    def calculateHeight(self) :
        """
        Calcule la hauteur du BNode, au moins egale a 1
        :return: hauteur du BNode
        """
        if self.leftChild == None or self.rightChild == None :
            return 1
        
        return  1 + max(self.leftChild.getHeight(), self.rightChild.getHeight())
        
    
    
    def exist(self,look4):
        '''
            Retourne True si l'etiquette recherchee existe dans l'arbre, et False sinon
            :param: node, etiquette
            :return: bool
        '''
        BNode.cpt+=1
        if self.content==str(look4):
            return True
        found = False
        for i in range(len(self.get_children())):
            found=found or self.get_children()[i].exist(look4)
            
        return found
    


def exist_list(liste,look4):
    '''
        Retourne True si l'etiquette recherchee existe dans une liste, et False sinon
            :param: liste, etiquette
            :return: bool
    '''
    cpt=0
    for i in range(len(liste)):
        cpt+=1
        if liste[i]==look4:
            return True, cpt
    return False, cpt



# =============================================================================
# MAIN PROGRAM
# =============================================================================

if __name__ == "__main__" :
    
    # =============================================================================
    # Implementation d'un ABR
    # =============================================================================
    
    n10=BNode('100')
    n9=BNode('55')
    n8=BNode('30')
    n7=BNode('0')
    n6=BNode('91',None,n10)
    n5=BNode('77',n9,None)
    n4=BNode('10',None,n8)
    n3=BNode('1',n7,None)
    n2=BNode('80',n5,n6)
    n1=BNode('2',n3,n4)
    n0=BNode('42',n1,n2)
    
    abr=[42,2,80,1,10,77,91,0,30,55,100]
    
    # =============================================================================
    # Tests
    # =============================================================================
    
    print("leftChild n1 : ", n1.rightChild.content)
    print("enfants n2 : ", n2.get_children())
    
    
    # =============================================================================
    # Comparaisons methodes exist
    # =============================================================================
    
    print("\n recherche avec les deux versions de exist pour chaque valeur de l'ABR" )
    moyenne1=0
    moyenne2=0
    # recherche avec les deux versions de exist pour chaque valeur de l'ABR
    for i in range(len(abr)):
        print("valeur :" + str(abr[i]))
        print("exist      ", (n0.exist(abr[i]), BNode.cpt))
        print("exist list ", exist_list(abr,abr[i]))
        print('\n')
        moyenne1+=BNode.cpt
        moyenne2+=exist_list(abr,abr[i])[1]
    
    print("moyenne de comparaison methode exist =", moyenne1/len(abr))
    print("moyenne de comparaison methode exist list =", moyenne2/len(abr))


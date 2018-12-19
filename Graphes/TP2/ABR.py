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


    def __init__(self, values, label=None, lChild=None, rChild=None) :
        """
        Constructeur de la classe ABR
        :param lChild, rChild: attributs de la classe parente BNode
        :param values: liste des etiquettes
        """
        self.values = values
        super().__init__(label, lChild, rChild)       # constructeur parent
        
        
        
    def __eq__(self, other) :
        """
        Surcharge de l'operateur == pour les ABR
        """        
        return self.getContent() == other.getContent()
    
    
    
    def __lt__(self, other) :
        """
        Surcharge de l'operateur < pour les ABR
        """
        return self.getContent() < other.getContent()
    
    
    
    def __gt__(self, other) :
        """
        Surcharge de l'operateur > pour les ABR
        """
        return self.getContent() > other.getContent()
    
    
    
    def root(self) :
        """
        Retourne la racine de l'ABR
        :return: racine de l'ABR
        """
        return self
    
    
    
    def isNull(self) :
        """
        Verifie si la racine est nulle
        :return: True si la racine est nulle, False sinon
        """
        return self.root() == None
    
    
    
    def isEmpty(self) :
        """
        Verifie si la liste des etiquettes est vide
        :return: True si la liste est vide, False sinon
        """
        return self.values == None
    
    
        
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
    
    
    
    def getValues(self) :
        """
        Retourne la liste des etiquettes de l'ABR
        :return: liste des etiquettes
        """
        return self.values
    
    
    
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
        Effectue une rotation a gauche non destructive de l'ABR
        :return: l'ABR qui a subi une rotation a gauche
        """
        abr2   = self.rightChild                                                     # sous-ABR egal au fils droit de l'ABR  
        abr3   = ABR(self.values, self.getContent(), self.leftChild, abr2.leftChild)
        retABR = ABR(self.values, abr2.getContent(), abr3, abr2.rightChild)          # ABR rotationne a gauche (rassemblement des sous ABR)
        
        return retABR
    
    
    
    def rotD(self) :
        """
        Effectue une rotation à droite non destrucitve de l'ABR
        :return: l'ABR qui a subi une rotation a droite
        """
        abr2   = self.leftChild
        abr3   = ABR(self.values, self.getContent(), abr2.rightChild, self.rightChild)
        retABR = ABR(self.values, abr2.getContent(), abr2.leftChild, abr3)
        
        return retABR
        
    
        
    def balance(self) :
        """
        Equilibre l'ABR en effectuant une double rotation (gauche puis droite)
        si la hateur du petit-fils gauche du noeud courrant est inférieur celle du petit-fils droit, 
        sinon une simple rotation a droite \n
        Il n'y a aucune rotation si la difference de la hauteur du fils gauche par celle du fils droit n'est pas egale a 2 ou -2
        :return: l'ABR equilibre
        """
        hL = self.leftChild.getHeight()     # hauteur du fils gauche de l'ABR courrant
        hR = self.rightChild.getHeight()    # hauteur du fils droit de l'ABR courrant
        
        if hL - hR == 2 or hL - hR == -2:
            
            if self.leftChild.leftChild.getHeight() < self.leftChild.rightChild.getHeight() :
                self.leftChild = self.leftChild.rotG()      # rotation a gauche
            return self.rotD()      # rotation a droite
        
        return self.root()
                

    
            
    def add_node(self, label) :
        """
        Ajoute un noeud dans l'ABR et l'equilibre
        :param label: etiquette du noeud a ajouter
        """
        if label == None :
            return self.root()
#         Si la racine est nulle
        if self.isNull() :
            return ABR(self.values, label, None, None)
        # contenu du noeud courrant superieur
        if(label < self.getContent()) :
            self.leftChild = self.leftChild.add_node(label)
        # contenu du noeud courrant inferieur
        if(label > self.getContent()) :
            self.rightChild = self.rightChild.add_node(label)
            
        return self.balance()
        
        
    
    def makeABR(self) :
        """
        Fabrique un ABR a partir d'une liste de valeurs
        :return: ABR construit a partir de sa liste de valeur en attribut
        """
        if self.values == None :
            return self.root()
                
        # Construction de l'ABR
        v = self.values.pop()                   # la valeur est enlevee de la liste dans tous les cas
        if v != None and not self.exist(v) :    # on ajoute le noeud s'il n'existe pas deja
            self.add_node(v)
            
        return self.makeABR()
            
        
        
        
    

# =============================================================================
#  MAIN PROGRAM
# =============================================================================

if __name__ == "__main__" :
    
    intVal  = [1, 5, 9, 7, 6, 4, 8, 3, 2]              # liste des labels(entiers)
    charVal = ["il", "est", "2", "h", "a", "laide"]    # liste des labels(char), compares selon la longueur de chaîne
    
    intABR = ABR(intVal)
    intABR = intABR.makeABR()
    
    
    
    













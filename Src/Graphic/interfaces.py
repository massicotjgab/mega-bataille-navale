import sys

from PySide2.QtCore import QObject, Signal, Property, Slot, qDebug
from PySide2.QtWidgets import QApplication, QLabel
from PySide2.QtQml import QQmlApplicationEngine
from Src.GameEngine.GameEngine import Joueur

class playerInfo(QObject):
    def __init__(self):
        super(playerInfo, self).__init__()
        self.Joueur1 = Joueur()
        

    @Slot(str)
    def name(self, name):
        self.Joueur1.name=name
        qDebug ("Nom : " + name)
    #tram= self.Joueur1.format_pseudo() #voir avec fonction thomas start server
            
    @Slot(result="QVariantList")
    def updateDef(self):
        tab_defense = self.Joueur1.formate_defense_gui()
        tab_defense[0]=1
        print (tab_defense)
        return tab_defense

    @Slot(result="QVariantList")
    def updateAtt(self):
        tab_attaque = self.Joueur1.formate_attaque_gui()
        
        #print (tab_attaque)
        return tab_attaque
        
        
        
        


    








    @Slot(str)
    def ipadd(self, ip):
        qDebug ("Ip : " + ip)



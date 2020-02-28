import sys

from PySide2.QtCore import QObject, Signal, Property, Slot, qDebug
from PySide2.QtWidgets import QApplication, QLabel
from PySide2.QtQml import QQmlApplicationEngine
from Src.GameEngine.GameEngine import Joueur

class GameEngine(QObject):
    def __init__(self):
        super(GameEngine, self).__init__()
        self.Joueur1 = Joueur("")

    @Slot(str)
    def setName(self, name):
        self.Joueur1.change_pseudo=name
        qDebug ("Nom : " + name)
    #tram= self.Joueur1.format_pseudo() #voir avec fonction thomas start server
   
    @Slot(str)
    def setIp(self, ip):
        qDebug ("Ip : " + ip)
            
    @Slot(result="QVariantList")
    def updateDef(self):
        self.Joueur1.place_bateau_test() #test de placement de bateau
        self.Joueur1.place_nucleaire_test() #test de placement de bateau
        tab_defense = self.Joueur1.formate_defense_gui()
        #tab_defense[0]=1
        #print (tab_defense)
        return tab_defense

    @Slot(result="QVariantList")
    def updateAtt(self):
        tab_attaque = self.Joueur1.formate_attaque_gui()
        
        #print (tab_attaque)
        return tab_attaque
        
        
        
        


    











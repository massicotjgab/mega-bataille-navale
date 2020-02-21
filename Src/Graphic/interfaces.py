import sys

from PySide2.QtCore import QObject, Signal, Property, Slot, qDebug
from PySide2.QtWidgets import QApplication, QLabel
from PySide2.QtQml import QQmlApplicationEngine   

class playerInfo(QObject):
    @Slot(str)
    def name(self, name):
        qDebug ("Nom : " + name)
    
    @Slot(str)
    def ipadd(self, ip):
        qDebug ("Ip : " + ip)
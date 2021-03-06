import sys

from PySide2.QtCore import QObject, Signal, Property, Slot, qDebug
from PySide2.QtWidgets import QApplication, QLabel
from PySide2.QtQml import QQmlApplicationEngine
from interfaces import *

if __name__ == "__main__":
    gEngineUI = GameEngine()

    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Expose the Python object to QML
    context = engine.rootContext()
    context.setContextProperty("gEngineUI", gEngineUI)

    engine.load("Src/Graphic/qml/MainWindow.qml")
    sys.exit(app.exec_())
    
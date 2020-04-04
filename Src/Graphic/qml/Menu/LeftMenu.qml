import QtQuick 2.6
import QtQuick.Layouts 1.14
import QtQuick.Window 2.14
import QtQuick.Controls 2.14
import QtQuick.Controls.Styles 1.4

//MENU

ColumnLayout{
    id: colBat
    Layout.margins: 25
    Layout.fillWidth: true
    property var batTab : ["Porte-Container 5x2","Porte-Avion 5x1","Destroyer 4x1","Torpilleur 3x2","Sous-Marin Nucléaire 6x1","Petit Sous-Marin 3x1","Mini Sous-Marins 2x1"]
    property var orientation : ["VERTICAL", "HORIZONTAL"]
    ComboBox{
        id: choixBat
        Layout.minimumWidth: 600
        Layout.minimumHeight: 40
        Layout.fillWidth: true
        background: Rectangle{
            radius: 5
            color: "lightgrey"
            border.color: "black"
            border.width: 3
        }
        model: batTab
    }

    ComboBox{
        id : choixPosition
        Layout.minimumWidth: 600
        Layout.minimumHeight: 40
        Layout.fillWidth: true
        background: Rectangle{
            radius: 5
            color: "lightgrey"
            border.color: "black"
            border.width: 3
        }
        model: orientation
    }
}






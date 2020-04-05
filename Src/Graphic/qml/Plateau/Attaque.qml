import QtQuick 2.6
import QtQuick.Layouts 1.14
import QtQuick.Window 2.14
import QtQuick.Controls 2.14

//PLATEAU DE CASES
ColumnLayout{
    id:attaqueColumn
    Layout.fillWidth: true
    Layout.margins: 25
    Text{
        text: "ATTAQUE"
        font.pointSize: 18
    }
    SwipeView{
        id: attaqueStack
        clip: true
        interactive : false
        Repeater{
            model: 3
            AttDamier{}
        }
    }
    TabBar{
        id: attBar
        Layout.preferredWidth: attaqueStack.width
        TabButton{
            text: "Surface"
            font.pointSize: 18
            onClicked: attaqueStack.currentIndex = attBar.currentIndex
            background: Rectangle{
                radius: 5
                color: attBar.currentIndex === 0 ? "lightgrey":"black"
                border.color: attBar.currentIndex === 0 ? "black":"white"
                border.width: 3
            }
        }
        TabButton{
            text: "Milieu"
            font.pointSize: 18
            onClicked: attaqueStack.currentIndex = attBar.currentIndex
            background: Rectangle{
                radius: 5
                color: attBar.currentIndex === 1 ? "lightgrey":"black"
                border.color: attBar.currentIndex === 1 ? "black":"white"
                border.width: 3
            }
        }
        TabButton{
            text: "Profondeur"
            font.pointSize: 18
            onClicked: attaqueStack.currentIndex = attBar.currentIndex
            background: Rectangle{
                radius: 5
                color: attBar.currentIndex === 2 ? "lightgrey":"black"
                border.color: attBar.currentIndex === 2 ? "black":"white"
                border.width: 3
            }
        }
    }
}

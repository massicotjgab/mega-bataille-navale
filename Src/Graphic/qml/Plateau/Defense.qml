import QtQuick 2.6
import QtQuick.Layouts 1.14
import QtQuick.Window 2.14
import QtQuick.Controls 2.14

//PLATEAU DE CASES
ColumnLayout{
    id:defenseColumn
    Layout.fillWidth: true
    Layout.margins: 25
    Text{
        text: "DEFENSE"
        font.pointSize: 18
    }
    SwipeView{
        id: defenseStack
        clip: true
        interactive : false
        Repeater{
            model: 3
            Damier{}
        }
    }
    TabBar{
        id: defBar
        Layout.preferredWidth: defenseStack.width
        TabButton{
            text: "Surface"
            font.pointSize: 18
            onClicked: defenseStack.currentIndex = defBar.currentIndex
            background: Rectangle{
                radius: 5
                color: defBar.currentIndex == 0 ? "lightgrey":"black"
                border.color: defBar.currentIndex == 0 ? "black":"white"
                border.width: 3
            }
        }
        TabButton{
            text: "Millieu"
            font.pointSize: 18
            onClicked: defenseStack.currentIndex = defBar.currentIndex
            background: Rectangle{
                radius: 5
                color: defBar.currentIndex == 1 ? "lightgrey":"black"
                border.color: defBar.currentIndex == 1 ? "black":"white"
                border.width: 3
            }
        }
        TabButton{
            text: "Profondeur"
            font.pointSize: 18
            onClicked: defenseStack.currentIndex = defBar.currentIndex
            background: Rectangle{
                radius: 5
                color: defBar.currentIndex == 2 ? "lightgrey":"black"
                border.color: defBar.currentIndex == 2 ? "black":"white"
                border.width: 3
            }
        }
    }
}

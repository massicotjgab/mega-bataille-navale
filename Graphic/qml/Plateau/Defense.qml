import QtQuick 2.6
import QtQuick.Layouts 1.14
import QtQuick.Window 2.14
import QtQuick.Controls 2.14

//PLATEAU DE CASES
ColumnLayout{
    id:defenseColumn
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
        Layout.fillWidth: true
        TabButton{
            text: "Surface"
            font.pointSize: 18
            onClicked: defenseStack.currentIndex = 0
        }
        TabButton{
            text: "Millieu"
            font.pointSize: 18
            onClicked: defenseStack.currentIndex = 1
        }
        TabButton{
            text: "Profondeur"
            font.pointSize: 18
            onClicked: defenseStack.currentIndex = 2
        }
    }
}

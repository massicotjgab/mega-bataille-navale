import QtQuick 2.6
import QtQuick.Layouts 1.14
import QtQuick.Window 2.14
import QtQuick.Controls 2.14

//PLATEAU DE CASES
ColumnLayout{
    id:attaqueColumn
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
            Damier{}
        }
    }
    TabBar{
        Layout.fillWidth: true
        TabButton{
            text: "Surface"
            font.pointSize: 18
            onClicked: attaqueStack.currentIndex = 0
        }
        TabButton{
            text: "Millieu"
            font.pointSize: 18
            onClicked: attaqueStack.currentIndex = 1
        }
        TabButton{
            text: "Profondeur"
            font.pointSize: 18
            onClicked: attaqueStack.currentIndex = 2
        }
    }
}

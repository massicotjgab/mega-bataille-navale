import QtQuick 2.6
import QtQuick.Layouts 1.14
import QtQuick.Window 2.14
import QtQuick.Controls 2.14


ColumnLayout{//CONNECTION
    id: menuPres
    Layout.fillWidth: true

    Text{
        Layout.alignment: Qt.AlignHCenter
        text: "CHOIX DU MODE DE CONNEXION"
        font.pointSize: 18
        horizontalAlignment: horizontalCenter
    }

    TabBar{//CHOIX DU MODE DE CONNECTION
        id: modeConnectBar
        Layout.fillWidth: true
        Layout.margins: 0
        TabButton{
            text: "Héberger"
            font.pointSize: 18
            background: Rectangle{
                radius: 5
                color: modeConnectBar.currentIndex == 0 ? "lightgrey":"black"
                border.color: modeConnectBar.currentIndex == 0 ? "black":"white"
                border.width: 3
            }
            onClicked: modeConnectStack.currentIndex = modeConnectBar.currentIndex
        }
        TabButton{
            text: "En ligne"
            font.pointSize: 18
            background: Rectangle{
                radius: 5
                color: modeConnectBar.currentIndex == 1 ? "lightgrey":"black"
                border.color: modeConnectBar.currentIndex == 1 ? "black":"white"
                border.width: 3
            }
            onClicked: modeConnectStack.currentIndex = modeConnectBar.currentIndex
        }
    }

    SwipeView{//MODE DE CONNECTION
        id: modeConnectStack
        Layout.fillWidth: true
        Layout.margins : 50
        spacing: 10
        clip: true
        interactive : false

        ColumnLayout{//MODE HEBERGEUR
            Layout.fillWidth: true
            TextField{
                placeholderText: "Nom"
                Layout.minimumWidth: 500
                Layout.alignment: Qt.AlignHCenter
                maximumLength : 15
                font.pointSize: 18
            }
            TextField{
                placeholderText: "Adresse ip"
                Layout.minimumWidth: 500
                Layout.alignment: Qt.AlignHCenter
                maximumLength : 15
                font.pointSize: 18
            }
            TextField{
                placeholderText: "autre champ a definir"
                Layout.minimumWidth: 500
                Layout.alignment: Qt.AlignHCenter
                maximumLength : 15
                font.pointSize: 18
            }
        }

        ColumnLayout{//MODE HEBERGE
            Layout.fillWidth: true
            TextField{
                placeholderText: "Nom"
                Layout.minimumWidth: 500
                Layout.alignment: Qt.AlignHCenter
                maximumLength : 15
                font.pointSize: 18
            }
            TextField{
                placeholderText: "autre champ a definir"
                Layout.minimumWidth: 500
                Layout.alignment: Qt.AlignHCenter
                maximumLength : 15
                font.pointSize: 18
            }
            TextField{
                placeholderText: "autre champ a definir"
                Layout.minimumWidth: 500
                Layout.alignment: Qt.AlignHCenter
                maximumLength : 15
                font.pointSize: 18
            }
        }
    }
}

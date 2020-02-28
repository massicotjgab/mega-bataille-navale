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
                color: modeConnectBar.currentIndex === 0 ? "lightgrey":"black"
                border.color: modeConnectBar.currentIndex === 0 ? "black":"white"
                border.width: 3
            }
            onClicked: modeConnectStack.currentIndex = modeConnectBar.currentIndex
        }
        TabButton{
            text: "En ligne"
            font.pointSize: 18
            background: Rectangle{
                radius: 5
                color: modeConnectBar.currentIndex === 1 ? "lightgrey":"black"
                border.color: modeConnectBar.currentIndex === 1 ? "black":"white"
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
            id: hebergColumn
            TextField{
                placeholderText: "Nom"
                Layout.minimumWidth: 500
                Layout.alignment: Qt.AlignHCenter
                maximumLength : 15
                font.pointSize: 18
                onEditingFinished: {
                    gEngineUI.setName(text)
                }
            }
            TextField{
                placeholderText: "255.255.255.255"
                Layout.minimumWidth: 500
                Layout.alignment: Qt.AlignHCenter
                maximumLength : 15
                font.pointSize: 18
                enabled: false
            }
        }

        ColumnLayout{//MODE HEBERGE
            Layout.fillWidth: true
            TextField{
                id: nmChp
                placeholderText: "Nom"
                Layout.minimumWidth: 500
                Layout.alignment: Qt.AlignHCenter
                maximumLength : 15
                font.pointSize: 18
                focus: true
                onEditingFinished: {
                    gEngineUI.setName(text)
                }
                Keys.onReturnPressed: {
                    ipChp.focus = true
                }
            }
            TextField{
                id: ipChp
                placeholderText: "Adresse ip"
                Layout.minimumWidth: 500
                Layout.alignment: Qt.AlignHCenter
                maximumLength : 15
                font.pointSize: 18
                onEditingFinished: {
                    gEngineUI.setIp(text)
                }
                Keys.onReturnPressed: {
                    okBtn.focus = true
                }
            }
        }
    }
}

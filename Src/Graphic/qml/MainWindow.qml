import QtQuick 2.6
import QtQuick.Layouts 1.14
import QtQuick.Window 2.14
import QtQuick.Controls 2.14
import "Plateau"
import "Menu"
import "Connexion"

Window {
    visible: true
    title: "BATTLESHIP"
    minimumWidth : maingrid.implicitWidth
    minimumHeight : maingrid.implicitHeight + okBar.implicitHeight

    property var tabColor : ["lightblue", "blue", "darkblue"]
    ColumnLayout{
        anchors.fill : parent

        SwipeView{//GESTION DES FENETRES
            id: menuStack
            clip: true
            Layout.fillWidth: true
            Layout.fillHeight: true
            interactive: false

            //MENU CONNEXION
            Connexion{}

            //PLACEMENT DES BATEAUX
            RowLayout{
                id: placementgrid
                Layout.margins : 50
                spacing: 10
                LeftMenu{}
                Defense{}

            }

            //GRILLE GÉNÉRALE DE JEU
            RowLayout{
                id: maingrid
                Layout.margins : 50
                //anchors.fill : parent
                spacing: 10

                MainBoard{}
            }
        }


        RowLayout{
            id: okBar
            Layout.preferredWidth: menuStack.width

            RowLayout{}
            Button{
                visible: true
                id: clBtn
                text: "CANCEL"
                Layout.alignment: Qt.AlignLeft
                font.pointSize: 18
                background: Rectangle{
                    radius: 5
                    color: "lightgrey"
                    border.color: "black"
                    border.width: 3
                }
                onClicked: {
                    if (menuStack.currentIndex > 0){
                        menuStack.currentIndex = menuStack.currentIndex - 1
                    }
                }
            }
            Button{
                id: okBtn
                text: "OK"
                Layout.minimumWidth: clBtn.implicitWidth
                Layout.alignment: Qt.AlignLeft
                font.pointSize: 18
                background: Rectangle{
                    radius: 5
                    color: "lightgrey"
                    border.color: "black"
                    border.width: 3
                }
                onClicked:{
                    if (menuStack.currentIndex < 2){
                        menuStack.currentIndex = menuStack.currentIndex + 1
                    }
                }
            }
        }
    }
}

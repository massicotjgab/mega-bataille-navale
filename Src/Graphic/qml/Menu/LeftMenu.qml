import QtQuick 2.6
import QtQuick.Layouts 1.14
import QtQuick.Window 2.14
import QtQuick.Controls 2.14


//MENU

ColumnLayout{
    id: placeBoat
    Layout.margins: 25
    Layout.fillWidth: true

    Rectangle{
        id: menu
        Layout.minimumWidth: 100
        Layout.fillHeight : parent
        Layout.fillWidth : parent
        color: "lightgrey"
        border.width: 2
        Text{
            anchors.centerIn: parent
            text: "Bateaux"
            font.pointSize: 24
            focus: true
        }
    }
}





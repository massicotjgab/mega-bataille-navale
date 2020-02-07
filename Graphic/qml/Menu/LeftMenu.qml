import QtQuick 2.6
import QtQuick.Layouts 1.14
import QtQuick.Window 2.14
import QtQuick.Controls 2.14


//MENU
Rectangle{
    id: menu
    Layout.minimumWidth: 100
    Layout.fillHeight : true
    Layout.fillWidth : true
    color: "lightgrey"
    border.width: 2
    Text{
        anchors.centerIn: parent
        text: "MENU"
        font.pointSize: 24
        focus: true
    }
}

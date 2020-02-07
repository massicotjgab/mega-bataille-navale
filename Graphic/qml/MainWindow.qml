import QtQuick 2.6
import QtQuick.Layouts 1.14
import QtQuick.Window 2.14
import QtQuick.Controls 2.14
import "Menu"
import "Plateau"

Window {
    visible: true
    minimumWidth : maingrid.implicitWidth
    minimumHeight : maingrid.implicitHeight

    property var tabColor : ["lightblue", "blue", "darkblue"]

    //GRILLE GÉNÉRALE
    RowLayout{
        id: maingrid
        Layout.margins : 50
        anchors.fill : parent
        spacing: 10
        LeftMenu{}
        MainBoard{}
    }
}

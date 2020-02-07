import QtQuick 2.6
import QtQuick.Layouts 1.14
import QtQuick.Window 2.14
import QtQuick.Controls 2.14

//DAMIER
GridLayout {
    property string couleur : tabColor[index]
    id: damier
    Layout.fillWidth : true
    Layout.fillHeight : true
    columnSpacing : 0
    rowSpacing : 0
    columns: 15

    Repeater{
        model : 225
        OneCase{}
    }
}

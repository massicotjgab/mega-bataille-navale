import QtQuick 2.6
import QtQuick.Layouts 1.14
import QtQuick.Window 2.14
import QtQuick.Controls 2.14

//DAMIER
GridLayout {
    id: defDamier
    property string couleur : tabColor[index]
    property var tabDef: gEngineUI.updateDef()
    property int i: index
    Layout.fillWidth : true
    Layout.fillHeight : true
    columnSpacing : 0
    rowSpacing : 0
    columns: 15

    Repeater{
        id: defRepCase
        model : 225
        DefOneCase{}
    }
}

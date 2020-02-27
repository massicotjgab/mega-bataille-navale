import QtQuick 2.6
import QtQuick.Layouts 1.14
import QtQuick.Window 2.14
import QtQuick.Controls 2.14

ColumnLayout{
    property int indfinal : (defDamier.i) * (225) + index
    property string macouleur : defDamier.tabDef[indfinal] === 0 ? couleur:"black"
    Rectangle {
        id: defOneCase

        Layout.minimumWidth: 40
        Layout.minimumHeight: 40
        Layout.fillWidth : true
        Layout.fillHeight : true
        //color: couleur
        Text {
            text: indfinal
        }
        color: macouleur
        opacity: 0.8
        border.color: "black"
        border.width: 1
        radius: 1
    }
}

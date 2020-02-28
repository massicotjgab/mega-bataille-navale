import QtQuick 2.6
import QtQuick.Layouts 1.14
import QtQuick.Window 2.14
import QtQuick.Controls 2.14

ColumnLayout{
    id: attColLay
    property int indfinal : (attDamier.i) * (225) + index
    property string macouleur : attDamier.tabAtt[attColLay.indfinal] === 0 ? couleur:"black"
    Rectangle {
        id: attOneCase
        Layout.minimumWidth: 40
        Layout.minimumHeight: 40
        Layout.fillWidth : true
        Layout.fillHeight : true
        Text {
            text: attColLay.indfinal
        }
        color: attColLay.macouleur
        opacity: 0.8
        border.color: "black"
        border.width: 1
        radius: 1
    }
}

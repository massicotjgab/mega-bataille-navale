import QtQuick 2.6
import QtQuick.Layouts 1.14
import QtQuick.Window 2.14
import QtQuick.Controls 2.14

//GRILLE DES PLATEAUX
RowLayout{
    id: plateau
    //Layout.margins : 25
    Layout.fillHeight : true
    spacing : 5
    Attaque{}
    Defense{}
}

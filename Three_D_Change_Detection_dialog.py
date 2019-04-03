# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ThreeDChangeDetectionDialog
                                 A QGIS plugin
 Tool for change detection between temporally different DEMs (rasters) of the same location  
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-02-25
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Jordan Bates, Muhammad Hasan Mustafa, Tanmoy Chakraborty
        email                : m20180811@novaims.unl.pt , m20180796@novaims.unl.pt , m20180804@novaims.unl.pt
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt5 import uic
from PyQt5 import QtWidgets

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'Three_D_Change_Detection_dialog_base.ui'))


class ThreeDChangeDetectionDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ThreeDChangeDetectionDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

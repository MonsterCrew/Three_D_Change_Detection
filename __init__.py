# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ThreeDChangeDetection
                                 A QGIS plugin
 Tool for change detection between temporally different DEMs (rasters) of the same location  
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-02-25
        copyright            : (C) 2019 by Jordan Bates, Muhammad Hasan Mustafa, Tanmoy Chakraborty
        email                : m20180811@novaims.unl.pt , m20180796@novaims.unl.pt , m20180804@novaims.unl.pt
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ThreeDChangeDetection class from file ThreeDChangeDetection.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Three_D_Change_Detection import ThreeDChangeDetection
    return ThreeDChangeDetection(iface)

# -*- coding: utf-8 -*-

"""
/***************************************************************************
 EstimapRecreation
                                 A QGIS plugin
 Ecosystem services mapping at
European scale (ESTIMAP)- Recreation
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2019-02-08
        copyright            : (C) 2019 by NATCAPES
        email                : nik@nikosalexandris.net
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

__author__ = 'NATCAPES'
__date__ = '2019-02-08'
__copyright__ = '(C) 2019 by NATCAPES'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os

from qgis.core import Qgis, QgsProcessingProvider, QgsMessageLog
from processing.algs.grass7.Grass7AlgorithmProvider import Grass7AlgorithmProvider
from processing.algs.grass7.Grass7Algorithm import Grass7Algorithm


class EstimapRecreationProvider(Grass7AlgorithmProvider):

    descriptionFolder = os.path.join(os.path.dirname(__file__), 'description')

    def id(self):
        """
        Returns the unique provider id, used for identifying the provider. This
        string should be a unique, short, character only string, eg "qgis" or
        "gdal". This string should not be localised.
        """
        return 'NATCAPES'

    def name(self):
        """
        Returns the provider name, which is used to describe the provider
        within the GUI.

        This string should be short (e.g. "Lastools") and localised.
        """
        return self.tr('NATCAPES')

    def longName(self):
        """
        Returns the a longer version of the provider name, which can include
        extra details such as version numbers. E.g. "Lastools LIDAR tools
        (version 2.2.1)". This string should be localised. The default
        implementation returns the same string as name().
        """
        return self.name()

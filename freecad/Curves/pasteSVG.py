import xml.sax
import importSVG
import os
import FreeCAD
import FreeCADGui
from PySide import QtGui
from freecad.Curves import ICONPATH

TOOL_ICON = os.path.join( ICONPATH, 'svg_rv3.svg')

class pasteSVG:
    def Activated(self):
        cb = QtGui.QApplication.clipboard()
        t=cb.text()

        if t[0:5] == '<?xml':
            h = importSVG.svgHandler()
            doc = FreeCAD.ActiveDocument
            if not doc:
                doc = FreeCAD.newDocument("SvgImport")
            h.doc = doc
            xml.sax.parseString(t,h)
            doc.recompute()
            FreeCADGui.SendMsgToActiveView("ViewFit")
        else:
            FreeCAD.Console.PrintError('Invalid clipboard content.\n')
        
    #def IsActive(self):
        #return(True)

    def GetResources(self):
        return {'Pixmap' : TOOL_ICON, 'MenuText': 'paste SVG', 'ToolTip': 'Pastes the SVG content of the clipboard'}

FreeCADGui.addCommand('pasteSVG', pasteSVG())

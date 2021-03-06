# coding=utf-8
# Copyright(c) 2017, Oleg Rezvov
# @PRSPKT, http://prspkt.ru
__author__ = "ООО АБ Проспект"

# region import
import clr

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# Import Element wrapper extension methods
clr.AddReference("RevitNodes")
import Revit

clr.ImportExtensions(Revit.Elements)

# Import geometry conversion extension methods
clr.ImportExtensions(Revit.GeometryConversion)

# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application

# Import RevitAPI
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

import System
from System import Array
from System.Collections.Generic import *

import sys

pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)

view = UnwrapElement(IN[0])
txt = [n for n in IN[1]]
baseVec = XYZ(1, 0, 0)
upVec = XYZ(0, 1, 0)
convert = 0.00328084

point = [XYZ(i.X*convert, i.Y*convert, i.Z) for i in IN[2]]

textNoteTypes = FilteredElementCollector(doc).OfClass(TextNoteType).ToElements()
bip = BuiltInParameter.ALL_MODEL_TYPE_NAME
typeName = IN[3]
textType = []
textTypeChosen = ""

for i in textNoteTypes:
	if i.get_Parameter(bip).AsString() == typeName:
		textType.append(i)
	else:
		message = "Text Type with specified name \ndoes not exists. Please specify a \ndifferent name."
if len(textType) != 0:
	textTypeChosen = textType[0]
else:
	textTypeChosen = '\n'.join('{:^35}'.format(s) for s in message.split('\n'))

try:
    errorReport = None
    TransactionManager.Instance.EnsureInTransaction(doc)

    collector = FilteredElementCollector(doc, view.Id)
    text_elements = collector.OfCategory(BuiltInCategory.OST_TextNotes)

    for element in text_elements:
        element_id = UnwrapElement(element).Id
        doc.Delete(element_id)

    for i, k in enumerate(point):
        len = (txt[i].Length)* 0.0066
        opts = TextNoteOptions(textTypeChosen.Id)
        opts.HorizontalAlignment = HorizontalTextAlignment.Center
        note = TextNote.Create(doc, view.Id, k, len, txt[i], opts)#TextAlignFlags.TEF_ALIGN_CENTER)

    TransactionManager.Instance.TransactionTaskDone()


#OUT = note
except:  # if error accurs anywhere in the process catch it
    import traceback

    errorReport = traceback.format_exc()  # End Transaction
    TransactionManager.Instance.TransactionTaskDone()

# Assign your output to the OUT variable
if errorReport == None:
    OUT = "OK"
else:
    OUT = errorReport

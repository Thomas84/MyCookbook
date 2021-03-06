# Copyright(c) 2016, Konrad K Sobon
# @arch_laboratory, http://archi-lab.net

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

#The inputs to this node will be stored as a list in the IN variable.
dataEnteringNode = IN

def ProcessList(_func, _list):
    return map( lambda x: ProcessList(_func, x) if type(x)==list else _func(x), _list )

def ProcessListArg(_func, _list, _arg):
    return map( lambda x: ProcessListArg(_func, x, _arg) if type(x)==list else _func(x, _arg), _list )

def ProcessParallelLists(_func, *lists):
    return map( lambda *xs: ProcessParallelLists(_func, *xs) if all(type(x) is list for x in xs) else _func(*xs), *lists )

def Unwrap(item):
    return UnwrapElement(item)

# Convert single element to list
def ToList(x):
    if hasattr(x,'__iter__'):
        return x
    else :
        return [x]
wallList = []
otherWalls = []
lvl = IN[1].Name
SearchStr=IN[2]
# Start Transaction
# TransactionManager.Instance.EnsureInTransaction(doc)
# Regenerate
# TransactionManager.Instance.ForceCloseTransaction()

try:
    errorReport = None
    walls = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()
    for wall in walls:
        wType = wall.Name
        wLevel = wall.LookupParameter("Базовая зависимость")
        if wType and lvl == wLevel.AsValueString():
            if SearchStr in wType:
                wallList.append(wall)
            else:
                otherWalls.append(wall)
        
    #wallList.append(wall for wall in walls)

except:
    # if error accurs anywhere in the process catch it
    import traceback
    errorReport = traceback.format_exc()

# End Transaction
TransactionManager.Instance.TransactionTaskDone()


#Assign your output to the OUT variable
if errorReport == None:
    OUT = wallList, otherWalls
else:
    OUT = errorReport
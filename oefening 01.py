import rhinoscriptsyntax as rs
import Rhino
import math


#www.github.com/mcneel/rhinopyton/blob/master/scripts/rhinoscript/mesh.py

mesh_id = rs.GetObject("Selecteer je mesh")
if(mesh_id != None):
    mesh = rs.coercemesh(mesh_id)
    polygons = rs.MeshFaces(mesh,True)
    print polygons
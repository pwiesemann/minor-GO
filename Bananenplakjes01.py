import rhinoscriptsyntax as rs
import Rhino
import math

#www.github.com/mcneel/rhinopyton/blob/master/scripts/rhinoscript/mesh.py

mesh_id = rs.GetObject("Selecteer een mesh")
if(mesh_id != None):
    mesh = rs.coercemesh(mesh_id)
    polygons = rs.MeshFaces(mesh,True)
    vertices = rs.MeshVertices(mesh) 
    mylist = [vertices]
    xmin = min(mylist)
    print polygons
    print len(polygons)
    
    print min(vertices)
    print max(vertices)

if(mesh_id != None):
    point0 = min(vertices)
    if point0:
         point1 = max(vertices)
         if point1:
             rs.AddCutPlane(mesh_id, point0, point1)

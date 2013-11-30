import rhinoscriptsyntax as rs
import Rhino
import math

#www.github.com/mcneel/rhinopyton/blob/master/scripts/rhinoscript/mesh.py
#phyton tutorial

mesh_id = rs.GetObject("Selecteer een mesh")
if(mesh_id != None):
    mesh = rs.coercemesh(mesh_id)
    polygons = rs.MeshFaces(mesh,True)
    vertices = rs.MeshVertices(mesh) 

    print vertices
    print len(polygons)

    print min(vertices)
    print max(vertices)
  
minVertex = [vertices[0][0], vertices[0][1], vertices[0][2]]
maxVertex = [vertices[0][0], vertices[0][1], vertices[0][2]]
for vertex in vertices:
    if vertex[0] < minVertex[0]:
        minVertex[0] = vertex[0]
    elif vertex[0] > maxVertex[0]:
        maxVertex[0] = vertex[0]
    if vertex[1] < minVertex[1]:
        minVertex[1] = vertex[1]
    elif vertex[1] > maxVertex[1]:
        maxVertex[1] = vertex[1]
    if vertex[2] < minVertex[2]:
        minVertex[2] = vertex[2]
    elif vertex[2] > maxVertex[2]:
        maxVertex[2] = vertex[2]

print minVertex 
print maxVertex
        
if(mesh_id != None):
    rs.AddCutPlane([mesh_id], (minVertex[0],minVertex[1],minVertex[2]), (maxVertex[0],minVertex[1],maxVertex[2]))         
    rs.GetPoint("blaat")
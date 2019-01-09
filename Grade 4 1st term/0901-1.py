import rhinoscriptsyntax as rs
import math
import random
import Rhino.Geometry as rg

result=rs.GetCurveObject()
curveid=result[0]
rail=rs.GetCurveObject()

def TransformProfile(object,pt1,pt2):
    normal=rs.VectorSubtract(pt1,pt2)
    normal=rs.VectorUnitize(normal)
    
    plane=rs.PlaneFromNormal(pt1,normal)
    
    transformation=rs.XformRotation1((rs.WorldXYPlane),normal)
    profiletras=rs.TransformObject(object,transformation,True)
    
    
#pt1=rs.CurveStartPoint
#pt2=rs.CurveEndPoint

pt1=rs.GetPoint()
pt2=rs.GetPoint()
rs.MoveObject(curveid,rs.VectorCreate(pt1,pt2))
print rs.VectorCreate(pt1,pt2)

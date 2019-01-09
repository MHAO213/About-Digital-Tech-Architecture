import rhinoscriptsyntax as rs
import math
import random

r=1000
circle=rs.AddCircle((0,0,0),r)
maxgeneration=7

def splitcircle(circle,parameter):
    points=[]
    curves=rs.SplitCurve(circle, parameter, delete_input=True)
    for cur in curves:
        points.append(rs.CurveEndPoint(cur))
    return points

    
def draw(center,maxrad,minrad,index):
    torus=rs.AddTorus(center,maxrad,minrad)
    materialIndex=rs.AddMaterialToObject(torus)
    rs.MaterialColor(materialIndex,(random.uniform(0,255),random.uniform(0,255),150+index*5))
#    rs.MaterialShine(materialIndex,index*5 )
    rs.MaterialTransparency(materialIndex, random.uniform(0,0.1*index))
    
def circles(center,circle,radius,generation):
    cir=[]
    index=maxgeneration-generation
    if generation==0:
        draw(center,radius,index*10,index)
    if generation<maxgeneration:
        domain = rs.CurveDomain(circle)
        parameter = domain[1] /2 
        points=splitcircle(circle,parameter)
        for p in points:
            temprand=random.uniform(0,0)
            cent=rs.RotateObject(rs.MoveObject(p,(0,0,generation*10)),center,temprand )
            temp=rs.RotateObject((rs.AddCircle(cent,radius)),center,temprand )
            circles(cent,temp,radius*0.75,generation+1)
            draw(cent,radius,index*10,index)
            
#            srf=rs.AddPlanarMesh(temp)
#            rs.ObjectColor(temp,(random.uniform(0,255),random.uniform(0,255),255-10*generation)
#            materialIndex=rs.AddMaterialToObject(srf)
#            rs.MaterialColor(materialIndex,(random.uniform(0,255),random.uniform(0,255),255))
#           rs.MaterialShine(materialIndex,generation*5 )
#           rs.MaterialTransparency(materialIndex, random.uniform(0,0.1*generation))


circles((0,0,0),circle,r,0)
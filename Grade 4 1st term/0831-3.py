import rhinoscriptsyntax as rs
import random

def pointtocone(origin,direction,mindis,maxdis,maxangle):
    vectwig=rs.VectorUnitize(direction)
    vectwig=rs.VectorScale(vectwig,random.uniform(mindis,maxdis))
    mutationplane=rs.PlaneFromNormal((0,0,0),vectwig)
    vectwig=rs.VectorRotate(vectwig,random.random()*maxangle,mutationplane[1])
    vectwig=rs.VectorRotate(vectwig,random.random()*360,direction)
    return rs.PointAdd(origin,vectwig)

def neuralGrow(poistion,angle,length,maxangledeviation,generation,maxgeneration):
    goal=rs.Polar(poistion,angle,length)
    rs.AddCone(goal,poistion,11-generation)
    angle1=angle+random.uniform(-maxangledeviation,-5)
    angle2=angle+random.uniform(5,maxangledeviation)
    if generation<maxgeneration:
        
        neuralGrow(goal,angle1,length,maxangledeviation,generation+1,maxgeneration)
        neuralGrow(goal,angle2,length,maxangledeviation,generation+1,maxgeneration)
        
        
poistion=(0,0,0)
angle=90
length=20
maxangledeviation=20

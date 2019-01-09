import rhinoscriptsyntax as rs
import random


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

for i in range(12):
#    x=random.uniform(200,550)
    x=i*150
    y=random.uniform(-250,250)
    neuralGrow((x,0,0),angle,length,maxangledeviation,0,i)
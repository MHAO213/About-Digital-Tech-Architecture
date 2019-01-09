import rhinoscriptsyntax as rs
import random

def randomwalk(poistion,angle,length,maxangledeviation,amountsteps):
#    poistion=(0,0,0)
    
#    angle=90
#    length=90
 #   maxangledeviation=30
 #   amountsteps=1000
    
    for i in range(amountsteps):
        goal=rs.Polar(poistion,angle,length)
        rs.AddLine(poistion,goal)
        poistion=goal
        angle=angle+(random.uniform(-maxangledeviation,maxangledeviation))
       
rs.EnableRedraw(False)
for i in range(100):
    randomwalk((0,0,0),3,10,5,100)

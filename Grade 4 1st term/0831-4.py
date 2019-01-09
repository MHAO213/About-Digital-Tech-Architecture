import rhinoscriptsyntax as rs
import math
import random
import Rhino.Geometry as rg


for x in range(100):
    for y in range(x):
        for z in range(y):
            rs.AddCone((x**2,y**2,z**2),)

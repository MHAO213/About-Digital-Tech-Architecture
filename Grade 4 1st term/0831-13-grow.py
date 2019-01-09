import rhinoscriptsyntax as rs
import math
import random
import Rhino.Geometry as rg

def draw(pipe,index):
    materialIndex=rs.AddMaterialToObject(pipe)
    rs.MaterialColor(materialIndex,(random.uniform(0,255),random.uniform(0,255),150+index*5))
    rs.MaterialShine(materialIndex,index*0.1 )
    rs.MaterialTransparency(materialIndex, random.uniform(0,0.15*index))

def AddLine(start,ends,radius,index):
    line=rs.AddLine(start,ends)
    pipe=rs.AddPipe(line,0,radius)
    draw(pipe,index)
    return line

def RecursiveLine(line,generation):
    if generation>0:
        vector=rs.VectorCreate(rs.CurveStartPoint(line),rs.CurveEndPoint(line))
        vector=rs.VectorRotate(vector,90,(0,0,1))
        hight=rs.VectorCreate((0,0,0),(0,0,generation*5))
        points=rs.DivideCurve(line,random.uniform(5,10))
        for p in points:
            start=rg.Point3d.Add(p,hight)
            if random.uniform(0,1):
                vector=-vector
            vector=vector*0.8
#            ends=rs.MoveObject(p,vector)
            vectorh=rs.VectorRotate(vector,90,rs.VectorCreate(rs.CurveStartPoint(line),rs.CurveEndPoint(line)))
            highpoints=rg.Point3d.Add(start,vectorh)
            AddLine(start,highpoints,generation*5,generation)
            start=highpoints
            ends=rg.Point3d.Add(start,vector)
            newline=AddLine(start,ends,generation*5,generation)
            RecursiveLine(newline,generation-1)

newline=AddLine((-1000,0,0),(1000,0,0),25,5)
RecursiveLine(newline,4)
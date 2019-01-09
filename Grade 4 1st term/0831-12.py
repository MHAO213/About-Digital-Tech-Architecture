import rhinoscriptsyntax as rs
import math
import random


def SplitRecursive(surface,splitValue,direction,generation,index):
    if generation >0:
        domain_u = rs.SurfaceDomain(surface, direction)
        domainRange=domain_u[1]-domain_u[0]
        split = domainRange * splitValue+domain_u[0]
        surface1=rs.TrimSurface(surface,direction,(split,domain_u[1]))
        surface2=rs.TrimSurface(surface,direction,(domain_u[0],split))
        rs.DeleteObject(surface)
        SplitRecursive(surface1,random.uniform(0.4,0.6),0,generation-1,index)
        SplitRecursive(surface2,random.uniform(0.4,0.6),1,generation-1,index)
    else:
        materialIndex=rs.AddMaterialToObject(surface)
        rs.MaterialColor(materialIndex,(random.uniform(0,255),random.uniform(0,255),150+index*5))
        rs.MaterialShine(materialIndex,index*0.1 )
        rs.MaterialTransparency(materialIndex, random.uniform(0,0.15*index))

def ExplodeBox(hulls,index):
    if rs.IsBrep(hulls):
        faces=rs.ExplodePolysurfaces(hulls,True)
        for face in faces:
            SplitRecursive(face,0.5,0,3,index)

def RecursiveBox(polysurface,generation):
    surfaces=rs.ExplodePolysurfaces(polysurface,True)
    for surface in surfaces:
        
        if generation>0:
            rs.RebuildSurface(surface,pointcount=(5, 5))
            domainU=rs.SurfaceDomain(surface,0)
            domainV=rs.SurfaceDomain(surface,1)
            randomU=random.uniform(domainU[0],domainU[1])
            randomV=random.uniform(domainV[0],domainV[1])
            point=rs.EvaluateSurface(surface,randomU,randomV)
            hulls=drawBoxByCenter(point[0],point[1],point[2],generation*3,generation*3,generation*6)
            RecursiveBox(hulls,generation-1)
#            ExplodeBox(hulls)
        SplitRecursive(surface,0.5,0,3,generation)

def drawBoxByCenter(x,y,z,dx,dy,dz):
    box=rs.AddBox(((x,y,z),(x+dx,y,z),(x+dx,y+dy,z),(x,y+dy,z),(x,y,z+dz),(x+dx,y,z+dz),(x+dx,y+dy,z+dz),(x,y+dy,z+dz)))
    rs.MoveObject(box,(-dx/2,-dy/2,-dz/2))
    return box

hull=drawBoxByCenter(0,0,0,10,10,10)
RecursiveBox(hull,3)

import rhinoscriptsyntax as rs
import math
import random

    
def NewSphere(center,radius):
    newsphere=rs.AddSphere(center,radius)
    newsphere=rs.RebuildSurface(newsphere,pointcount=(6,6))
    rs.n
    materialIndex=rs.AddMaterialToObject(newsphere)
    rs.MaterialColor(materialIndex,(random.uniform(0,50),random.uniform(0,50),random.uniform(50,255)))
    
def RecursiveSphere(surface,generation):
    if generation>0:
        domainU=rs.SurfaceDomain(surface,0)
        domainV=rs.SurfaceDomain(surface,1)
        randomU1=random.uniform(domainU[0],domainU[1])
        randomV1=random.uniform(domainV[0],domainV[1])
        randomU2=random.uniform(domainU[0],domainU[1])
        randomV2=random.uniform(domainV[0],domainV[1])
        randomU3=random.uniform(domainU[0],domainU[1])
        randomV3=random.uniform(domainV[0],domainV[1])
        point1=rs.EvaluateSurface(surface,randomU1,randomV1)
        point2=rs.EvaluateSurface(surface,randomU2,randomV2)
        point3=rs.EvaluateSurface(surface,randomU3,randomV3)
        newsphere1=NewSphere(point,1000/(4-generation))
        newsphere2=NewSphere(point,1000/(4-generation))
        newsphere3=NewSphere(point,1000/(4-generation))
        RecursiveSphere(newsphere1,generation-1)
        RecursiveSphere(newsphere2,generation-1)
        RecursiveSphere(newsphere3,generation-1)


newsphere=NewSphere((0,0,0),1000)
RecursiveSphere(newsphere,4)

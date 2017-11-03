import random as r

points = []
corners = []

def getRandomPt():
    numPoints = len(corners)
    rand = r.randint(0, numPoints-1)
    return corners[rand]

def createRandomPt(dim):
    posx = r.random()*dim
    posy = r.random()*dim
    return p(posx,posy)
    

def initR(start, dim , numIters):
    points.extend([start.p1,start.p2, start.p3])
    corners.extend([start.p1,start.p2, start.p3])
    po = createRandomPt(dim)
    points.append(po)
    for i in range(0, numIters):
        aux = getRandomPt()
        po = po.mid(aux)
        points.append(po)
    return points

if(__name__ != "__main__"):
    from mathe.structures import p,t

    


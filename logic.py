from structures import p,t
tri = []

def getChild(a):
    t1 = t(a.p1, a.p1.mid(a.p2), a.p1.mid(a.p3))
    t2 = t(a.p1.mid(a.p2),a.p2,  a.p2.mid(a.p3))
    t3 = t(a.p1.mid(a.p3), a.p2.mid(a.p3), a.p3)
    return [t1, t2, t3]

def init(start, n=8):
    numIters = int( 1/3 * (4 ** (n+1) -1))
    print("Total number of triangles = {}.".format(numIters))
    tri.append(start)
    for i in range (numIters):
        aux = tri.pop(0)
        tri.extend(getChild(aux))
    return tri

import math as m
from plotp import plot
from structures import p,t
from logic import init

if(__name__ == "__main__"):
    l = 10000
    t1 = t(p(0,0), p(l/2, l*m.sin(60*m.pi/180)), p(l,0))
    t1.show()
    tree = init(t1)
    plot(tree, l)

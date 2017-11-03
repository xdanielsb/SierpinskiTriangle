import math as m
from mathe.plotp import plot
from mathe.structures import p,t
from mathe.logic import init
from randoe.logicr import initR

if(__name__ == "__main__"):
    l = 10000
    t1 = t(p(0,0), p(l/2, l*m.sin(60*m.pi/180)), p(l,0))
    #Matematical Process
    #tree = init(t1)
    #plot(tree, l)
    #Random Process
    tree = initR(t1, l, 100000)
    plot(tree, l)
    

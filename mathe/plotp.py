import numpy as np
import matplotlib.pyplot as plt
from mathe.structures import p,t

def plot(tri, dim):
    x, y = [], []
    if(type(tri[0]) == t):
        for tt in tri:
            points = tt.get()
            for  po in points:
                x.append(po.x)
                y.append(po.y)
                
    if(type(tri[0]) == p):
        for po in tri:
            x.append(po.x)
            y.append(po.y)

    if 0 < len(x):
        plt.plot(x, y, 'b.')
        plt.axis([0, dim, 0, dim])
        plt.show()

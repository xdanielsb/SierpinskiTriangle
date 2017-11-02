import numpy as np
import matplotlib.pyplot as plt

def plot(tri, l):
    x, y = [], []
    for tt in tri:
        points = tt.get()
        for  p in points:
            x.append(p.x)
            y.append(p.y)
    plt.plot(x, y, 'b.')
    plt.axis([0, l, 0, l])
    plt.show()

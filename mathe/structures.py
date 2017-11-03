class p:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def mid(self, p2):
        return p( (self.x+p2.x)/2, (self.y+p2.y)/2)
    def show(self):
        print("Point = ({},{})".format(self.x, self.y))
   
class t:
    def __init__(self, p1,p2,p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def show(self):
        print("Triangle ({}, {}), ({}, {}), ({}, {})".format(self.p1.x, self.p1.y, self.p2.x, self.p2.y, self.p3.x, self.p3.y))
    def get(self):
        return [self.p1, self.p2, self.p3]

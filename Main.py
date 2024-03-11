import math

class renderer():
    object_array = []
    def __init__(self, _x =600, _y = 400, _g = 1):
        self.x, self.y = _x, _y
        self.g = _g
    
    def new_frame(self):
        objects = []
        for object in self.object_array:
            if object[1] < self.y-object[2]:
                #o = object[3]*math.cos(object[4])
                object[3] = -((self.g+object[3]*math.sin(object[4])))#**2+(object[3]*math.cos(object[4]))**2)**0.5
                #object[4] = math.asin(o/object[3])
                #print(o)
                object[1] += object[3]*math.sin(object[4])
                #object[0] += object[3]*math.cos(object[4])
            else:
                object[1] = self.y-object[2]
            objects.append(object)
        return objects
        

class circle(renderer):
    def __init__(self, _r = 10, _x = 100, _y = 100, _v = 0, _a = 1.5*math.pi):
        super().object_array.append([_x, _y, _r, _v, _a])

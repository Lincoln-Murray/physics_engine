import math

class renderer():
    object_array = []
    def __init__(self, _x =600, _y = 400, _g = 9.8):
        self.x, self.y = _x, _y
        self.g = _g
    
    def new_frame(self):
        for object in self.object_array:
            if object[0] > self.x:
                object[3] += self.g
                object[0] += object[3]
            else:
                object[0] = self.x-object[2]
            return object
        

class circle(renderer):
    def __init__(self, _r = 5, _x = 10, _y = 10, _v = 0, _a = 0):
        super().object_array.append([_x, _y, _r, _v, _a])

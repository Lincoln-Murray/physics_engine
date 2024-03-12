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
                object[4] += self.g
                object[0] += object[3]
                object[1] += object[4]
                if object[1] < self.y-object[2]:
                    pass
                else:
                    object[1] = self.y-object[2]
            else:
                object[1] = self.y-object[2]
            objects.append(object)
        return objects
        

class circle(renderer):
    def __init__(self, _r = 10, _x = 100, _y = 100, _v = 10, _a = 0.5*math.pi):
        _vy = _v*math.cos(_a)
        _vx = _v*math.sin(_a)
        super().object_array.append([_x, _y, _r, _vx, _vy, _a])

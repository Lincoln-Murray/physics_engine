import math

class renderer():
    object_array = []
    def __init__(self, _x =600, _y = 400, _g = 9.8, _pixels_per_metre = 10):
        self.x, self.y = _x, _y
        self.g = _g
        self.ppm = _pixels_per_metre
    
    def new_frame(self, _frame_time):
        objects = []
        iterations_per_frame = 1/_frame_time
        for object in self.object_array:
            if object[4] < self.y-object[-1]:
                object[2] += self.ppm*self.g**(1/iterations_per_frame)
                if abs(object[1]) == object[1]:
                    object[3] += self.ppm*abs(object[1])**(1/iterations_per_frame)
                else:
                    object[3] -= self.ppm*abs(object[1])**(1/iterations_per_frame)
                object[4] += self.ppm*object[2]**(1/iterations_per_frame)
            if object[4] >= self.y-object[-1]:
                object[4] = self.y-object[-1]
            if object[3] > self.x-object[-1] or object[3] < object[-1] :
                object[1] = -object[3]
            objects.append(object)
        return objects
        
    #super().object_array.append([_x, _y, _r, _vx, _vy, _a])
class circle():
    def __init__(self, parent, _r = 10, _x = 400, _y = 100, _v = 30, _a = 0.5*math.pi):
        _vy = _v*math.cos(_a)
        _vx = _v*math.sin(_a)
        parent.object_array.append(['circle', _vx, _vy, _x, _y, _r])

class rectangle():
    def __init__(self, parent, _x1 = 400, _y1 = 100, _x2 = 410, _y2 = 110, _v = 30, _a = 0.5*math.pi):
        _vy = _v*math.cos(_a)
        _vx = _v*math.sin(_a)
        parent.object_array.append(['rectangle', _vx, _vy, _x1, _y1, _x2, _y2])

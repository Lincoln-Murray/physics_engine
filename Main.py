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
            if object[1] < self.y-object[2]:
                object[4] += self.ppm*self.g**(1/iterations_per_frame)
                if abs(object[3]) == object[3]:
                    object[0] += self.ppm*abs(object[3])**(1/iterations_per_frame)
                else:
                    object[0] -= self.ppm*abs(object[3])**(1/iterations_per_frame)
                object[1] += self.ppm*object[4]**(1/iterations_per_frame)
            if object[1] >= self.y-object[2]:
                object[1] = self.y-object[2]
            if object[0] > self.x-object[2] or object[0] < object[2] :
                object[3] = -object[3]
            objects.append(object)
        return objects
        

class circle(renderer):
    def __init__(self, _r = 10, _x = 400, _y = 100, _v = 30, _a = 0.5*math.pi):
        _vy = _v*math.cos(_a)
        _vx = _v*math.sin(_a)
        super().object_array.append([_x, _y, _r, _vx, _vy, _a])

# 2D physics engine

## Table of Contents

+ [About](#about)
+ [Getting Started](#getting_started)
+ [Usage](#usage)

## <a name = "about">About </a>

 This is a small project I decided to work on because I was bored and I wanted a better understanding of implementing physics with the end goal of porting/taking my knowledge to my graphics library.

 Happy Coding!

## <a name = "getting_started">Getting Started </a>

To get this library running download the Main.py file and put it into your projects folder, then you need to just import it like you would any other Python3 library(by whatever the filename is). That's it, then you can create instances of the classes to use the library/module(whatever you want to call it).

## <a name = "usage">Usage </a>

### Initiating the library:

To initiate the engine create an instance:

```
Import Main  
screen_width = 1920  
screen_height = 1080  
gravity = 1 
pixel_metre_ratio = 10
decay_rate = 0.95  
engine_example = Main.renderer(screen_width, screen_height, gravity, pixel_metre_ratio, decay rate)
```

Then add an object(in this case a circle):

```
x, y = 100,100  
velocity, angle_radians = 30, 0.5*math.pi  
circle = Main.circle(x, y, velocity, angle_radians)  
```


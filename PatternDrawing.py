import turtle
 
 
class FractalPolygonDrawer:
 
    def __init__(self, sides=4, length=300, depth=3):
        self.sides = sides
        self.length = length
        self.depth = depth
 
        self.screen = turtle.Screen()
        self.screen.title("Fractal Polygon Drawer")
        self.screen.setup(width=800, height=800)
 
        self.t = turtle.Turtle()
        self.t.speed(0)  
        self.t.hideturtle()  
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
    
    def draw_fractal_edge(self, length, depth):
     
        if depth == 0:
            self.t.forward(length)
            return
 
        segment_length = length / 3.0
 
       
        self.draw_fractal_edge(segment_length, depth - 1)
        self.t.right(60)
        self.draw_fractal_edge(segment_length, depth - 1)
        self.t.left(120)
        self.draw_fractal_edge(segment_length, depth - 1)
        self.t.right(60)
        self.draw_fractal_edge(segment_length, depth - 1)
        
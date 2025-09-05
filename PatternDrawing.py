"""
Question 3: Recursive Fractal Polygon Drawer
=============================================================================
This program uses recursion to draw fractal polygons with turtle graphics.
The user provides:
- Number of sides
- Side length
- Recursion depth
"""

import turtle
 
 
class FractalPolygonDrawer:
    """Class to handle fractal polygon drawing with turtle graphics."""
 
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
        """
        Recursively draw one edge of the fractal polygon.

        Args:
            length (float): Length of the edge.
            depth (int): Recursion depth.
        """
    

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

    def draw_fractal_polygon(self):
        """
        Draw the full fractal polygon by drawing each side with fractal edges.
        """
        angle = 360.0 / self.sides
        for _ in range(self.sides):
            self.draw_fractal_edge(self.length, self.depth)
            self.t.right(angle)

    def position_turtle(self):
        """
        Position the turtle at the starting point for drawing.
        """
        self.t.penup()
        self.t.goto(-self.length / 2, self.length / 2)
        self.t.pendown()

    def run(self):
        """
        Start the fractal drawing process.
        """
        self.position_turtle()




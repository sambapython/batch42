import turtle as t
class shape(object):
    def __init__(self,color="black",size=1):
        self.color=color
        self.size=size
class dot(shape):
    def __init__(self,x,y,color="black",size=1):
        self.x=x
        self.y=y
        shape.__init__(self,color,size)
class snow_man_parts(shape):
    def __init__(self,color="black",size=1):
        shape.__init__(self,color,size)
    def dot(self,x,y):
        t.up()
        t.goto(x,y)
        t.dot()
        
    def snowmansface(self,x,y):
        t.up()
        t.goto(x + 15,y)
        t.dot()
        t.goto(x - 15,y)
        t.dot()
        t.goto(x -15,y -25)
        t.down()
        t.forward(30)
        t.up()
    def snowmansarm(self,x,y,length,heading):
        t.up()
        t.goto(x,y)
        t.setheading(heading)
        t.down()
        t.forward(length)
        t.setheading(heading + 20)
        t.forward(20)
        t.up()
        t.back(20)
        t.down()
        t.setheading(heading - 20)
        t.forward(20)
        t.up()
        t.home()


class line(shape):
    def __init__(self,x1, y1, x2, y2,color='black',size=1):
        self.x1=x1
        self.y1=y1
        self.y2=y2
        self.x2=x2
        shape.__init__(self,color,size)
    def draw(self):
          t.penup()
          t.goto (self.x1, self.y1)
          t.pendown()
          t.goto (self.x2, self.y2)
          t.penup()
    def __str__(self):
        return "line"
class circle(shape):
    def __init__(self,x,y,r,color="green",fill=0,size=1):
          # draw a circle
            self.x=x
            self.y=y
            self.r=r
            self.fill=fill
            shape.__init__(self,color,size)
    def draw(self):
          t.penup()
          t.goto (self.x, self.y)
          t.pendown()
          t.begin_fill()
          t.width(7)
          t.color (self.color)
          t.fill(self.fill)
          t.circle (self.r)
          t.end_fill()
    def __str__(self):
        return "Circle"
class triangle(shape):
    def __init__(self,x,y,steps=3,color='black',size=1):
        self.x=x
        self.y=y
        self.steps=steps
        shape.__init__(self,color,size)

    def draw(self):
        t.pensize(3)
        t.penup()
        t.goto (self.x, self.y)
        t.color('yellow')
        t.begin_fill()
        t.forward(175)
        t.left(125)
        t.forward(200)
        t.left(125)
        t.forward(200)
        t.end_fill()
        t.penup()
        
    def __str__(self):
        return "triangle"
class rectangle(shape):
    def __init__(self,x,y,color="red",size=1):
        self.x=x
        self.y=y
        
        shape.__init__(self,color,size)
    def draw(self):
         t.pensize(3)
         t.penup()
         t.goto(self.x,self.y)
         t.color(self.color)
         t.begin_fill()
         t.forward(75)
         t.left(90)
         t.forward(90)
         t.left(90)
         t.forward(75)
         t.left(90)
         t.forward(90)
         t.left(90)
         t.end_fill()
    def __str__(self):
        return "rectangle"
class square(shape):
    def __init__(self,x,y,steps=4,color='black',size=1):
        self.x=x
        self.y=y
        self.steps=steps
        shape.__init__(self,color,size)
    def draw(self):
          t.penup()
          t.goto (self.x, self.y)
          t.pendown()
          t.begin_fill()
          t.color ('navy')
          t.circle (40, steps = 4)
          t.end_fill()
    def __str__(self):
        return "square"

def male_snow():
    circle_o=circle(-250,-250,120,color='red',fill=0)
    circle_o1=circle(-250,-10,90,color='red',fill=0)
    circle_o2=circle(-250,170,60,color='red',fill=0)
    circle_o3=circle(-250,85,10,color='green',fill=0)
    circle_o4=circle(-250,35,10,color='yellow',fill=0)
    circle_o5=circle(-250,-85,10,color='green',fill=0)
    circle_o6=circle(-250,-135,10,color='yellow',fill=0)
    circle_o2.draw()
    circle_o.draw()
    circle_o1.draw()
    parts_o=snow_man_parts()
    parts_o.snowmansarm(-150,60,70,20) 
    parts_o.snowmansarm(-350,60,70,160)
    parts_o.snowmansface(-250,240)
    line_o=line(-190,290,-310,290)
    line_o1=line(-240,215,-220,225)
    line_o2=line(-260,215,-280,230)
    line_o2.draw()
    line_o1.draw()
    line_o.draw()
    circle_o3.draw()
    circle_o4.draw()
    circle_o5.draw()
    circle_o6.draw()
    rectangle_o=rectangle(-285,290)
    rectangle_o.draw()
    
def female_snow():
    circle_o=circle(250,-250,120,color='black',fill=0)
    circle_o1=circle(250,-10,90,color='black',fill=0)
    circle_o2=circle(250,170,60,color='black',fill=0)
    circle_o3=circle(250,85,10,color='yellow',fill='yellow')
    circle_o4=circle(250,35,10,color='green',fill='pink')
    circle_o5=circle(250,-85,10,color='blue',fill='yellow')
    circle_o6=circle(250,-135,10,color='red',fill='pink')
    circle_o1.draw()
    circle_o.draw()
    circle_o2.draw()
    parts_o=snow_man_parts()
    parts_o.dot(235,220)
    parts_o.snowmansface(235,245)
    line_o=line(-60,290,-60,290)
    line_o1=line(160,80,80,10)
    line_o2=line(340,80,420,60)
    line_o3=line(420,60,330,-30)
    line_o4=line(230,290,200,230)
    line_o5=line(200,260,170,200)
    line_o6=line(260,280,320,230)
    line_o.draw()
    line_o1.draw()
    line_o2.draw()
    line_o3.draw()
    line_o4.draw()
    line_o5.draw()
    line_o6.draw()
    circle_o3.draw()
    circle_o4.draw()
    circle_o5.draw()
    circle_o6.draw()
    triangle_o=triangle(170,270)
    triangle_o.draw()
def main(): 
    t.title ('snowmen with colors')
    t.setup (1000, 1000, 0, 0)
    male_snow()
    female_snow()
    t.hidet()
    t.done()

main()

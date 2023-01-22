import turtle
#creating a new turtle object and assigning it to t

#setting the background color
turtle.bgcolor('#B97507')

#creating turtle objects and assigning it to t1 and t2
turtle.title("Scooby-Doo")
t1 = turtle.Turtle()
t2 = turtle.Turtle()

#keeping the fasted speed for now, you can keep the speed as needed
#'fastest' : 0
#'fast' : 10
#'normal' : 6
#'slow' : 3
#'slowest' : 1

t1.speed(0)

#setting the size of pen to 3 
t1.pensize(3)


t2.speed(0)
t2.pensize(3)
#t1 is pointing towards positive x-axis
#t2 is pointing towards left x-axis

#pu is same as pen up
t1.pu()
t2.pu()

# going at co-ordinates(0,-140), as we will start drawing from this position 
# we will begin with foot
t1.goto(0,-240) 
t2.goto(0,-240)

t1.pd()
t2.pd()

#the pointer t1, point towards 20 degrees with respect to positive x-axis
t1.right(20)
#the pointer t2, point towards 20 degrees with respect to negative x-axis
t2.right(180-20)

t1.forward(40) #right foot length
t2.forward(40) #left foot length

#we will again go to the co-ordinates from where we started drawing foot
t1.pu()
t2.pu()

t1.goto(0,-240) 
t2.goto(0,-240)

t1.pd()
t2.pd()

#from here we will start making the front two legs
t1.left(80)
t2.right(80)

t1.forward(40)
t2.forward(40)

t1.left(120)
t2.right(120)

t1.forward(15) #right leg
t2.forward(15) #left leg

t1.right(110)
t2.left(110)

t1.forward(55)
t2.forward(55)

t1.circle(100,50)
t2.circle(-100,50)

t1.left(80)
t2.right(80)

t1.circle(-40,60)
t2.circle(40,60)
#inner side of front two legs done

#now, the below lines of code will draw the stomach
#t1: left side, t2.right side
t1.forward(20)
t2.forward(20)

t1.right(15)
t2.left(15)

t1.forward(20)
t2.forward(20)

t1.circle(-40,60)
t2.circle(40,60)

t1.forward(30)
t2.forward(20)

t1.pu()
t2.pu()

t1.left(10)
t2.right(20)

t1.forward(15)
t2.forward(20)

t1.pd()
t2.pd()
#store co-ordinates of current position of t1 and t2 pointers so that
#after completing the lower body, we can start to draw the neck & face
#from this particular position
t1_face=t1.pos() 
t2_face=t2.pos()

#the below lines of code will draw the outer side of stomach and front legs
t1.left(160)
t2.right(155)

t1.forward(30)
t2.forward(65)

t1.right(9)
t1.forward(25)

t1.circle(30,40)
tail=t1.pos()
t2.circle(-30,40)

t1.left(10)
t2.right(20)

t1.forward(10)
t2.forward(20)

t1.left(20)
t2.right(20)

t1.forward(30)
t2.forward(8)

#storing the co-ordinates so that we can start to draw the two back legs from here
t1_backleg=t1.pos()
t2_backleg=t2.pos()

#let's proceed to first draw the outer side of front two legs
t1.circle(100,10)
t1.right(5)
t1.forward(10)
t1.right(180)
t1.forward(10)
t1.left(130)
t2.left(55)

t1.circle(100,40)
t2.circle(-190,10)
t2.circle(-190,20)

t1.forward(80)
t2.forward(15)

t1.circle(-15,150)
t2.left(5)
t2.circle(250,10)

t2.forward(10)
t2.circle(9,80)
t1.forward(6)

#left feet
t1.left(80)
t1.circle(20,120)
t1.left(20)
t1.forward(10)

#right feet
t2.right(40)
t2.circle(10,120)
t2.forward(5)
t2.right(115)
t2.circle(-20,150)
#till this point, we completed drawing front legs and stomach

#now, we will start to draw two back legs
t1.pu()
t1.goto(t1_backleg)
t2.pu()
t2.goto(t2_backleg)
t1.pd()
t2.pd()

t1.right(120)
t2.right(210)

t1.forward(70)
t2.forward(70)

t1.left(60)
t2.right(60)

t1.forward(40)
t2.forward(40)

t1.left(40)
t2.right(40)

t1.forward(38)
t2.forward(51)

t1.right(50)
t2.left(40)

t1.pu()
t2.pu()

t1.forward(20)
t2.forward(20)

t1.pd()
t2.pd()

t1.right(60)
t2.left(80)

t1.forward(40)
t2.forward(30)

t1.left(90)
t2.right(90)

t1.forward(10)
t2.forward(10)

t1.right(180)
t2.right(180)

t1.forward(15)
t2.forward(15)

t1.circle(10,140)
t2.circle(-10,140)

t1.forward(10)
t2.forward(10)

t1.left(50)
t2.right(50)

t1.forward(25)
t2.forward(30)
#till this point, we have drawn the four legs and stomach

#let's draw the tail now
t1.pu()
t1.goto(tail) # we had stored the co-ordinates where we wanted to draw tail
t1.pd()
t1.right(170)
t1.circle(-20,50)
t1.right(10)
t1.circle(-20,50)
t1.forward(40)
t1.circle(30,180)
t1.forward(10)
t1.circle(10,40)
t1.circle(9,200)
t1.right(50)
t1.forward(5)
t1.circle(-12,100)
t1.left(10)
t1.circle(-12,100)
t1.left(5)
t1.circle(-200,10)
t1.circle(100,18)
t1.circle(20,90)
t1.circle(140,12)
#till now we have completed drawing the lower body

#Now, let's proceed to draw neck and face
#we have already stored the co-ordinated, from where we want to draw neck and face
#below lines of code will take the turtles t1 and t2 to those positions 
t1.pu()
t2.pu()
t1.goto(t1_face)
t2.goto(t2_face)
t1.pd()
t2.pd()

#let's start drawing the neck
#we will draw the necklace first
t1.fillcolor('#10CA95')
t2.fillcolor('#10CA95')

t1.begin_fill()
t2.begin_fill()

t1.left(100)
t2.right(130)
t1.forward(20)#width of necklace
t2.forward(20)
t1.right(70)
t2.left(70)
t1.forward(10)
t2.forward(10)
t1.right(180)
t1.forward(10)
t1.left(135)
t1.circle(90,52)
t1.right(110)
t1.pu()
t1.forward(20)
t1.pd()
t1.right(70)
t1.circle(-90,54)
t1.right(65)
t1.forward(21)
t1.right(70)
t1.forward(15)
t2.forward(5)

t1.end_fill()
t2.end_fill()

#the necklace will get drawn by this point

#let's proceed to draw neck
t1.right(100)
t2.left(100)
t1.forward(10)
t2.forward(10)
t1.right(180)
t2.right(190)
t1.pu()
t2.pu()
t1.forward(10)
t2.forward(10)
t1.pd()
t2.pd()
t1.forward(20)
t2.forward(20)
t1.circle(-180,10)
t2.circle(170,12)
#till now, we have completed drawing till neck

#let's go ahead and draw the face
t1_face=t1.pos()
t2_face=t2.pos()
#we are again storing the co-ordinates of current position of the two turles
#first we will draw the upper part of face
#after that we will come back to this position that we stored
#and draw the lower part of the face

#drawing upper part of face
t1.left(40)
t2.right(40)

t1.forward(14)
t2.forward(14)

t1.circle(-15,90)
t2.circle(15,90)

t1.forward(9)
t2.forward(9)

t1.left(90)
t2.right(90)

t1.pensize(1.5)
t2.pensize(1.5)
t1.circle(-10,90)
t2.circle(10,90)
t1.pensize(3)
t2.pensize(3)
t1.pu()
t2.pu()
t1.goto(t1_face)
t2.goto(t2_face)
t1.left(65)
t2.right(65)
t1.forward(33)
t2.forward(33)
t1.pd()
t2.pd()
t1.left(10)
t2.right(10)
t1.forward(9)
t2.forward(9)
t1.circle(-15,75)
t2.circle(15,75)
t1.left(6)
t2.right(6)
t1.forward(18)
t2.forward(18)
#drawing ears
t1.left(110)
t2.right(100)
t1.circle(-20,15)
t2.circle(20,15)
t1.forward(8)
t2.forward(5)
t1.circle(-20,100)
t2.circle(20,100)
t1.right(90)
t2.left(90)
t1.circle(-90,30)
t2.circle(90,27)
#we have drawn the ears

t1.left(115)
t1.circle(-30,57)

#we'll now proceed to draw the eyes
t1.pu()
t2.pu()
t1.right(140)
t2.left(25)
t1.forward(40)
t2.forward(10)
t1.right(180)
t1.left(30)
t2.right(150)
#we reached the position from where we can draw eyebrows
#let's increase pensize as eyebrows are dark
t1.pd()
t2.pd()
t1.pensize(6)
t2.pensize(6)
t1.circle(-15,68)
t2.circle(15,68)
t1.pensize(2)
t2.pensize(2)
#eyebrows done, now we will draw the eyes
t1.pu()
t2.pu()
t1.right(80)
t2.left(80)
t1.forward(15)
t2.forward(15)
t1.left(8)
t2.right(8)
t1.pd()
t2.pd()


t1.fillcolor('white')
t1.begin_fill()
t1.circle(-7,360)
t1.end_fill()

t1.circle(-7,60)

t1.fillcolor('black')
t1.begin_fill()
t1.circle(-4,360)
t1.end_fill()

t2.fillcolor('white')
t2.begin_fill()
t2.circle(7,360)
t2.end_fill()

t2.circle(7,60)

t2.fillcolor('black')
t2.begin_fill()
t2.circle(4,360)
t2.end_fill()
#we have drawn the eyes also
#now we will go to the position that we stored earlier
#so, that we can draw the lower part of face
t1.pu()
t2.pu()
t1.goto(t1_face)
t2.goto(t2_face)
t1.left(120)
t2.right(135)
t1.pd()
t2.pd()
t1.forward(10)
t2.forward(10)
t1.circle(18,165)
t2.circle(-15,80)
#drawing the nose using turtle t1
t1.begin_fill()
t1.right(85)
t1.forward(18)
t1.left(95)
t1.circle(25,85)
t1.left(100)
t1.forward(30)
t1.end_fill()
#now we are done with nose, so let's go ahead and draw mouth
t2.left(120)
t2.pu()
t2.circle(-18,35)
tongue=t2.pos()
t1.pu()
t1.goto(tongue)
t2.circle(-18,50)

t1.pd()
t2.pd()
#we will draw tongue using turtle t1
#and mouth using turtle t2
t1.right(25)
t1.circle(10,140)
#we have completed drawing tongue

#let's draw the mouth now
t2.left(135)
t2.circle(25,115)

#we have completed drawing the dog
t1.hideturtle()
t2.hideturtle()

turtle.done()
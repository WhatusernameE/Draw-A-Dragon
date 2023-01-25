import turtle


t = turtle.Turtle()
turtle.Screen().bgcolor("white")

#Variables To Run While Loops.
time = 1
timeTwo = 1
timeThree = 1
timeFour = 1
timeFive = 1
timeSix = 1
timeSeven = 1

#How The Turtle Is Drawing.
t.shape("turtle")
t.width(5)
t.speed(10)

#t.forward(Moves Forwards)
#t.right(Turns Right Set Amount Of Degrees)
#t.left(Turns Left Set Amount Of Degrees)
#t.back(Moves Backwards)


#Creates The Body For The Dragon.
t.color("red", "dark cyan")
t.begin_fill()
t.forward(175)
t.right(90)
t.forward(75)
t.left(-90)
t.forward(175)
t.right(90)
t.forward(75)
t.end_fill()

#Create head
t.color("red", "light gray")
t.begin_fill()
t.forward(45)
t.left(90)
t.forward(45)
t.left(90)
t.forward(45)
t.left(90)
t.forward(45)
t.end_fill()
#Creates The Spikes.
for a in ["black"]:
    while time < 4:
        t.color(a)
        t.penup()
        t.forward(20)
        t.pendown()
        t.left(45)
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.left(45)

        time = time + 1
    t.penup()
    t.forward(30)
    t.right(90)
    t.forward(75)
for c in ["red"]:
    t.color(c)
    t.penup()
    #Creates the legs
    t.right(90)
    t.forward(30)
    t.left(90)
    t.forward(65)

    while timeTwo < 3:

        t.pendown()
        t.left(65)
        t.forward(15)
        t.right(90)
        t.forward(5)
        t.right(90)
        t.forward(15)
        timeTwo = timeTwo + 1

for c in ["green"]:
    t.color(c)
    t.forward(7)
    t.left(50)
    t.forward(61)
    t.left(90)

for c in ["red"]:
    t.color(c)

    #Creates the legs
    t.forward(38)
    t.left(90)
    t.forward(65)

    while timeThree < 3:

        t.left(65)
        t.forward(15)
        t.right(90)
        t.forward(5)
        t.right(90)
        t.forward(15)

        timeThree = timeThree + 1

for c in ["green"]:
    t.color(c)
    t.forward(7)
    t.left(50)
    t.forward(61)
    t.left(90)

for c in ["red"]:
    t.color(c)
    t.forward(107)
    t.right(90)
    t.forward(75)
    t.left(90)
    t.forward(45)
    t.right(90)
    t.forward(25)

    #Unicorn Horn

for c in ["green"]:
    t.color(c)
    t.left(25)
    t.forward(100)
    t.right(158)
    t.forward(103)
    t.left(43)

    #Move back to do tail.

for c in ["black"]:
    t.color(c)
    t.penup()
    t.forward(187)
    t.right(90)
    t.forward(45)
    t.forward(25)

    #Create Tail:
    t.pendown()
    while timeFour < 10:

        t.left(20)
        t.forward(12.5)

        timeFour = timeFour + 1


for c in ["black"]:
    t.color(c)
    while timeFive < 10:
        t.right(20)
        t.back(12.5)

        timeFive = timeFive + 1

    #going back to be able to create the eyes

    t.penup()
    t.left(90)
    t.back(220)
    t.left(90)
    t.forward(30)

for c in ["black"]:
    t.color(c)
    t.right(90)
    t.forward(13)
    t.width(2)
    t.pendown()

    t.begin_fill()
    while timeSix < 5:
        t.right(90)
        t.forward(6)
        t.speed(3)
        timeSix = timeSix + 1
    t.end_fill()

    t.right(90)
    t.forward(3)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(3)

    t.begin_fill()
    while timeSeven < 5:
        t.right(90)
        t.forward(6)
        t.speed(3)
        timeSeven = timeSeven + 1
    t.end_fill()
t.penup()
t.forward(100)
turtle.Screen().exitonclick()

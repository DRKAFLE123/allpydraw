# we are going to make 3D spiral in vs code using python
import turtle as dk
import colorsys

dk.bgcolor('black')
dk.speed('fastest')
dk.pensize(2)
hue=0.0
dk.hideturtle()

for i in range(500):
    color=colorsys.hls_to_rgb(hue,0.6,1)
    dk.pencolor(color)
    dk.fd(i)
    dk.rt(98.5)
    dk.circle(100)
    hue+=0.005

dk.exitonclick()
# now run the code

from turtle import*
import colorsys
speed(1)
bgcolor(white)
h = 0
for i in range(20):
    for j in range(25):
        c = colorsys.hsv_to_rgb(h,1,1)
        color(c)
        h += 
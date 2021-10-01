import graphics
import cmath

import colorsys

def hsv2rgb(h,s,v):
    rgb = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))
    return graphics.color_rgb(255-rgb[0],255-rgb[1],255-rgb[2])

def complex2color(z):
    zp = cmath.polar(z)
    return hsv2rgb((zp[1]+cmath.pi)/(2*cmath.pi),(1-5**(-zp[0]))*1.0,1.0)
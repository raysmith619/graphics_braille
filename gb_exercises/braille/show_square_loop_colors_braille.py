# show_square_loop_colors_braille.py  # braille
# Display a square with colored sides

##from turtle import *		     # Get standard stuff
#import graphics_braille
import graphics_braille.wx_turtle_braille as tu		     # Get braille

colors = ["red","orange","yellow","green"]

for colr in colors:
    tu.width(40)
    tu.color(colr)
    tu.forward(200)
    tu.right(90)
tu.done()		    # Complete drawings

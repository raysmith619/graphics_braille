# x_show_square_loop_colors_braille.py  # braille
# Display a square with colored sides
#isolate except for this directory
import sys
import os
file_dir = os.path.dirname(__file__)
def remove_path_ending(ending=None):
    """ Remove all sys.path entries ending in 
    :ending: ending of path to be removed
    """
    found = True
    while found:
        found = False       # Set if any found
        sys_path = sys.path
        for ent in sys.path:
            if ent.endswith(ending):
                sys_path.remove(ent)
                print(f"Removing: {ent}")
                found = True
        if found:
            sys.path = sys_path
                
remove_path_ending(r"\resource_lib\src")
mod_dir = r"C:\Users\Owner\AppData\Local\Programs\Python\Python313\Lib\site-packages\graphics_braille"
mod_dir = r"C:/Users/raysm/vscode/graphics_braille_main/src/graphics_braille"
if len(sys.argv) > 1:
    opt = sys.argv[1]
    print(f"Hacking in module directory:{mod_dir}")
    sys.path.append(mod_dir)    
print(f"sys.path:\n    {"\n    ".join(sys.path)}")
##from turtle import *		     # Get standard stuff
from graphics_braille import *
from graphics_braille import wx_turtle_braille
from graphics_braille import wx_tk_rpc_host
from wx_turtle_braille import *		     # Get braille

colors = ["red","orange","yellow","green"]

for colr in colors:
    width(40)
    color(colr)
    forward(200)
    right(90)
done()		    # Complete drawings

#__init__.py    30Oct2025  crs
# Command line scripts for graphics_braille
from graphics_braille import *

def gbhelp():
    print("""
          gb, gbhelp - List graphics-braille commands
          gbreadme - Display README.md
          gbtest - Do simple program test
          """)

def gbreadme():
    import os
    os.system("distinfo_readme graphics_braille")

def gbtest():
    import graphics_braille.z_show_square_loop_colors_braille

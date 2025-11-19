#__init__.py    30Oct2025  crs
# Command line scripts for graphics_braille
import shutil
import pathlib

from graphics_braille import *

def main_function():
    print("Installation Run")

def gbhelp():
    print("""
          gb, gbhelp - List graphics-braille commands
          gbreadme - Display README.md
          gbfiles - add user files to user desktop
          gbtest - Do simple program test
          """)

def gbreadme():
    import os
    os.system("distinfo_readme graphics_braille")

def gbfiles():
    """ Download user files
    """
    source_dir = "exercises"
    desktop = pathlib.Path.home() / 'Desktop'
    user_dir = desktop
    try:
        # Copy the directory tree, allowing existing directories
        shutil.copytree(source_dir, user_dir, dirs_exist_ok=True)
        print(f"Successfully copied '{source_dir}' to '{user_dir}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    
    
def gbtest():
    import graphics_braille.z_show_square_loop_colors_braille

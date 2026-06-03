# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 09:04:47 2026

"""
# Lisa Kraatz

from tkinter import *

def main():
    root = Tk()
    color = 'lavender'
    root.title('Smiley Face')
    canvas = Canvas(root,
                    bg = 'lavender',
                    width = 600,
                    height = 800)
    canvas.pack()
    # Outline Circle
    canvas.create_oval(50,50,550,550,
                       outline = 'purple',
                       width = 5)
    # Left Small Circle
    canvas.create_oval(160,160,250,250,
                       fill = 'skyblue',
                       width = 0) # No outline
    # Left Small Inner Circle
    canvas.create_oval(180,180,230,230,
                       fill = 'black',
                       width = 0) # No outline
    # Right Small Circle
    canvas.create_oval(360,160,450,250,
                       fill = 'lightgreen',
                       width = 0)
    # Right Small Inner Circle
    canvas.create_oval(380,180,430,230,
                       fill = 'black',
                       width = 0)
    # Rectangle
    canvas.create_rectangle(150,300,450,350,
                       fill = 'turquoise',
                       width = 0)
    # Triangle
    points = [150,360,450,360,300,500]
    canvas.create_polygon(points,
                       fill = 'pink',
                       width = 2)
    
    root.mainloop()
    
    
main()


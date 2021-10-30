from drawingpanel import *

width = 1024
height = 768
panel = DrawingPanel(width, height)
canvas = panel.canvas
 
def draw_h(x, y, size):
    #draw an H centered at (x,y) of a certain size
    canvas = panel.canvas
    canvas.create_line(x - size / 2, y, x + size / 2, y)
    canvas.create_line(x - size / 2, y + size / 2, 
    	x - size / 2, y - size /2)
    canvas.create_line(x + size / 2, y + size / 2,
                    x + size / 2, y - size / 2)
 

def draw_h_recur(n,  x,  y, size):
    #n controlling the recursion level. What is the smallest size H. 
        if n == 0:
        	return

        #draw the central/main H
        draw_h(x, y, size)
        
        #now recursively make 4 smaller H trees
        x0 = x - size / 2
        y0 = y - size / 2
        x1 = x + size / 2
        y1 = y + size / 2
        #first draw the bottom left subtree
        draw_h_recur(n - 1, x0, y0, size / 2)
        #then draw the top left subtree
        draw_h_recur(n - 1, x0, y1, size / 2)      
        #then the bottom right subtree
        draw_h_recur(n - 1, x1, y0, size / 2)
        draw_h_recur(n - 1, x1, y1, size / 2)
        panel.sleep(100)


def main():
    
    draw_h_recur(6, width / 2, height / 2, width / 4)


main()


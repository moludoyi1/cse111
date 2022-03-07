
# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    
    draw_rectangle(canvas, 0, 0, 800, 500, fill='blue4')


    draw_oval(canvas, 100, 450, 200, 400, fill="pink")
    draw_oval(canvas, 0, 470, 130, 400, fill="pink")
    #keep  draw_oval(canvas, 750, 470, 130, 400, fill="red")
    draw_oval(canvas, 750, 470, 650, 400, fill="red")




    draw_mount(canvas, 150, 150, 500)
    draw_mount(canvas, 10, 150, 500)

    draw_rectangle(canvas, 0, 0, 800, 175, fill='darkGreen')

    draw_cloud(canvas, 137, 435, 210)
    draw_cloud(canvas, 210, 390, 100)
    draw_cloud(canvas, 320, 290, 150)
    draw_cloud(canvas, 250, 375, 150)
    draw_cloud(canvas, 190, 382, 100)

    draw_cloud(canvas, 450, 400, 350)#1
    draw_cloud(canvas, 420, 350, 450)#2
    draw_cloud(canvas, 480, 320, 350)#3
    draw_cloud(canvas, 500, 300, 350)#4
    draw_cloud(canvas, 600, 410, 400)#5
    draw_cloud(canvas, 550, 300, 350)#6
    draw_cloud(canvas, 600, 350, 500)#7

    draw_cloud(canvas, 750, 270, 700)#test


    draw_cloud(canvas, 50, 430, 100)

    draw_oval(canvas, 750, 470, 650, 400, outline="black", fill="salmon")#example
    draw_oval(canvas, 450, 270, 600, 100, outline="darkorange", fill="darkGoldenrod1")#sun


    for x2 in range (25, 900, 55):
        draw_pine_tree(canvas, x2, 100, 170)
        x2 = x2 + 25
        draw_pine_tree(canvas, x2, 100, 150)
        x2 = x2 + 7
        draw_pine_tree(canvas, x2, 100, 140)

    for x1 in range(25, 900, 50):
        draw_pine_tree(canvas, x1, 100, 150)

    for x in range(100, 900, 50):
        #draw_pine_tree(canvas, x, 250, 80)
        x = x + 50
        #draw_pine_tree(canvas, x, 150, 200)
        x = x + 100
        #draw_pine_tree(canvas, x, 100, 200)
        x = x - 200
        draw_pine_tree(canvas, x, 50, 220)
        #draw_pine_tree(canvas, x, 50, 220) #redundint





    draw_grid(canvas, scene_width, scene_height, 50)
        
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.


def draw_pine_tree(canvas, center_x, bottom, height):
    #draw tree trunk
    trunk_width = height / 10
    trunk_height = height / 8
    left_trunk = center_x - trunk_width / 2# should be 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2#should be 2
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, trunk_top, fill='tan4')

    #tree skirt
    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_bottom = trunk_top
    peak_x = center_x
    peak_y = bottom + height
    skirt_right = center_x + skirt_width / 2
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y, skirt_right, skirt_bottom, fill='forestGreen')

def draw_grid(canvas, width, height, interval):
    #for drawing a vertical line
    label_y = 15
    for x in range(interval, width, interval):
        #draw_line(canvas, x, 0, 30, height) #Idea for sunshine
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f'{x}')
        #for drawing horizontal lines
    label_x = 15
    for y in range(interval, height, interval):
        #draw_line(canvas, x, 0, 30, height) #Idea for sunshine
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f'{y}')

def draw_cloud(canvas, center_x, bottom, height):
    #draw clouds
    cloud_width = height / 7
    cloud_height = height / 5
    left_cloud = center_x - cloud_height
    bottom_cloud = bottom
    right_cloud = center_x + cloud_height
    cloud_top = bottom + cloud_height
    #draw_oval(canvas, cloud_left, cloud_bottom, cloud_right, cloud_top, fill='salmon')
    draw_oval(canvas, left_cloud, bottom_cloud, right_cloud, cloud_top, outline="salmon", fill='salmon')

def draw_mount(canvas, center_x, bottom, height):
    #draw mounains 
    mountain_width = height / 9
    mountain_height = height / 4
    left_mountain = center_x - (mountain_height * 2)
    bottom_mountain = center_x - bottom 
    right_mountain = center_x + (mountain_height * 2)
    mountain_top = center_x + mountain_height
    #draw_polygon(canvas, left_mountain, bottom_mountain, right_mountain, mountain_top, fill='purple')
    draw_polygon(canvas, left_mountain, bottom_mountain, mountain_top, height, right_mountain, bottom_mountain, fill='purple')



    
    

# Call the main function so that
# this program will start executing.
main()

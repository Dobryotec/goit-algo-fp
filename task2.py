import turtle

def draw_pythagoras_tree(branch_length, level, t):
    if level == 0:
        return

    t.forward(branch_length)

    pos = t.position()
    angle = t.heading()

   
    t.right(45)
    draw_pythagoras_tree(branch_length * 0.7, level - 1, t)

 
    t.setposition(pos)
    t.setheading(angle)

    t.left(45)
    draw_pythagoras_tree(branch_length * 0.7, level - 1, t)


    t.setposition(pos)
    t.setheading(angle)

def main():
    screen = turtle.Screen()
    screen.title("Pythagoras Tree")

    t = turtle.Turtle()
    t.speed(0)  
    t.left(90)  

    level = int(turtle.numinput("Level of Recursion", "Enter the level of recursion:", 5, minval=1, maxval=15))


    draw_pythagoras_tree(100, level, t)

    screen.mainloop()

if __name__ == "__main__":
    main()

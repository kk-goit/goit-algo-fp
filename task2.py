import turtle

def draw_square(t: turtle.Turtle, size):
    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.penup()
    

def pythagoras_tree(t: turtle.Turtle, order, size):
    draw_square(t, size)
    if order > 0:
        t.forward(size)
        new_size = size * 0.5 * (2**0.5)
        t.left(45)
        pythagoras_tree(t, order - 1, new_size)
        t.right(90)
        t.forward(new_size)
        pythagoras_tree(t, order - 1, new_size)
        t.backward(new_size)
        t.left(45)
        t.backward(size)

def draw_pythagoras_tree(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, 0)
    t.left(90)
    
    pythagoras_tree(t, order, size)

    window.mainloop()


if __name__ == "__main__":
    while True:
        rq = input("Please, enter the reqursion level:").strip()
        if not rq.isdecimal():
            print(f"{rq} is not a digit")
            continue
        break
    draw_pythagoras_tree(int(rq), 50)
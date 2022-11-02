from turtle import *

if __name__ == "__main__":
    speed(100)
    color('cyan')
    bgcolor('black')
    b = 200
    penup()
    forward(200)
    pendown()
    while b > 0:
        left(b)
        forward(b * 3)
        b-=1

    while True:
        if input("Input 'q': ") == 'q':
            break
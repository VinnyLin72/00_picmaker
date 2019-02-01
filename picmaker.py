from random import *

def main():
    pic = open('image.ppm', 'w')
    w = 500
    h = 500
    pic.write('P3\n500 500\n255\n')
    color = str(randint(0, 255))
    for i in range(h):
        for j in range(w):
            if (randint(0, 1) == 1):
                 color = str(randint(0, 255))
            pic.write(color + ' ' + color + ' ' + color + ' ')
    pic.close()


main()

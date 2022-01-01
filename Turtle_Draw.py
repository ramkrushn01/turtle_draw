from turtle import Screen, Turtle, mainloop, up

from numpy.lib.function_base import angle
from img_info import ImgInfo
import random


class DrawImg(Turtle):

    def drawImg(self, x, y, d, maxd):
        # print('x',x,'y',y)
        # if x < -324 and y > 99 and y < 198:
                # self.pencolor('red')
        if False:
            pass

        else:
            self.pencolor('black')
        if d >= maxd:
            pass
        else:
            self.up()
            self.goto(x, y)
            self.down()
            self.forward(d)

    def drawMe(self, xcor, ycor, diff):
        self.speed(10)
        self.up()
        self.goto(-400, 400)
        self.down()
        self.maxd = max(diff[:10])
        self.xcorLen = len(xcor)
        self.ranList = random.sample(
            list(range(0, self.xcorLen)), self.xcorLen)

        for i in range(len(xcor)):
            # j = self.ranList[i]
            j = i
            x = (xcor[j])-400
            y = -(ycor[j])+400
            d = diff[j]
            self.drawImg(x, y, d, self.maxd)

def main():
    imgMe1 = input('Enter Your Image Path: ')
    imgMe = f'pngImg/{imgMe1}.png'
    imginfo = ImgInfo()
    imlist = imginfo.imgInfo(imgMe)

    # window = Screen()
    # window.onclick(lambda x, y: print(x, y))
    # window.bgcolor("black")
    drme = DrawImg()
    drme.speed(0)
    drme.getscreen().delay(10)
    drme.getscreen().tracer(10)
    drme.drawMe(imlist[0], imlist[1], imlist[2])
    

if __name__ == '__main__':
    main()
    mainloop()

# for dhoni3
# if x < -324 and y>99 and y<198: line number 15

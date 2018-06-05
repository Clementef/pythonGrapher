from graphics import *
import math

def main():
	global win
	win = GraphWin("Grapher",500,500)
	win.setBackground(color_rgb(51,51,51))

	drawAxes()

	drawFunc()

	win.getMouse()
	win.close()

def funcOperation(n):
	return ((math.cos(3*n/50)*50)+(.01*(n ** 2))-100)

def drawAxes():
	leftPt = Point(0,250)
	rightPt = Point(500,250)
	horizLine = Line(leftPt,rightPt)
	horizLine.setOutline(color_rgb(255,255,255))
	horizLine.setWidth(1)
	horizLine.draw(win)

	topPt = Point(250,0)
	bottomPt = Point(250,500)
	vertLine = Line(topPt,bottomPt)
	vertLine.setOutline(color_rgb(255,255,255))
	vertLine.setWidth(1)
	vertLine.draw(win)

	for i in range(0,500,10):
		pt1 = Point(i,245)
		pt2 = Point(i,255)
		conLine = Line(pt1,pt2)
		conLine.setOutline(color_rgb(255,255,255))
		conLine.setWidth(1)
		conLine.draw(win)
	for i in range(0,500,10):
		pt1 = Point(245,i)
		pt2 = Point(255,i)
		conLine = Line(pt1,pt2)
		conLine.setOutline(color_rgb(255,255,255))
		conLine.setWidth(1)
		conLine.draw(win)

def drawFunc():
	step = 1
	for i in range(-250,250,step):
		pt1 = Point(i+250,-1 * funcOperation(i)+250)
		pt2 = Point(i+250+step,-1 * funcOperation(i+step)+250)
		conLine = Line(pt1,pt2)
		conLine.setOutline(color_rgb(255,255,255))
		conLine.setWidth(1)
		conLine.draw(win)


if __name__ == "__main__":
	main()
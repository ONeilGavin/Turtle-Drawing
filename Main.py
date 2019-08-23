import tkinter as tk
import Drawing
import Recamen
import Ulam


def runDrawing(draw, drawSpeed, drawType):
    if drawType == 0:
        Drawing.draw(draw, drawSpeed)
    elif drawType == 1:
        Recamen.draw(draw, drawSpeed)
    elif drawType == 2:
        Ulam.draw(draw, drawSpeed)

def drawingType(num):
    global type
    global draw
    global drawSpeed
    if num == 0:
        type = 0
    elif num == 1:
        type = 1
    elif num == 2:
        type = 2
    if yesCount.get() != 0:
        draw = True
        drawSpeed = speedSlider.get()
    else:
        draw = False

window = tk.Tk()
window.title('Drawing')

showDrawing = tk.Label(window, text = "Show picture being drawn?")
showDrawing.pack()

yesCount = tk.IntVar()
yesButton = tk.Checkbutton(window, text = "Yes", variable = yesCount)
yesButton.pack()

noCount = tk.IntVar()
noButton = tk.Checkbutton(window, text = "No", variable = noCount)
noButton.pack()

turtleSpeed = tk.Label(window, text = "Select drawing speed")
turtleSpeed.pack()

speedSlider = tk.Scale(window, from_=1, to =10, orient = tk.HORIZONTAL)
speedSlider.pack()


swirlButton = tk.Button(window, text="Square Swirl", command = lambda: drawingType(0))
swirlButton.pack()

recamenButton = tk.Button(window, text = "Recamen Sequence", command = lambda : drawingType(1))
recamenButton.pack()

ulamButton = tk.Button(window, text = "Ulam Spiral", command = lambda : drawingType(2))
ulamButton.pack()

startButton = tk.Button(window, text = "Start", command = lambda : runDrawing(draw, drawSpeed, type))
startButton.pack()

closeButton = tk.Button(window, text = "Quit", command = lambda : window.destroy())
closeButton.pack()

window.mainloop()


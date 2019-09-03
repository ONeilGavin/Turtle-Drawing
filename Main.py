import tkinter as tk
import Recamen
import SquareSwirl
import Ulam



def runDrawing(draw, drawSpeed, drawType): #Draw based on its visibility and type
    if drawType == 0:
        SquareSwirl.draw(draw, drawSpeed)
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

    if yesCount.get() == 1: #If yes to show drawing, set draw to true and set the speed to the slider's state
        draw = True
        drawSpeed = speedSlider.get()
    elif noCount.get() == 1:
        draw = False
        drawSpeed = 0

#Create Window and button for the GUI
window = tk.Tk()
window.title('Drawing')

showDrawing = tk.Label(window, text = "Show picture being drawn?")
showDrawing.pack()
#Store yes values
yesCount = tk.IntVar()
yesButton = tk.Checkbutton(window, text = "Yes", variable = yesCount)
yesButton.pack()
#Store no values
noCount = tk.IntVar()
noButton = tk.Checkbutton(window, text = "No", variable = noCount)
noButton.pack()

turtleSpeed = tk.Label(window, text = "Select drawing speed")
turtleSpeed.pack()

speedSlider = tk.Scale(window, from_=1, to =10, orient = tk.HORIZONTAL)
speedSlider.pack()

#Each drawing button calls the drawingType method with its corresponding number for which type of drawing it is
#drawingType will initialize the variables that control the visibility and speed of the drawing
swirlButton = tk.Button(window, text="Square Swirl", command = lambda: drawingType(0))
swirlButton.pack()

recamenButton = tk.Button(window, text = "Recamen Sequence", command = lambda : drawingType(1))
recamenButton.pack()

ulamButton = tk.Button(window, text = "Ulam Spiral", command = lambda : drawingType(2))
ulamButton.pack()

#Runs the drawing with a boolean representing if it will be showing, its draw speed, and the drawing type
startButton = tk.Button(window, text = "Start", command = lambda : runDrawing(draw, drawSpeed, type))
startButton.pack()

closeButton = tk.Button(window, text = "Quit", command = lambda : window.destroy())
closeButton.pack()

window.mainloop()

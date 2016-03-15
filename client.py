from tkinter import *
from functools import partial

w=540
h=540
flh=150
tbw=300
toolWindowMargin=20
toolHeight=90
toolMargin=10
toolSmallHeight = 50
buttonSize = 50
toolIdleBG = "#AAAAAA"
toolIdleActiveBG = "#BBBBBB"
toolSelectedBG = "#CCCC55"
toolSelectedActiveBG = "#BBBB44"
selectedTool = "start"
startLocation = [-1, -1]

root = Tk()
root.title("Nathair Level Generator")
editfull = Frame(root, width=w+tbw, height=h,)
editfull.pack(side=TOP)

finishedLvlsImage = PhotoImage(file="finishedLevels.png")
finishedLvls =  Frame(root, width=w+tbw, height=flh, bg="red")
finishedLvlsBG = Label(finishedLvls, image=finishedLvlsImage)
finishedLvlsBG.place(x=0, y=0, relwidth=1, relheight=1)
finishedLvls.pack(side=BOTTOM)

toolbarImage = PhotoImage(file="toolPannel.png")
toolbar = Frame(editfull, width=tbw, height=h)
toolbarBG = Label(toolbar, image=toolbarImage)
toolbarBG.place(x=0, y=0, relwidth=1, relheight=1)
toolbar.pack(side=RIGHT)


widthSlider = Scale(toolbar, from_=3, to=10, orient=HORIZONTAL, label="width")
widthSlider.place(x=toolMargin,y=toolMargin, height=toolHeight-20, width=tbw-20)
widthSlider.set(5)

heightSlider = Scale(toolbar, from_=3, to=10, orient=HORIZONTAL, label="height")
heightSlider.place(x=toolMargin,y=toolHeight+toolMargin, height=toolHeight-20, width=tbw-20)
heightSlider.set(5)

editWindowImage = PhotoImage(file="checkerboard.png")
editwindow = Frame(editfull, width=w, height=h)
background_label = Label(editwindow, image=editWindowImage)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
editwindow.pack(side=LEFT)

buttons = []
colors = ["red", "green", "blue", "yellow"]
wallImage = PhotoImage(file="wall.png")
openImage = PhotoImage(file="open.png")
unknownImage = PhotoImage(file="unknown.png")
startImage = PhotoImage(file="start.png")
tpImages = {"tpred1" : PhotoImage(file="teleporterRed1.png"),
            "tpred2" : PhotoImage(file="teleporterRed2.png"),
            "tpblue1" : PhotoImage(file="teleporterBlue1.png"),
            "tpblue2" : PhotoImage(file="teleporterBlue2.png"),
            "tpgreen1" : PhotoImage(file="teleporterGreen1.png"),
            "tpgreen2" : PhotoImage(file="teleporterGreen2.png"),
            "tpyellow1" : PhotoImage(file="teleporterYellow1.png"),
            "tpyellow2" : PhotoImage(file="teleporterYellow2.png")}

tpLocations = {"tpred1" : [-1,-1], "tpred2" : [-1,-1], "tpblue1" : [-1,-1], "tpblue2" : [-1,-1],
            "tpgreen1" : [-1,-1], "tpgreen2" : [-1,-1], "tpyellow1" : [-1,-1], "tpyellow2" : [-1,-1]}

def buttonEvent(loc):
    x, y = loc
    global buttons
    global selectedTool
    global startLocation
    if selectedTool == "wall":
        buttons[x][y].configure(image=wallImage)
    elif selectedTool == "open":
        buttons[x][y].configure(image=openImage)
    elif selectedTool == "start":
        if startLocation != [-1, -1]:
            buttons[startLocation[0]][startLocation[1]].configure(image=unknownImage)
        buttons[x][y].configure(image=startImage)
        startLocation = [x, y]
    elif selectedTool == "erase":
        buttons[x][y].configure(image=unknownImage)
    else:
        if tpLocations[selectedTool] != [-1, -1]:
            buttons[tpLocations[selectedTool][0]][tpLocations[selectedTool][1]].configure(image=unknownImage)
        buttons[x][y].configure(image=tpImages[selectedTool])
        tpLocations[selectedTool] = [x, y]
    print("Button at (" + str(x) + ", " + str(y) + ") was pressed")


def createButtons(countW, countH):
    originX = ((10-countW) * buttonSize) / 2 + toolWindowMargin
    originY = ((10-countH) * buttonSize) / 2 + toolWindowMargin
    global buttons
    buttons = []
    for locX in range(0, countW):
        buttons.append([])
        for locY in range(0, countH):
            tempButtonHandler = partial(buttonEvent, (locX, locY))
            buttons[locX].append(Button(editwindow, command=tempButtonHandler, image=unknownImage))
            buttons[locX][locY].place(x=locX*50+originX, y=locY*50+originY, width=buttonSize, height=buttonSize)
    return buttons


def destroyButtons(buttons):
    for buttonCols in buttons:
        for button in buttonCols:
            button.destroy()


def setDimensionsAction():
    global startLocation
    startLocation = [-1, -1]
    global tpLocations
    for tpType in tpLocations:
        tpLocations[tpType] = [-1, -1]
    global buttons
    destroyButtons(buttons)
    buttons = createButtons(widthSlider.get(), heightSlider.get())


setDimensions = Button(toolbar, text="set map size", command=setDimensionsAction)
setDimensions.place(x=tbw/2-70, y=2*toolHeight+10, height=toolSmallHeight-2*toolMargin, width=140)

startTool = Button(toolbar, text="START TILE")
startTool.place(x=10, y=2*toolHeight+toolSmallHeight+10, width=tbw-2*toolMargin, height=toolSmallHeight-2*toolMargin)

openTool = Button(toolbar, text="FLOOR TILE")
openTool.place(x=10, y=2*toolHeight+toolSmallHeight*2+10, width=tbw-2*toolMargin, height=toolSmallHeight-2*toolMargin)

wallTool = Button(toolbar, text="WALL TILE")
wallTool.place(x=10, y=2*toolHeight+toolSmallHeight*3+10, width=tbw-2*toolMargin, height=toolSmallHeight-2*toolMargin)

eraseTool = Button(toolbar, text="ERASE TILE")
eraseTool.place(x=10, y=2*toolHeight+toolSmallHeight*4+10, width=tbw-2*toolMargin, height=toolSmallHeight-2*toolMargin)

tpTool = {"red":[], "green":[], "blue":[], "yellow":[]}

tpIter = 0
tpRowMargin = 7
tpButtonSpace = (tbw-tpRowMargin*2)/8
tpMargin = 3

toolMap = {"start" : startTool, "open" : openTool, "wall" : wallTool, "erase" : eraseTool}

l = Label(toolbar, text="Teleporters", bg="#7d7d7d")
l.place(x=10, y=2*toolHeight+toolSmallHeight*5-3, width=tbw-2*toolMargin, height=toolSmallHeight-2*toolMargin)

for color in colors:
    for i in range(0, 2):
        tpTool[color].append( Button(toolbar, text=str(i+1), fg=color) )
        tpTool[color][i].place(x=tpIter*tpButtonSpace+tpMargin+tpRowMargin, y=2*toolHeight+toolSmallHeight*5+27, width=tpButtonSpace-2*tpMargin, height=toolSmallHeight-2*toolMargin)
        tpIter += 1
        toolMap["tp" + color + str(i+1)] = tpTool[color][i]
    l = Label(toolbar, text=color, bg="#7d7d7d", fg=color)
    l.place(x=(tpIter-2)*tpButtonSpace+tpRowMargin, y=2*toolHeight+toolSmallHeight*6+7, width=2*tpButtonSpace)

def initTools():
    global toolMap
    for toolName, toolButton in toolMap.items():
        toolButton.configure(bg=toolIdleBG, activebackground=toolIdleActiveBG)

def setToolSelected(tool):
    global toolMap
    global selectedTool
    toolMap[selectedTool].configure(bg=toolIdleBG, activebackground=toolIdleActiveBG)
    toolMap[tool].configure(bg=toolSelectedBG, activebackground=toolSelectedActiveBG)
    selectedTool = tool

setToolStart = partial(setToolSelected, "start")
setToolOpen = partial(setToolSelected, "open")
setToolWall = partial(setToolSelected, "wall")
setToolErase = partial(setToolSelected, "erase")
toolMap["start"].configure(command=setToolStart)
toolMap["open"].configure(command=setToolOpen)
toolMap["wall"].configure(command=setToolWall)
toolMap["erase"].configure(command=setToolErase)

setTool_tpr1 = partial(setToolSelected, "tpred1")
toolMap["tpred1"].configure(command=setTool_tpr1)
setTool_tpr2 = partial(setToolSelected, "tpred2")
toolMap["tpred2"].configure(command=setTool_tpr2)
setTool_tpb1 = partial(setToolSelected, "tpblue1")
toolMap["tpblue1"].configure(command=setTool_tpb1)
setTool_tpb2 = partial(setToolSelected, "tpblue2")
toolMap["tpblue2"].configure(command=setTool_tpb2)
setTool_tpg1 = partial(setToolSelected, "tpgreen1")
toolMap["tpgreen1"].configure(command=setTool_tpg1)
setTool_tpg2 = partial(setToolSelected, "tpgreen2")
toolMap["tpgreen2"].configure(command=setTool_tpg2)
setTool_tpy1 = partial(setToolSelected, "tpyellow1")
toolMap["tpyellow1"].configure(command=setTool_tpy1)
setTool_tpy2 = partial(setToolSelected, "tpyellow2")
toolMap["tpyellow2"].configure(command=setTool_tpy2)

initTools()

setToolSelected("start")

buttons = createButtons(5,5)
print(buttons)


mainloop()
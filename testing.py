from guiConstruction import Main_Window, Sub_Window, Label, Image, Button

def testRoutine():
    label.setText("TEST SUCCESSFUL")

mainWin = Main_Window("[TEST]", 1000, 1000)
subWin = Sub_Window("[TEST2]", 1000, 1000)

label = Label(mainWin.lay, "VERY VERY VERY LONG TEXT THIS IS LONG TEXT ", "C")
label2 = Label(mainWin.lay, "test left", "L")
label3 = Label(mainWin.lay, "test right", "R")

image = Image(subWin.lay, "pyQT-GUI-Construction-Tool/images/sunset_ocean.jpg", 200, 220, True, "L")
image2 = Image(subWin.lay, "pyQT-GUI-Construction-Tool/images/sunset.jpg", 270, 200, True, "C")
image3 = Image(subWin.lay, "pyQT-GUI-Construction-Tool/images/darth_fader.jpeg", 200, 200, True, "R")

button = Button(mainWin.lay, testRoutine, "click")

mainWin.app.exit(mainWin.app.exec_())
from guiConstruction import Main_Window, Sub_Window, Label, Image, Button

def testRoutine():
    label.setText("TEST SUCCESSFUL")

mainWin = Main_Window("[TEST]", 1000, 1000)
subWin = Sub_Window("[TEST2]", 500, 500)

label = Label(mainWin.lay, "VERY VERY VERY LONG TEXT THIS IS LONG TEXT ")

image = Image(mainWin.lay, "pyQT-GUI-Construction-Tool/images/sunset_ocean.jpg", 200, 220, True)

button = Button(mainWin.lay, testRoutine, "click")

mainWin.app.exit(mainWin.app.exec_())
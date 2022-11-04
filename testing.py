from guiConstruction import Application, Window, Label, Image, Button, Layout

def testRoutine():
    label.setText("TEST SUCCESSFUL")

mainApp = Application()
mainWin = Window("[test]", 1000, 1000)
mainLayout = Layout(mainWin)

label = Label(mainLayout, "VERY VERY VERY LONG TEXT THIS IS LONG TEXT")

image = Image(mainLayout, "pyQT-GUI-Construction-Tool/images/sunset_ocean.jpg")

button = Button(mainLayout, testRoutine, "click")

mainApp.exit(mainApp.exec_())
from guiConstruction import Application, Window, Label, Image, Button

def testRoutine():
    label.setText("TEST SUCCESSFUL")

mainApp = Application()
mainWin = Window("[test]",1000, 1000)

label = Label(mainWin, "test", 50, 50, 50, 50)

image = Image(mainWin, "pyQT-GUI-Construction-Tool/images/sunset_ocean.jpg", 100, 100, 800, 874)

button = Button(mainWin, testRoutine, "click", 150, 50, 50, 50)

mainApp.exit(mainApp.exec_())
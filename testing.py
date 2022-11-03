from guiConstruction import Application, Window, Label, Image

mainApp = Application()
mainWin = Window()
subWin = Window()
sub2Win = Window()

label = Label(mainWin, "test", 50, 50, 50, 50)
label2 = Label(subWin, "test2", 100, 100, 50, 50)
label3 = Label(sub2Win, "chromebooks are bad", 300, 300, 50, 50)

image = Image(mainWin, "pyQT-GUI-Construction-Tool/images/sunset.jpg", 100, 100, 100, 100)

mainApp.exit(mainApp.exec_())
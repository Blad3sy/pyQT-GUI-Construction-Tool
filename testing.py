from guiConstruction import Application, Window, Label, Image

mainApp = Application()
mainWin = Window("imageTest",1000, 1000)
subWin = Window("secondWinTest", 600, 600)
sub2Win = Window("lengthTest", 500, 500)

label = Label(mainWin, "test", 50, 50, 50, 50)
label2 = Label(subWin, "test2", 100, 100, 50, 50)
label3 = Label(sub2Win, "chromebooks are bad", 100, 100, 50, 50)

image = Image(mainWin, "pyQT-GUI-Construction-Tool/images/sunset_ocean.jpg", 100, 100, 800, 874)

mainApp.exit(mainApp.exec_())
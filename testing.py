from guiConstruction import Application, Window, Label

mainApp = Application()
mainWin = Window()
subWin = Window()
sub2Win = Window()

label = Label(mainWin, "test", 50, 50)
label2 = Label(subWin, "test2", 100, 100)
label3 = Label(sub2Win, "chromebooks", 300, 300)

mainApp.exit(mainApp.exec_())
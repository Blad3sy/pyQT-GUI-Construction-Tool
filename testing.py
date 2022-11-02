from guiConstruction import Application, Window, Label

mainApp = Application()
mainWin = Window()

label = Label(mainWin)

mainWin.show()
mainApp.exit(mainApp.exec_())
from tkinter import *

class HolaButton():
    def __init__(self, parent=None, **config):

        self.myParent = parent
        self.myParent.geometry("300x300")
        button = Button(self.myParent, **config)
        button.pack()
        button.config(command=self.callback)

    def callback(self):
        print('Adiós...')
        self.myParent.quit()

if __name__ == '__main__':
    root = Tk()
    miAplicacion = HolaButton(root, text='Hello subclass world')
    root.mainloop()




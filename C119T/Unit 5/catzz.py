from Tkinter import *

import Tkinter.messagebox as bx

wind = Tk()

wind.title( 'Music checkbox' )

fram = Frame( wind )

var1 = IntVar()

var2 = IntVar()

var3 = IntVar()

var4 = IntVar()

music1 = Checkbutton( fram , text = 'Beatles' , variable = var1 , onvalue = 1 , offvalue = 0 )

music2 = Checkbutton( fram , text = 'Temptations' , variable = var2 , onvalue = 1 , offvalue = 0 )

music3 = Checkbutton( fram , text = 'Elvis' , variable = var3 , onvalue = 1 , offvalue = 0 )

music4 = Checkbutton( fram , text = 'Aretha' , variable = var4 , onvalue = 1 , offvalue = 0 )

def radchkbox() :

                strvar = 'Choose your selections():'

                if var1.get() == 1 : strvar += '\n She Loves You'

                if var2.get() == 1 : strvar += '\n My Girl'

                if var3.get() == 1 : strvar += '\n Hounddog'

                if var4.get() == 1 : strvar += '\n Respect'

                bx.showinfo( 'Your Selection' , strvar )

butn = Button( fram , text = 'Choice' , command = radchkbox )

butn.pack( side = RIGHT , padx = 10 )

music1.pack( side = LEFT )

music2.pack( side = LEFT )

music3.pack( side = LEFT )

music4.pack( side = LEFT )

fram.pack( padx = 35, pady = 35 )

wind.mainloop()

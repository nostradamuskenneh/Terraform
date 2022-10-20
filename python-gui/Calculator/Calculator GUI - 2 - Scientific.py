from tkinter import *
from tkinter import ttk
import time
from tkinter import messagebox
import sys

# this is the main root or main window
root = Tk()
# this is the app title
root.title("TIA CALCULATOR")
root.resizable(0, 0)

# globe variable.
font_1 = "Helvertica"
h = 16
style = "italic"

fg_1 = "white"
fg_2 = "black"
fg_on = "red"
fg_off = "blue"
fg_exit = "light blue"
color = "grey"
borderwidth_1 = 2
relief_1 = "ridge"

# '#454545' ,

# flat, groove, raised, ridge, solid, or sunken
# bold
# italic

# Helvertica
# white
# beige
# light blue
# grey
# lavender
# olive


class Application(Frame):
    def __init__(self, master, **kw):  # to initialize this window
        super().__init__(master, **kw)
        self.master = master

        # DISPLAY
        self.display = Entry(self.master,
                             font=(font_1, 45),
                             relief=SUNKEN,
                             justify=RIGHT,
                             bg='#ddffee', bd=10, width=8)
        # self.display.insert(0,"0")
        # self.display.focus()
        self.display.grid(row=1, column=0, columnspan=4)
        self.master.iconbitmap("m1.ICO")

        # ROW 1
        self.but1 = Button(self.master,
                           bg=color,
                           text="sin", fg=fg_1,
                           font=(font_1, h, style),
                           relief=relief_1,
                           command=lambda: self.appendeTodisplay("sin"),
                           borderwidth=borderwidth_1)
        self.but1.grid(row=2, column=0, sticky="NWNESWSE")

        self.but2 = Button(self.master,
                           bg=color,
                           text="cos",
                           fg=fg_1,
                           font=(font_1, h, style),
                           relief=relief_1,
                           borderwidth=borderwidth_1)
        self.but2.grid(row=2, column=1, sticky="NWNESWSE")

        self.but3 = Button(self.master,
                           bg=color,
                           text="tan", fg=fg_1,
                           font=(font_1, h, style),
                           relief=relief_1,
                           borderwidth=borderwidth_1)
        self.but3.grid(row=2, column=2, sticky="NWNESWSE")

        self.but4 = Button(self.master,
                           bg=color,
                           text="  on  ",
                           fg=fg_on,
                           font=(font_1, h, style),
                           relief=relief_1,
                           command=lambda: self.Onbuttom(),
                           borderwidth=borderwidth_1)
        self.but4.grid(row=2, column=3, sticky="NWNESWSE")

        # ROW 2
        self.but5 = Button(self.master,
                           bg=color,
                           text="csc",
                           fg=fg_1,
                           font=(font_1, h, style),
                           relief=relief_1,
                           borderwidth=borderwidth_1)
        self.but5.grid(row=3, column=0, sticky="NWNESWSE")

        self.but6 = Button(self.master,
                           bg=color,
                           text="sec",
                           fg=fg_1,
                           font=(font_1, h, style),
                           relief=relief_1,
                           borderwidth=borderwidth_1)
        self.but6.grid(row=3, column=1, sticky="NWNESWSE")

        self.but7 = Button(self.master,
                           bg=color,
                           text="cot",
                           fg=fg_1,
                           font=(font_1, h, style),
                           relief=relief_1,
                           borderwidth=borderwidth_1)
        self.but7.grid(row=3, column=2, sticky="NWNESWSE")

        self.but8 = Button(self.master,
                           bg=color,
                           text="  off  ",
                           fg=fg_off,
                           font=(font_1, h, style),
                           relief=relief_1,
                           command=lambda: self.Offbuttom(),
                           borderwidth=borderwidth_1)
        self.but8.grid(row=3, column=3, sticky="NWNESWSE")

        # ROW 3
        self.but9 = Button(self.master,
                           bg=color,
                           text="asinh ",
                           fg=fg_1,
                           font=(font_1, h, style),
                           relief=relief_1,
                           borderwidth=borderwidth_1)
        self.but9.grid(row=4, column=0, sticky="NWNESWSE")

        self.but10 = Button(self.master,
                            bg=color,
                            text="acosh",
                            fg=fg_1,
                            font=(font_1, h, style),
                            relief=relief_1,
                            borderwidth=borderwidth_1)
        self.but10.grid(row=4, column=1, sticky="NWNESWSE")

        self.but11 = Button(self.master,
                            bg=color,
                            text="atanh",
                            fg=fg_1,
                            font=(font_1, h, style),
                            relief=relief_1,
                            borderwidth=borderwidth_1)
        self.but11.grid(row=4, column=2, sticky="NWNESWSE")

        self.but12 = Button(self.master,
                            bg=color,
                            text="exit",
                            fg=fg_exit,
                            font=(font_1, h, style),
                            relief=relief_1,
                            command=self.iExit,
                            borderwidth=borderwidth_1)
        self.but12.grid(row=4, column=3, sticky="NWNESWSE")

        # ROW 4
        self.but13 = Button(self.master,
                            bg=color,
                            text="exp",
                            fg=fg_1,
                            font=(font_1, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("exp"),
                            borderwidth=borderwidth_1)
        self.but13.grid(row=5, column=0, sticky="NWNESWSE")

        self.but14 = Button(self.master,
                            bg=color,
                            text="deg",
                            fg=fg_1,
                            font=(font_1, h, style),
                            relief=relief_1,
                            borderwidth=borderwidth_1)
        self.but14.grid(row=5, column=1, sticky="NWNESWSE")

        self.but15 = Button(self.master,
                            bg=color,
                            text="←",
                            fg=fg_1,
                            font=(font_1, h, style),
                            command=lambda: self.Rbutton(),
                            relief=relief_1,
                            borderwidth=borderwidth_1)
        self.but15.grid(row=5, column=2, sticky="NWNESWSE")

        self.but16 = Button(self.master,
                            bg=color,
                            text="  C  ",
                            fg=fg_1,
                            font=(font_1, h, style),
                            relief=relief_1,
                            command=lambda: self.clearText(),
                            borderwidth=borderwidth_1)
        self.but16.grid(row=5, column=3, sticky="NWNESWSE")

        # ROW 5
        self.but17 = Button(self.master,
                            bg=color,
                            text="e",
                            fg=fg_1,
                            font=(font_1, h, style),
                            relief=relief_1,
                            borderwidth=borderwidth_1)
        self.but17.grid(row=6, column=0, sticky="NWNESWSE")

        self.but18 = Button(self.master,
                            bg=color,
                            text="log",
                            fg=fg_1,
                            font=(font_1, h, style),
                            relief=relief_1,
                            borderwidth=borderwidth_1)
        self.but18.grid(row=6, column=1, sticky="NWNESWSE")

        self.but19 = Button(self.master,
                            bg=color,
                            text="pi",
                            fg=fg_1,
                            font=(font_1, h, style),
                            relief=relief_1,
                            command=self.pi,
                            borderwidth=borderwidth_1)
        self.but19.grid(row=6, column=2, sticky="NWNESWSE")

        self.but20 = Button(self.master,
                            bg=color,
                            text="  %  ",
                            fg=fg_1,
                            font=(font_1, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("%"),
                            borderwidth=borderwidth_1)
        self.but20.grid(row=6, column=3, sticky="NWNESWSE")

        # ROW 6
        self.but21 = Button(self.master,
                            bg=color,
                            text="√",
                            fg=fg_2,
                            font=(font_1, h, style),
                            relief=relief_1,
                            borderwidth=borderwidth_1)
        self.but21.grid(row=7, column=0, sticky="NWNESWSE")

        self.but22 = Button(self.master,
                            bg=color,
                            text="(",
                            fg=fg_2,
                            font=(font_1, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("("),
                            borderwidth=borderwidth_1)
        self.but22.grid(row=7, column=1, sticky="NWNESWSE")

        self.but23 = Button(self.master,
                            bg=color,
                            text=")",
                            fg=fg_2,
                            font=(font_1, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay(")"),
                            borderwidth=borderwidth_1)
        self.but23.grid(row=7, column=2, sticky="NWNESWSE")

        self.but24 = Button(self.master,
                            bg=color,
                            text="  +  ",
                            fg=fg_2,
                            font=(font_1, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("+"),
                            borderwidth=borderwidth_1)
        self.but24.grid(row=7, column=3, sticky="NWNESWSE")

        # ROW 7
        self.but25 = Button(self.master,
                            bg=color,
                            text="7",
                            fg=fg_2,
                            font=(font_1, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("7"),
                            borderwidth=borderwidth_1)
        self.but25.grid(row=8, column=0, sticky="NWNESWSE")

        self.but26 = Button(self.master,
                            bg=color,
                            text="8",
                            fg=fg_2,
                            font=(font_1, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("8"),
                            borderwidth=borderwidth_1)
        self.but26.grid(row=8, column=1, sticky="NWNESWSE")

        self.but27 = Button(self.master,
                            bg=color,
                            text="9",
                            fg=fg_2,
                            font=(font_1, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("9"),
                            borderwidth=borderwidth_1)
        self.but27.grid(row=8, column=2, sticky="NWNESWSE")

        self.but28 = Button(self.master,
                            bg=color,
                            text="  ÷  ",
                            fg=fg_2,
                            font=(font_1, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("/"),
                            borderwidth=borderwidth_1)
        self.but28.grid(row=8, column=3, sticky="NWNESWSE")

        # ROW 8
        self.but29 = Button(self.master,
                            bg=color,
                            text="4",
                            fg=fg_2,
                            font=(font_1, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("4"),
                            borderwidth=borderwidth_1)
        self.but29.grid(row=9, column=0, sticky="NWNESWSE")

        self.but30 = Button(self.master,
                            bg=color,
                            text="5",
                            fg=fg_2,
                            font=(font_1, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("5"),
                            borderwidth=borderwidth_1)
        self.but30.grid(row=9, column=1, sticky="NWNESWSE")

        self.but31 = Button(self.master,
                            bg=color,
                            text="6",
                            fg=fg_2,
                            font=(font_1, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("6"),
                            borderwidth=borderwidth_1)
        self.but31.grid(row=9, column=2, sticky="NWNESWSE")

        self.but32 = Button(self.master,
                            bg=color,
                            text="  x  ",
                            fg=fg_2,
                            font=(font_1, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("*"),
                            borderwidth=borderwidth_1)
        self.but32.grid(row=9, column=3, sticky="NWNESWSE")

        # ROW 9
        self.but33 = Button(self.master,
                            bg=color,
                            text="1",
                            fg=fg_2,
                            font=(font_1, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("1"),
                            borderwidth=borderwidth_1)
        self.but33.grid(row=10, column=0, sticky="NWNESWSE")

        self.but34 = Button(self.master,
                            bg=color,
                            text="2",
                            fg=fg_2,
                            font=(font_1, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("2"),
                            borderwidth=borderwidth_1)
        self.but34.grid(row=10, column=1, sticky="NWNESWSE")

        self.but35 = Button(self.master,
                            bg=color,
                            text="3",
                            fg=fg_2,
                            font=(font_1, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("3"),
                            borderwidth=borderwidth_1)
        self.but35.grid(row=10, column=2, sticky="NWNESWSE")

        self.but36 = Button(self.master,
                            bg=color,
                            text="  -  ",
                            fg=fg_2,
                            font=(font_1, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("-"),
                            borderwidth=borderwidth_1)
        self.but36.grid(row=10, column=3, sticky="NWNESWSE")

        # ROW 10
        self.but37 = Button(self.master,
                            bg=color,
                            text="0",
                            fg=fg_2,
                            font=(font_1, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("0"),
                            borderwidth=borderwidth_1)
        self.but37.grid(row=11, column=0, sticky="NWNESWSE")

        self.but38 = Button(self.master,
                            bg=color,
                            text="±",
                            fg=fg_2,
                            font=(font_1, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("±"),
                            borderwidth=borderwidth_1)
        self.but38.grid(row=11, column=1, sticky="NWNESWSE")

        self.but39 = Button(self.master,
                            bg=color, text=".",
                            fg=fg_2,
                            font=(font_1, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("."),
                            borderwidth=borderwidth_1)
        self.but39.grid(row=11, column=2, sticky="NWNESWSE")

        self.but40 = Button(self.master,
                            bg=color,
                            text="  =  ",
                            fg=fg_2,
                            font=(font_1, h, style),
                            relief=relief_1,
                            command=lambda: self.CalculateExpression(),
                            borderwidth=borderwidth_1)
        self.but40.grid(row=11, column=3, sticky="NWNESWSE")

        self.label = Label(
            self.master, text="scientific calculator", bg='#b5b5b5')
        self.label.grid(row=0, column=0, sticky="NWNESWSE", columnspan=4)

    def Offbuttom(self):
        self.display.delete(0, END)
        self.display.insert(0, "")
        self.but1.config(state=DISABLED)
        self.but2.config(state=DISABLED)
        self.but3.config(state=DISABLED)
        #self.but4.config(state = DISABLED)
        self.but5.config(state=DISABLED)
        self.but6.config(state=DISABLED)
        self.but7.config(state=DISABLED)
        #self.but8.config(state = DISABLED)
        self.but9.config(state=DISABLED)
        self.but10.config(state=DISABLED)
        self.but11.config(state=DISABLED)
        #self.but12.config(state = DISABLED)
        self.but13.config(state=DISABLED)
        self.but14.config(state=DISABLED)
        self.but15.config(state=DISABLED)
        self.but16.config(state=DISABLED)
        self.but17.config(state=DISABLED)
        self.but18.config(state=DISABLED)
        self.but19.config(state=DISABLED)
        self.but20.config(state=DISABLED)
        self.but21.config(state=DISABLED)
        self.but22.config(state=DISABLED)
        self.but23.config(state=DISABLED)
        self.but24.config(state=DISABLED)
        self.but25.config(state=DISABLED)
        self.but26.config(state=DISABLED)
        self.but27.config(state=DISABLED)
        self.but28.config(state=DISABLED)
        self.but29.config(state=DISABLED)
        self.but30.config(state=DISABLED)
        self.but31.config(state=DISABLED)
        self.but32.config(state=DISABLED)
        self.but33.config(state=DISABLED)
        self.but34.config(state=DISABLED)
        self.but35.config(state=DISABLED)
        self.but36.config(state=DISABLED)
        self.but37.config(state=DISABLED)
        self.but38.config(state=DISABLED)
        self.but39.config(state=DISABLED)
        self.but40.config(state=DISABLED)

    def Onbuttom(self):
        self.display.insert(0, "0")
        self.but1.config(state=NORMAL)
        self.but2.config(state=NORMAL)
        self.but3.config(state=NORMAL)
        #self.but4.config(state = NORMAL)
        self.but5.config(state=NORMAL)
        self.but6.config(state=NORMAL)
        self.but7.config(state=NORMAL)
        #self.but8.config(state = NORMAL)
        self.but9.config(state=NORMAL)
        self.but10.config(state=NORMAL)
        self.but11.config(state=NORMAL)
        #self.but12.config(state = NORMAL)
        self.but13.config(state=NORMAL)
        self.but14.config(state=NORMAL)
        self.but15.config(state=NORMAL)
        self.but16.config(state=NORMAL)
        self.but17.config(state=NORMAL)
        self.but18.config(state=NORMAL)
        self.but19.config(state=NORMAL)
        self.but20.config(state=NORMAL)
        self.but21.config(state=NORMAL)
        self.but22.config(state=NORMAL)
        self.but23.config(state=NORMAL)
        self.but24.config(state=NORMAL)
        self.but25.config(state=NORMAL)
        self.but26.config(state=NORMAL)
        self.but27.config(state=NORMAL)
        self.but28.config(state=NORMAL)
        self.but29.config(state=NORMAL)
        self.but30.config(state=NORMAL)
        self.but31.config(state=NORMAL)
        self.but32.config(state=NORMAL)
        self.but33.config(state=NORMAL)
        self.but34.config(state=NORMAL)
        self.but35.config(state=NORMAL)
        self.but36.config(state=NORMAL)
        self.but37.config(state=NORMAL)
        self.but38.config(state=NORMAL)
        self.but39.config(state=NORMAL)
        self.but40.config(state=NORMAL)

    def Rbutton(self):
        # self.display.delete(0,END)
        # self.display.configure(justify=LEFT)
        self.display.delete(0, 1)

    def replaceText(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)

    def appendeTodisplay(self, text):
        self.EntryText = self.display.get()
        self.textLength = len(self.EntryText)

        if self.EntryText == "0":
            self.replaceText(text)

        else:
            self.display.insert(self.textLength, text)

    def clearText(self):
        self.replaceText("0")

    def CalculateExpression(self):
        self.expression = self.display.get()
        # we have to replace all the %/100 so that typton will not considere it as modulo.
        self.expression = self.expression.replace("%", "/100")
        self.result = eval(self.expression)
        # self.replaceText(self.result)# this will put the result on the screen

        try:
            self.result = eval(self.expression)
            self.replaceText(self.result)

        except:
            messagebox.showinfo("Error", "Invalid Input")

        # print(self.result)# it will print the result on the consel when we press equal for verification

    def pi(self):
        self. result = False
        self.current = math.pi
        self.displad(self.current)
# ==============================================================================================
# Sign out button function

    def iExit(self):
        self.qExit = messagebox.askyesno("Calculator",
                                         "Are you sure that you want to close?",
                                         icon="warning")
        if self.qExit > 0:
            self.master.destroy()
            return


# ==============================================================================================


def main():
    app = Application(root)
    root.mainloop()


if __name__ == '__main__':
    main()

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import time
import datetime
from tkinter import Menu
from tkinter import scrolledtext

# TITLE GLOBE VARIABLE
bd_main_frame = 50
h2 = 18
style_title = "bold"
# APPLICATION GLOBE VARIABLES
h1 = 14
bd_app_frames = 4
style_app = ""
font_1 = "Time"

relief_1 = RIDGE
Width_Label = "0"
Width_Entry = 25

sticky_label = 'w'
sticky_Entry = 'e' + 'w'
sticky_label_cost = E

pad_x_total = 3
pad_x_all = 2

pad_y = "4"

space_items_cost = "\t"
space_entry = "\t"
space_button = "\n"

Width_entry = 6
justify_entry = RIGHT
state_entry = DISABLED

# the value can be any number
on_value_1 = 1
off_value_1 = 0
Line = "___________________________________________"


# FLAT, RAISED, SUNKEN, GROOVE, RIDGE
# style = "italic"
# style = "bold"


class login:
    def __init__(self, master):  # to initialize this window
        self.master = master
        self.master.resizable(False, False)
        self.master.title("LOGIN SYSTEM")
        self.master.config(bg="powder blue")

        # Variables declaration (for the rest button)
        self.entry_Username = StringVar()
        self.entry_Password = StringVar()

        self.label = ttk.Label(self.master, text='Username',
                               background="powder blue", font=('Time', 10))
        self.label.grid(row=0, column=0, pady=10, padx=1)

        self.label = ttk.Label(self.master, text='Password',
                               background="powder blue", font=('Time', 10))
        self.label.grid(row=1, column=0, pady=5, padx=1)

        self.entry_Username = ttk.Entry(
            self.master, width=25, font=('Time', 10))
        # this put the cursor in the entry name when we run the program
        self.entry_Username.focus()
        self.entry_Password = ttk.Entry(
            self.master, width=25, font=('Time', 10))
        self.entry_Password.config(show='*')  # this is to hid the password
        self.entry_Username.grid(
            row=0, column=1, padx=1, columnspan=2, sticky='e' + 'w')  # to expand the Entry
        self.entry_Password.grid(
            row=1, column=1, padx=1, columnspan=2, sticky='e' + 'w')

        self.label = Label(self.master, text='', background="powder blue")
        self.label.grid(row=2, column=0, columnspan=3, sticky='e' + 'w')

        self.btn1 = ttk.Button(self.master, text='Login',
                               command=self.Login_System)
        master.bind('<Return>', self.Login_System)
        self.btn1.grid(row=3, column=0, sticky='e' + 'w', pady=1, padx=1)
        self.btn2 = ttk.Button(self.master, text='Reset', command=self.Reset)
        master.bind('<Control-r>', self.Reset)
        self.btn2.grid(row=3, column=1, sticky='e' + 'w', pady=1, padx=30)
        self.btn3 = ttk.Button(self.master, text='Exit', command=self.iExit)
        master.bind('<Control-e>', self.iExit)
        self.btn3.grid(row=3, column=2, sticky='e' + 'w', pady=1, padx=1)

    # Login system passwords
    def Login_System(self, event=None):  # event can be None or "" (empty string)
        username = (self.entry_Username.get())
        password = (self.entry_Password.get())

        if (username == str("leo.tia")) or (password == str("tia12345")):  # tia12345 most be a string
            self.restaurant_window = Toplevel(self.master)
            self.app = Restaurant_Management_System(self.restaurant_window)

        if (username == str("s4gene")) and (password == str("12345")):  # tia12345 most be a string
            self.restaurant_window = Toplevel(self.master)
            self.app = Restaurant_Management_System(self.restaurant_window)

        # elif (username == str("1")) and (password == str(1)):  # tia12345 most be a string
        #     self.restaurant_window = Toplevel(self.master)
        #     self.app = Restaurant_Management_System(self.restaurant_window)

        # elif (username == str("2")) or (username == str("3")) and (password == str("2")) or (
        #         password == str(3)):  # tia12345 most be a string
        #     self.restaurant_window = Toplevel(self.master)
        #     self.app = Restaurant_Management_System(self.restaurant_window)

        # elif (username == str("4")) or (username == str("5")) and (password == str(4)) or (
        #         password == str(5)):  # tia12345 most be a string
        #     self.restaurant_window = Toplevel(self.master)
        #     self.app = Restaurant_Management_System(self.restaurant_window)

        # elif (username == str("5")) and (password == str(5)):
        #     self.restaurant_window = Toplevel(self.master)
        #     self.app = Restaurant_Management_System(self.restaurant_window)

        else:
            messagebox.askretrycancel("Hospital Login System", "Invalid password or username",
                                      icon="error")  # put this first

            # self.entry_Username.set("")
            # self.entry_Password.set("")# this set the entry to zero if wrong password or username
            self.entry_Username.focus()  # put the cursor in the username entry

    def Restaurant_System(self):
        self.restaurant_window = Toplevel(self.master)
        self.app = Restaurant_Management_System(self.restaurant_window)

    def iExit(self, event=""):
        self.qExit = messagebox.askyesno("Hospital Login System",
                                         "This system is still running.\n"
                                         "Are you sure that you want to sign out?",
                                         icon="warning")
        if self.qExit > 0:
            self.master.destroy()
            return

    # Reset button function
    # self.entry_Username = StringVar()
    # self.entry_Password = StringVar()

    def Reset(self, event=""):
        self.entry_Username.delete(0, 'end')
        self.entry_Password.delete(0, 'end')
        # this set the entry to zero if wrong password or username
        self.entry_Username.focus()


# ==============================================================================================
class Restaurant_Management_System:
    def __init__(self, master):  # to initialize this window
        self.master = master
        # self.master.resizable(False, False)
        self.master.title("LOGIN SYSTEM")
        master.title('Restaurant Management System')
        # master.resizable(False, False)

        # -------------------------------------------------------------------------------------------------------------------
        # TODO FRAMES
        self.main_frame = Frame(self.master, bd=10, relief=RIDGE)
        self.main_frame.pack()

        self.Top_frame = Frame(self.main_frame)
        self.Top_frame.pack(side=TOP)

        self.Logo_frame = Frame(self.Top_frame)
        self.Logo_frame.pack(side=LEFT)

        self.Top_frame_left = Frame(self.Top_frame)
        self.Top_frame_left.pack(side=LEFT)

        self.Top_frame_middle = Frame(self.Top_frame)
        self.Top_frame_middle.pack(side=LEFT)

        self.Top_frame_right = Frame(self.Top_frame)
        self.Top_frame_right.pack(side=RIGHT)

        self.Data_left_frame = Frame(
            self.main_frame, bd=bd_app_frames, relief=relief_1)
        self.Data_left_frame.pack(side=LEFT)

        self.Data_middle_frame = Frame(
            self.main_frame, bd=bd_app_frames, relief=relief_1)
        self.Data_middle_frame.pack(side=LEFT)

        self.Data_right_frame = Frame(
            self.main_frame, bd=bd_app_frames, relief=relief_1)
        self.Data_right_frame.pack(side=LEFT)

        self.DataReceipt = LabelFrame(self.main_frame,
                                      relief=relief_1,
                                      bd=bd_app_frames,
                                      font=(font_1, h2, style_title),
                                      text="Customer Receipt")
        self.DataReceipt.pack(side=RIGHT)

        # Using a scrolled Text control
        scroll_W = 21
        scroll_H = 23
        scr = scrolledtext.ScrolledText(self.DataReceipt,
                                        font=("Time", 14),
                                        width=scroll_W,
                                        height=scroll_H,
                                        wrap=WORD)
        scr.grid(column=0, sticky='WE', row=0)
        scr.focus()

        # self.images_frame = Frame(self.main_frame)
        # self.images_frame.pack(side=BOTTOM)

        # -------------------------------------------------------------------------------------------------------------------
        # TODO MENU BAR
        def exit():
            qExit = messagebox.askyesno("Fast Food",
                                        "This system is still running.\n\n"
                                        "Do you want to quit?", icon="warning")
            if qExit > 0:
                master.destroy()
                return

        menuBar = Menu(master)
        master.config(menu=menuBar)
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="Print Customer Receipt")
        fileMenu.add_separator()
        fileMenu.add_command(label="Open File")
        fileMenu.add_separator()
        fileMenu.add_command(label="Save Files")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit the System", command=exit)
        menuBar.add_cascade(label="File", menu=fileMenu)

        # Add another Menu to the Menu Bar and an item
        ApplicationsMenu = Menu(menuBar, tearoff=0)
        ApplicationsMenu.add_command(label="Calculator", command=self.Cal)
        ApplicationsMenu.add_separator()
        ApplicationsMenu.add_command(label="Feedback", command=self.Feedback)
        menuBar.add_cascade(label="Applications", menu=ApplicationsMenu)

        ApplicationsMenu = Menu(menuBar, tearoff=0)
        ApplicationsMenu.add_command(label="Calc", command=self.Cal)
        menuBar.add_cascade(label="Calculation",
                            menu=ApplicationsMenu, command=self.Cal)

        # # Tab Control introduced here -----------------------------------------
        #
        # tabControl = ttk.Notebook(master)  # Create Tab Control
        #
        # tab1 = ttk.Frame(tabControl)  # Create a tab
        # tabControl.add(tab1, text='Find and replace')  # Add the tab
        #
        # tab2 = ttk.Frame(tabControl)  # Add a second tab
        # tabControl.add(tab2, text='Time & Date')  # Make second tab visible
        #
        # tab3 = ttk.Frame(tabControl)  # Add a second tab
        # tabControl.add(tab3, text='Text Entry')  # Make second tab visible
        #
        # tabControl.pack(fill="x", side=TOP)  # Pack to make visible
        #
        # frame_image = Frame(tab2)
        # frame_image.pack()
        # logo3 = PhotoImage(file="sandwich.PNG").subsample(5, 5)
        # L1 = Label(frame_image, text='TIA')
        # L1.pack()

        # ----------------------------------------------------------------------------------------
        # TODO MENU BAR

        toolbar = Frame(self.master, bg="gray")

        # logo1 = PhotoImage(file='printer.png').subsample(1, 1)
        # printButton = ttk.Button(toolbar, width=1)
        # printButton.pack(side=LEFT, padx=2, pady=2)
        # printButton.config(image=logo1, compound=LEFT)

        Sandwich = PhotoImage(file='sandwich.png').subsample(6, 6)
        button = ttk.Button(toolbar, text='TIA')
        button.pack(side=LEFT, padx=2, pady=2)
        button.config(image=Sandwich)

        toolbar.pack(fill=X, side=TOP)

        # ----------------------------------------------------------------------------------------

        def cost_of_meal(event=""):
            meal1 = float(varFries.get())
            meal2 = float(varSalad.get())
            meal3 = float(varHamburger.get())
            meal4 = float(varOnionRings.get())
            meal5 = float(varChickenSalad.get())
            meal6 = float(varFishSandwich.get())
            meal7 = float(varCheeseSandwich.get())
            meal8 = float(varChickenSandwich.get())

            meal9 = float(varHashBrown.get())
            meal10 = float(varToastedBagel.get())
            meal11 = float(varPancakesSyrup.get())
            meal12 = float(varPineappleStick.get())
            meal13 = float(varChocolateMuffin.get())

            meal14 = float(varTea.get())
            meal15 = float(varCola.get())
            meal16 = float(varCoffee.get())
            meal17 = float(varOrange.get())
            meal18 = float(varBottleWater.get())
            meal19 = float(varVanillaCone.get())
            meal20 = float(varVanillaShake.get())
            meal21 = float(varStrawberryShake.get())

            iTotal1 = ((meal1 * 1.20) + (meal2 * 2.10) + (meal3 * 3.30) + (meal4 * 1.30) + (meal5 * 3.50) + (
                meal6 * 3.60))
            iTotal2 = ((meal7 * 3.40) + (meal8 * 3.60) + (meal9 * 1.40) + (meal10 * 1.60) + (meal11 * 1.20) + (
                meal12 * 1.40))
            iTotal3 = ((meal13 * 2.40) + (meal14 * 1.50) +
                       (meal15 * 1.30) + (meal16 * 1.59) + (meal17 * 1.20))
            iTotal4 = ((meal18 * 0.99) + (meal19 * 2.10) +
                       (meal20 * 2.10) + (meal21 * 2.20))

            if (self.payment_Method.get() == ""):
                messagebox.showwarning(
                    "Payment method", "Choose a payment method first")

            elif (self.payment_Method.get() == "Cash"):
                iCost = (iTotal1 + iTotal2 + iTotal3 + iTotal4)
                iTax = (iCost * 3.4) / 100
                iTotal = (iCost + iTax)

                # 2f means 2 letters after the comma
                iCost_q = str("%.2f" % iCost)
                iCost_q = '$', str(iCost_q)  # this is to put the dollar symbol

                iTax_q = str("%.2f" % iTax)
                iTax_q = '$', str(iTax_q)

                iTotal_q = str("%.2f" % iTotal)
                iTotal_q = '$', str(iTotal_q)

                var22.set(iTax_q)
                var23.set(iCost_q)
                var24.set(iTotal_q)

                self.e3.configure(state=NORMAL)
                self.e4.configure(state=NORMAL)
                self.e5.configure(state=NORMAL)
                self.e2.configure(state=NORMAL)

                self.e2.delete(0, END)
                self.e2.focus()

            elif (self.payment_Method.get() == "Master Card"):
                iCost = (iTotal1 + iTotal2 + iTotal3 + iTotal4)
                iTax = (iCost * 3.4) / 100
                iTotal = (iCost + iTax)

                # 2f means 2 letters after the comma
                iCost_q = str("%.2f" % iCost)
                iCost_q = '$', str(iCost_q)  # this is to put the dollar symbol

                iTax_q = str("%.2f" % iTax)
                iTax_q = '$', str(iTax_q)

                iTotal_q = str("%.2f" % iTotal)
                iTotal_q = '$', str(iTotal_q)

                var22.set(iTax_q)
                var23.set(iCost_q)
                var24.set(iTotal_q)

                self.e3.configure(state=NORMAL)
                self.e4.configure(state=NORMAL)
                self.e5.configure(state=NORMAL)
                self.e2.configure(state=DISABLED)

                var27.set('0')
                var25.set('0')
                self.e6.configure(state=DISABLED)

            elif (self.payment_Method.get() == "Master Card"):
                iCost = (iTotal1 + iTotal2 + iTotal3 + iTotal4)
                iTax = (iCost * 3.4) / 100
                iTotal = (iCost + iTax)

                # 2f means 2 letters after the comma
                iCost_q = str("%.2f" % iCost)
                iCost_q = '$', str(iCost_q)  # this is to put the dollar symbol

                iTax_q = str("%.2f" % iTax)
                iTax_q = '$', str(iTax_q)

                iTotal_q = str("%.2f" % iTotal)
                iTotal_q = '$', str(iTotal_q)

                var22.set(iTax_q)
                var23.set(iCost_q)
                var24.set(iTotal_q)

                self.e3.configure(state=NORMAL)
                self.e4.configure(state=NORMAL)
                self.e5.configure(state=NORMAL)
                self.e2.configure(state=DISABLED)

                var27.set('0')
                var25.set('0')
                self.e6.configure(state=DISABLED)

            elif (self.payment_Method.get() == "Visa Card"):
                iCost = (iTotal1 + iTotal2 + iTotal3 + iTotal4)
                iTax = (iCost * 3.4) / 100
                iTotal = (iCost + iTax)

                # 2f means 2 letters after the comma
                iCost_q = str("%.2f" % iCost)
                iCost_q = '$', str(iCost_q)  # this is to put the dollar symbol

                iTax_q = str("%.2f" % iTax)
                iTax_q = '$', str(iTax_q)

                iTotal_q = str("%.2f" % iTotal)
                iTotal_q = '$', str(iTotal_q)

                var22.set(iTax_q)
                var23.set(iCost_q)
                var24.set(iTotal_q)

                self.e3.configure(state=NORMAL)
                self.e4.configure(state=NORMAL)
                self.e5.configure(state=NORMAL)
                self.e2.configure(state=DISABLED)

                var27.set('0')
                var25.set('0')
                self.e6.configure(state=DISABLED)

            elif (self.payment_Method.get() == "Debit Card"):
                iCost = (iTotal1 + iTotal2 + iTotal3 + iTotal4)
                iTax = (iCost * 3.4) / 100
                iTotal = (iCost + iTax)

                # 2f means 2 letters after the comma
                iCost_q = str("%.2f" % iCost)
                iCost_q = '$', str(iCost_q)  # this is to put the dollar symbol

                iTax_q = str("%.2f" % iTax)
                iTax_q = '$', str(iTax_q)

                iTotal_q = str("%.2f" % iTotal)
                iTotal_q = '$', str(iTotal_q)

                var22.set(iTax_q)
                var23.set(iCost_q)
                var24.set(iTotal_q)

                self.e3.configure(state=NORMAL)
                self.e4.configure(state=NORMAL)
                self.e5.configure(state=NORMAL)
                self.e2.configure(state=DISABLED)

                var27.set('0')
                var25.set('0')
                self.e6.configure(state=DISABLED)

            elif (self.payment_Method.get() == "Credit Card"):
                iCost = (iTotal1 + iTotal2 + iTotal3 + iTotal4)
                iTax = (iCost * 3.4) / 100
                iTotal = (iCost + iTax)

                # 2f means 2 letters after the comma
                iCost_q = str("%.2f" % iCost)
                iCost_q = '$', str(iCost_q)  # this is to put the dollar symbol

                iTax_q = str("%.2f" % iTax)
                iTax_q = '$', str(iTax_q)

                iTotal_q = str("%.2f" % iTotal)
                iTotal_q = '$', str(iTotal_q)

                var22.set(iTax_q)
                var23.set(iCost_q)
                var24.set(iTotal_q)

                self.e3.configure(state=NORMAL)
                self.e4.configure(state=NORMAL)
                self.e5.configure(state=NORMAL)
                self.e2.configure(state=DISABLED)

                var27.set('0')
                var25.set('0')
                self.e6.configure(state=DISABLED)

        # --------------------------------------------------------------------------------
        def Change_1():
            if (self.e2.get() == "0"):
                messagebox.showwarning("Payment method", "Your most put cash")

            else:
                meal1 = float(varFries.get())
                meal2 = float(varSalad.get())
                meal3 = float(varHamburger.get())
                meal4 = float(varOnionRings.get())
                meal5 = float(varChickenSalad.get())
                meal6 = float(varFishSandwich.get())
                meal7 = float(varCheeseSandwich.get())
                meal8 = float(varChickenSandwich.get())

                meal9 = float(varHashBrown.get())
                meal10 = float(varToastedBagel.get())
                meal11 = float(varPancakesSyrup.get())
                meal12 = float(varPineappleStick.get())
                meal13 = float(varChocolateMuffin.get())

                meal14 = float(varTea.get())
                meal15 = float(varCola.get())
                meal16 = float(varCoffee.get())
                meal17 = float(varOrange.get())
                meal18 = float(varBottleWater.get())
                meal19 = float(varVanillaCone.get())
                meal20 = float(varVanillaShake.get())
                meal21 = float(varStrawberryShake.get())

                iTotal1 = ((meal1 * 1.20) + (meal2 * 2.10) + (meal3 * 3.30) + (meal4 * 1.30) + (meal5 * 3.50) + (
                    meal6 * 3.60))
                iTotal2 = ((meal7 * 3.40) + (meal8 * 3.60) + (meal9 * 1.40) + (meal10 * 1.60) + (meal11 * 1.20) + (
                    meal12 * 1.40))
                iTotal3 = ((meal13 * 2.40) + (meal14 * 1.50) +
                           (meal15 * 1.30) + (meal16 * 1.59) + (meal17 * 1.20))
                iTotal4 = ((meal18 * 0.99) + (meal19 * 2.10) +
                           (meal20 * 2.10) + (meal21 * 2.20))

                iCost = (iTotal1 + iTotal2 + iTotal3 + iTotal4)
                iTax = (iCost * 3.4) / 100
                iTotal = (iCost + iTax)

                Cash = float(self.e2.get())
                Customer_Change = Cash - iTotal

                iCustomer_Change_q = str("%.3f" % Customer_Change)
                iCustomer_Change_q = '$', str(iCustomer_Change_q)
                var25.set(iCustomer_Change_q)

                self.e6.configure(state=NORMAL)

        # --------------------------------------------------------------------------------
        def Reset():
            varFries.set('0')
            varSalad.set('0')
            varHamburger.set('0')
            varOnionRings.set('0')
            varChickenSalad.set('0')
            varFishSandwich.set('0')
            varCheeseSandwich.set('0')
            varChickenSandwich.set('0')

            varHashBrown.set('0')
            varToastedBagel.set('0')
            varPancakesSyrup.set('0')
            varPineappleStick.set('0')
            varChocolateMuffin.set('0')

            self.e2.delete(0, 'end')  # this to delete the cash entry
            # this is to delete the payment method entry
            self.payment_Method.delete(0, 'end')
            # this is to set the payment method to an empty string
            self.payment_Method.set('')

            var22.set('0')
            var23.set('0')
            var24.set('0')
            var25.set('0')
            var27.set('0')

            varTea.set('0')
            varCola.set('0')
            varCoffee.set('0')
            varOrange.set('0')
            varBottleWater.set('0')
            varVanillaCone.set('0')
            varVanillaShake.set('0')
            varStrawberryShake.set('0')

            self.e3.configure(state=state_entry)
            self.e4.configure(state=state_entry)
            self.e5.configure(state=state_entry)
            self.e6.configure(state=state_entry)
            self.e2.configure(state=state_entry)

            self.entry_fries.configure(state=state_entry)
            self.entry_salad.configure(state=state_entry)
            self.entry_hamburger.configure(state=state_entry)
            self.entry_onion.configure(state=state_entry)
            self.entry_chicken.configure(state=state_entry)
            self.entry_fish.configure(state=state_entry)
            self.entry_cheese.configure(state=state_entry)
            self.entry_chicken_1.configure(state=state_entry)

            self.Fries.deselect()
            self.Salad.deselect()
            self.Hamburger.deselect()
            self.Onion_Rings.deselect()
            self.Chicken_Salad.deselect()
            self.Chicken_Sandwich.deselect()
            self.Cheese_Sandwich.deselect()
            self.Fish_Sandwich.deselect()

            self.E1.configure(state=state_entry)
            self.E2.configure(state=state_entry)
            self.E3.configure(state=state_entry)
            self.E4.configure(state=state_entry)
            self.E5.configure(state=state_entry)
            self.E6.configure(state=state_entry)
            self.E7.configure(state=state_entry)
            self.E8.configure(state=state_entry)

            self.T2.deselect()
            self.T3.deselect()
            self.T4.deselect()
            self.T5.deselect()
            self.T6.deselect()
            self.T8.deselect()
            self.T9.deselect()
            self.T10.deselect()

            self.b1.configure(state=state_entry)
            self.b2.configure(state=state_entry)
            self.b3.configure(state=state_entry)
            self.b4.configure(state=state_entry)
            self.b5.configure(state=state_entry)

            self.B2.deselect()
            self.B3.deselect()
            self.B4.deselect()
            self.B5.deselect()
            self.B6.deselect()

        # ----------------------------------------------------------------------------------------
        # TODO TOP FRAME DATA

        self.label = Label(self.Top_frame_middle, bd="0", relief=relief_1,
                           font=("Time", 27, "italic"),
                           text="\tRestaurant Management System             \t")
        self.label.pack()

        Date_1 = StringVar()
        Date_1.set(time.strftime("%d/%m/%y"))
        self.lbnInfo1 = Label(self.Top_frame_right, font=("arial", 25, "bold"),
                              textvariable=Date_1,
                              fg="steel Blue", bd=10, anchor="w")
        self.lbnInfo1.grid(row=0, column=0)

        def tick():
            time_string = time.strftime("%H:%M:%S")
            self.clock.config(text=time_string)
            self.clock.after(200, tick)

        self.clock = Label(self.Top_frame_left, fg="steel Blue",
                           font=("time", 25, "bold"), anchor="w")
        self.clock.grid(row=0, column=0)
        # we just call the tick function so that it ca display the time.
        tick()

        self.logo = PhotoImage(file="tour.gif").subsample(1, 1)
        self.label = Label(self.Logo_frame, image=self.logo, text="")
        self.label.grid(row=0, column=0)

        self.label_space = Label(self.Logo_frame, text="\t\t\t\t")
        self.label_space.grid(row=0, column=1)

        # ----------------------------------------------------------------------------------------
        # TODO LEFT FRAME DATA

        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()

        varFries = StringVar()
        varSalad = StringVar()
        varHamburger = StringVar()
        varOnionRings = StringVar()
        varChickenSalad = StringVar()
        varFishSandwich = StringVar()
        varCheeseSandwich = StringVar()
        varChickenSandwich = StringVar()

        varFries.set('0')
        varSalad.set('0')
        varHamburger.set('0')
        varOnionRings.set('0')
        varChickenSalad.set('0')
        varFishSandwich.set('0')
        varCheeseSandwich.set('0')
        varChickenSandwich.set('0')

        def chkFries():
            if var1.get() == on_value_1:
                self.entry_fries.configure(state="normal")
                varFries.set("")
                self.entry_fries.focus()
            elif var1.get() == off_value_1:
                self.entry_fries.configure(state=state_entry)
                varFries.set("0")

        def chkSalad():
            if var2.get() == on_value_1:
                self.entry_salad.configure(state="normal")
                varSalad.set("")
                self.entry_salad.focus()
            elif var2.get() == off_value_1:
                self.entry_salad.configure(state=state_entry)
                varSalad.set("0")

        def chkHamburger():
            if var3.get() == on_value_1:
                self.entry_hamburger.configure(state="normal")
                varHamburger.set("")
                self.entry_hamburger.focus()
            elif var3.get() == off_value_1:
                self.entry_hamburger.configure(state=state_entry)
                varHamburger.set("0")

        def chkOnionRings():
            if var4.get() == on_value_1:
                self.entry_onion.configure(state="normal")
                varOnionRings.set("")
                self.entry_onion.focus()
            elif var4.get() == off_value_1:
                self.entry_onion.configure(state=state_entry)
                varOnionRings.set("0")

        def chkChickenSalad():
            if var5.get() == on_value_1:
                self.entry_chicken.configure(state="normal")
                varChickenSalad.set("")
                self.entry_chicken.focus()
            elif var5.get() == off_value_1:
                self.entry_chicken.configure(state=state_entry)
                varChickenSalad.set("0")

        def chkFishSandwich():
            if var6.get() == on_value_1:
                self.entry_fish.configure(state="normal")
                varFishSandwich.set("")
                self.entry_fish.focus()
            elif var6.get() == off_value_1:
                self.entry_fish.configure(state=state_entry)
                varFishSandwich.set("0")

        def chkCheeseSandwich():
            if var7.get() == on_value_1:
                self.entry_cheese.configure(state="normal")
                varCheeseSandwich.set("")
                self.entry_cheese.focus()
            elif var7.get() == off_value_1:
                self.entry_cheese.configure(state=state_entry)
                varCheeseSandwich.set("0")

        def chkChickenSandwich():
            if var8.get() == on_value_1:
                self.entry_chicken_1.configure(state="normal")
                varChickenSandwich.set("")
                self.entry_chicken_1.focus()
            elif var8.get() == off_value_1:
                self.entry_chicken_1.configure(state=state_entry)
                varChickenSandwich.set("0")

        self.title_1 = Label(self.Data_left_frame,
                             text="Fast Food Meal and Vegetable\n",
                             font=(font_1, h2, style_title))
        self.title_1.grid(row=0, column=0, columnspan=2, sticky=sticky_Entry)

        self.Fries = Checkbutton(self.Data_left_frame,
                                 variable=var1,
                                 onvalue=on_value_1,
                                 offvalue=off_value_1,
                                 command=chkFries,
                                 text="Fries\t" + space_items_cost + "$1.20" + space_entry,
                                 font=(font_1, h1, style_app))
        self.Fries.grid(row=1, column=0, sticky=sticky_label)

        self.Salad = Checkbutton(self.Data_left_frame,
                                 variable=var2,
                                 onvalue=on_value_1,
                                 offvalue=off_value_1,
                                 command=chkSalad,
                                 text="Salad\t" + space_items_cost + "$2.10" + space_entry,
                                 font=(font_1, h1, style_app))
        self.Salad.grid(row=2, column=0, sticky=sticky_label)

        self.Hamburger = Checkbutton(self.Data_left_frame,
                                     variable=var3,
                                     onvalue=on_value_1,
                                     offvalue=off_value_1,
                                     command=chkHamburger,
                                     text="Hamburger" + space_items_cost + "$3.10" + space_entry,
                                     font=(font_1, h1, style_app))
        self.Hamburger.grid(row=3, column=0, sticky=sticky_label)

        self.Onion_Rings = Checkbutton(self.Data_left_frame,
                                       variable=var4,
                                       onvalue=on_value_1,
                                       offvalue=off_value_1,
                                       command=chkOnionRings,
                                       text="Onion Rings" + space_items_cost + "$1.30" + space_entry,
                                       font=(font_1, h1, style_app))
        self.Onion_Rings.grid(row=4, column=0, sticky=sticky_label)

        self.Chicken_Salad = Checkbutton(self.Data_left_frame,
                                         variable=var5,
                                         onvalue=on_value_1,
                                         offvalue=off_value_1,
                                         command=chkChickenSalad,
                                         text="Chicken Salad" + space_items_cost + "$3.50" + space_entry,
                                         font=(font_1, h1, style_app))
        self.Chicken_Salad.grid(row=5, column=0, sticky=sticky_label)

        self.title_2 = Label(self.Data_left_frame,
                             text="\nSandwich\n",
                             font=(font_1, h2, style_title))
        self.title_2.grid(row=6, column=0, columnspan=3, sticky=sticky_Entry)

        self.Chicken_Sandwich = Checkbutton(self.Data_left_frame,
                                            variable=var6,
                                            onvalue=on_value_1,
                                            offvalue=off_value_1,
                                            command=chkFishSandwich,
                                            text="Chicken Sandwich" + space_items_cost + "$3.60" + space_entry,
                                            font=(font_1, h1, style_app))
        self.Chicken_Sandwich.grid(row=7, column=0, sticky=sticky_label)

        self.Cheese_Sandwich = Checkbutton(self.Data_left_frame,
                                           variable=var7,
                                           onvalue=on_value_1,
                                           offvalue=off_value_1,
                                           command=chkCheeseSandwich,
                                           text="Cheese Sandwich" + space_items_cost + "$3.40" + space_entry,
                                           font=(font_1, h1, style_app))
        self.Cheese_Sandwich.grid(row=8, column=0, sticky=sticky_label)

        self.Fish_Sandwich = Checkbutton(self.Data_left_frame,
                                         variable=var8,
                                         onvalue=on_value_1,
                                         offvalue=off_value_1,
                                         command=chkChickenSandwich,
                                         text="Fish Sandwich" + space_items_cost + "$3.60" + space_entry,
                                         font=(font_1, h1, style_app))
        self.Fish_Sandwich.grid(row=9, column=0, sticky=sticky_label)

        self.line2 = Label(self.Data_left_frame,
                           font=("Time", 12),
                           text=Line)
        self.line2.grid(row=10, column=0, columnspan=2)

        self.exit = ttk.Button(self.Data_left_frame,
                               command=self.Feedback,
                               text=space_button + "Feedback" + space_button)
        self.exit.grid(row=11, column=0, sticky=W, padx=pad_x_total)

        # self.cal = ttk.Button(self.Data_left_frame, text=space_button + "RESET" + space_button)
        #         # self.cal.grid(row=11, column=1, sticky=E, padx=pad_x_total)

        self.logo2 = PhotoImage(file="reset.PNG").subsample(3, 4)
        self.cal = ttk.Button(self.Data_left_frame,
                              command=Reset,
                              text="",
                              image=self.logo2)
        self.cal.grid(row=11, column=1, sticky=E, padx=pad_x_total)
        # self.calculator.configure(image=self.logo1, compound=BOTTOM)

        # LEFT FRAME DATA ENTRY
        # ----------------------------------------------------------------------------------------
        self.entry_fries = ttk.Entry(self.Data_left_frame,
                                     width=Width_entry,
                                     justify=justify_entry,
                                     state=state_entry,
                                     textvariable=varFries,
                                     font=(font_1, h1, style_app))
        self.entry_fries.grid(row=1, column=1, sticky=E)

        self.entry_salad = ttk.Entry(self.Data_left_frame,
                                     width=Width_entry,
                                     textvariable=varSalad,
                                     justify=justify_entry,
                                     state=state_entry,
                                     font=(font_1, h1, style_app))
        self.entry_salad.grid(row=2, column=1, sticky=E)

        self.entry_hamburger = ttk.Entry(self.Data_left_frame,
                                         width=Width_entry,
                                         textvariable=varHamburger,
                                         justify=justify_entry,
                                         state=state_entry,
                                         font=(font_1, h1, style_app))
        self.entry_hamburger.grid(row=3, column=1, sticky=E)

        self.entry_onion = ttk.Entry(self.Data_left_frame,
                                     width=Width_entry,
                                     textvariable=varOnionRings,
                                     justify=justify_entry,
                                     state=state_entry,
                                     font=(font_1, h1, style_app))
        self.entry_onion.grid(row=4, column=1, sticky=E)

        self.entry_chicken = ttk.Entry(self.Data_left_frame,
                                       width=Width_entry,
                                       textvariable=varChickenSalad,
                                       justify=justify_entry,
                                       state=state_entry,
                                       font=(font_1, h1, style_app))
        self.entry_chicken.grid(row=5, column=1, sticky=E)

        self.entry_fish = ttk.Entry(self.Data_left_frame,
                                    width=Width_entry,
                                    textvariable=varFishSandwich,
                                    justify=justify_entry,
                                    state=state_entry,
                                    font=(font_1, h1, style_app))
        self.entry_fish.grid(row=7, column=1, sticky=E)

        self.entry_cheese = ttk.Entry(self.Data_left_frame,
                                      width=Width_entry,
                                      textvariable=varCheeseSandwich,
                                      justify=justify_entry,
                                      state=state_entry,
                                      font=(font_1, h1, style_app))
        self.entry_cheese.grid(row=8, column=1, sticky=E)

        self.entry_chicken_1 = ttk.Entry(self.Data_left_frame,
                                         width=Width_entry,
                                         textvariable=varChickenSandwich,
                                         justify=justify_entry,
                                         state=state_entry,
                                         font=(font_1, h1, style_app))
        self.entry_chicken_1.grid(row=9, column=1, sticky=E)

        # ----------------------------------------------------------------------------------------
        # TODO LEFT FRAME DATA
        var14 = IntVar()
        var15 = IntVar()
        var16 = IntVar()
        var17 = IntVar()
        var18 = IntVar()
        var19 = IntVar()
        var20 = IntVar()
        var21 = IntVar()

        varTea = StringVar()
        varCola = StringVar()
        varCoffee = StringVar()
        varOrange = StringVar()
        varBottleWater = StringVar()
        varVanillaCone = StringVar()
        varVanillaShake = StringVar()
        varStrawberryShake = StringVar()

        varTea.set('0')
        varCola.set('0')
        varCoffee.set('0')
        varOrange.set('0')
        varBottleWater.set('0')
        varVanillaCone.set('0')
        varVanillaShake.set('0')
        varStrawberryShake.set('0')

        def D1():
            if var14.get() == on_value_1:
                self.E1.configure(state="normal")
                varTea.set("")
                self.E1.focus()
            elif var14.get() == off_value_1:
                self.E1.configure(state=state_entry)
                varTea.set("0")

        def D2():
            if var15.get() == on_value_1:
                self.E2.configure(state="normal")
                varCola.set("")
                self.E2.focus()
            elif var15.get() == off_value_1:
                self.E2.configure(state=state_entry)
                varCola.set("0")

        def D3():
            if var16.get() == on_value_1:
                self.E3.configure(state="normal")
                varCoffee.set("")
                self.E3.focus()
            elif var16.get() == off_value_1:
                self.E3.configure(state=state_entry)
                varCoffee.set("0")

        def D4():
            if var17.get() == on_value_1:
                self.E4.configure(state="normal")
                varOrange.set("")
                self.E4.focus()
            elif var17.get() == off_value_1:
                self.E4.configure(state=state_entry)
                varOrange.set("0")

        def D5():
            if var18.get() == on_value_1:
                self.E5.configure(state="normal")
                varBottleWater.set("")
                self.E5.focus()
            elif var18.get() == off_value_1:
                self.E5.configure(state=state_entry)
                varBottleWater.set("0")

        def D6():
            if var19.get() == on_value_1:
                self.E6.configure(state="normal")
                varVanillaCone.set("")
                self.E6.focus()
            elif var19.get() == off_value_1:
                self.E6.configure(state=state_entry)
                varVanillaCone.set("0")

        def D7():
            if var20.get() == on_value_1:
                self.E7.configure(state="normal")
                varVanillaShake.set("")
                self.E7.focus()
            elif var20.get() == off_value_1:
                self.E7.configure(state=state_entry)
                varVanillaShake.set("0")

        def D8():
            if var21.get() == on_value_1:
                self.E8.configure(state="normal")
                varStrawberryShake.set("")
                self.E8.focus()
            elif var21.get() == off_value_1:
                self.E8.configure(state=state_entry)
                varStrawberryShake.set("0")

        self.T1 = Label(self.Data_right_frame,
                        text="Drinks\n",
                        font=(font_1, h2, style_title))
        self.T1.grid(row=0, column=0, columnspan=2, sticky=sticky_Entry)

        self.T2 = Checkbutton(self.Data_right_frame,
                              variable=var14,
                              onvalue=on_value_1,
                              offvalue=off_value_1,
                              command=D1,
                              text="Tea\t" + space_items_cost + "$1.50" + space_entry,
                              font=(font_1, h1, style_app))
        self.T2.grid(row=1, column=0, sticky=sticky_label)

        self.T3 = Checkbutton(self.Data_right_frame,
                              variable=var15,
                              onvalue=on_value_1,
                              offvalue=off_value_1,
                              command=D2,
                              text="Cola\t" + space_items_cost + "$1.30" + space_entry,
                              font=(font_1, h1, style_app))
        self.T3.grid(row=2, column=0, sticky=sticky_label)

        self.T4 = Checkbutton(self.Data_right_frame,
                              variable=var16,
                              onvalue=on_value_1,
                              offvalue=off_value_1,
                              command=D3,
                              text="Coffee\t" + space_items_cost + "$1.59" + space_entry,
                              font=(font_1, h1, style_app))
        self.T4.grid(row=3, column=0, sticky=sticky_label)

        self.T5 = Checkbutton(self.Data_right_frame,
                              variable=var17,
                              onvalue=on_value_1,
                              offvalue=off_value_1,
                              command=D4,
                              text="Orange\t" + space_items_cost + "$1.20" + space_entry,
                              font=(font_1, h1, style_app))
        self.T5.grid(row=4, column=0, sticky=sticky_label)

        self.T6 = Checkbutton(self.Data_right_frame,
                              variable=var18,
                              onvalue=on_value_1,
                              offvalue=off_value_1,
                              command=D5,
                              text="Bottle Water" + space_items_cost + "$0.99" + space_entry,
                              font=(font_1, h1, style_app))
        self.T6.grid(row=5, column=0, sticky=sticky_label)

        self.T7 = Label(self.Data_right_frame,
                        text="\nShakes\n",
                        font=(font_1, h2, style_title))
        self.T7.grid(row=6, column=0, columnspan=3, sticky=sticky_Entry)

        self.T8 = Checkbutton(self.Data_right_frame,
                              variable=var19,
                              onvalue=on_value_1,
                              offvalue=off_value_1,
                              command=D6,
                              text="Vanilla Cone" + space_items_cost + "$2.10" + space_entry,
                              font=(font_1, h1, style_app))
        self.T8.grid(row=7, column=0, sticky=sticky_label)

        self.T9 = Checkbutton(self.Data_right_frame,
                              variable=var20,
                              onvalue=on_value_1,
                              offvalue=off_value_1,
                              command=D7,
                              text="Vanilla Shake" + space_items_cost + "$2.10" + space_entry,
                              font=(font_1, h1, style_app))
        self.T9.grid(row=8, column=0, sticky=sticky_label)

        self.T10 = Checkbutton(self.Data_right_frame,
                               variable=var21,
                               onvalue=on_value_1,
                               offvalue=off_value_1,
                               command=D8,
                               text="Strawberry Shake" + space_items_cost + "$2.20" + space_entry,
                               font=(font_1, h1, style_app))
        self.T10.grid(row=9, column=0, sticky=sticky_label)

        self.line2 = Label(self.Data_right_frame,
                           font=("Time", 12),
                           text=Line)
        self.line2.grid(row=10, column=0, columnspan=2)

        self.logo1 = PhotoImage(file="calculator.PNG").subsample(9, 11)
        self.calculator = ttk.Button(self.Data_right_frame,
                                     image=self.logo1,
                                     command=self.Cal,
                                     # text=space_button + "CALCULATOR" + space_button
                                     )
        self.calculator.grid(row=11, column=0, sticky=W, padx=pad_x_total)
        # self.calculator.configure(image=self.logo1, compound=BOTTOM)
        master.bind('<Control-c>', self.Cal)

        self.calC = ttk.Button(self.Data_right_frame,
                               text=space_button + "RECEIPT" + space_button)
        self.calC.grid(row=11, column=1, sticky=E, padx=pad_x_total)

        # ----------------------------------------------------------------------------------------
        # TODO LEFT FRAME DATA ENTRY
        self.E1 = ttk.Entry(self.Data_right_frame,
                            width=Width_entry,
                            justify=justify_entry,
                            state=state_entry,
                            textvariable=varTea,
                            font=(font_1, h1, style_app))
        self.E1.grid(row=1, column=1, sticky=E)

        self.E2 = ttk.Entry(self.Data_right_frame,
                            width=Width_entry,
                            textvariable=varCola,
                            justify=justify_entry,
                            state=state_entry,
                            font=(font_1, h1, style_app))
        self.E2.grid(row=2, column=1, sticky=E)

        self.E3 = ttk.Entry(self.Data_right_frame,
                            width=Width_entry,
                            textvariable=varCoffee,
                            justify=justify_entry,
                            state=state_entry,
                            font=(font_1, h1, style_app))
        self.E3.grid(row=3, column=1, sticky=E)

        self.E4 = ttk.Entry(self.Data_right_frame,
                            width=Width_entry,
                            textvariable=varOrange,
                            justify=justify_entry,
                            state=state_entry,
                            font=(font_1, h1, style_app))
        self.E4.grid(row=4, column=1, sticky=E)

        self.E5 = ttk.Entry(self.Data_right_frame,
                            width=Width_entry,
                            textvariable=varBottleWater,
                            justify=justify_entry,
                            state=state_entry,
                            font=(font_1, h1, style_app))
        self.E5.grid(row=5, column=1, sticky=E)

        self.E6 = ttk.Entry(self.Data_right_frame,
                            width=Width_entry,
                            textvariable=varVanillaCone,
                            justify=justify_entry,
                            state=state_entry,
                            font=(font_1, h1, style_app))
        self.E6.grid(row=7, column=1, sticky=E)

        self.E7 = ttk.Entry(self.Data_right_frame,
                            width=Width_entry,
                            textvariable=varVanillaShake,
                            justify=justify_entry,
                            state=state_entry,
                            font=(font_1, h1, style_app))
        self.E7.grid(row=8, column=1, sticky=E)

        self.E8 = ttk.Entry(self.Data_right_frame,
                            width=Width_entry,
                            textvariable=varStrawberryShake,
                            justify=justify_entry,
                            state=state_entry,
                            font=(font_1, h1, style_app))
        self.E8.grid(row=9, column=1, sticky=E)

        # ----------------------------------------------------------------------------------------
        # TODO MIDDLE FRAME DATA

        var9 = IntVar()
        var10 = IntVar()
        var11 = IntVar()
        var12 = IntVar()
        var13 = IntVar()

        varHashBrown = StringVar()
        varToastedBagel = StringVar()
        varPancakesSyrup = StringVar()
        varPineappleStick = StringVar()
        varChocolateMuffin = StringVar()

        varHashBrown.set('0')
        varToastedBagel.set('0')
        varPancakesSyrup.set('0')
        varPineappleStick.set('0')
        varChocolateMuffin.set('0')

        def A1():
            if var9.get() == on_value_1:
                self.b1.configure(state="normal")
                varHashBrown.set("")
                self.b1.focus()
            elif var9.get() == off_value_1:
                self.b1.configure(state=state_entry)
                varHashBrown.set("0")

        def A2():
            if var10.get() == on_value_1:
                self.b2.configure(state="normal")
                varToastedBagel.set("")
                self.b2.focus()
            elif var10.get() == off_value_1:
                self.b2.configure(state=state_entry)
                varToastedBagel.set("0")

        def A3():
            if var11.get() == on_value_1:
                self.b3.configure(state="normal")
                varPancakesSyrup.set("")
                self.b3.focus()
            elif var11.get() == off_value_1:
                self.b3.configure(state=state_entry)
                varPancakesSyrup.set("0")

        def A4():
            if var12.get() == on_value_1:
                self.b4.configure(state="normal")
                varPineappleStick.set("")
                self.b4.focus()
            elif var12.get() == off_value_1:
                self.b4.configure(state=state_entry)
                varPineappleStick.set("0")

        def A5():
            if var13.get() == on_value_1:
                self.b5.configure(state="normal")
                varChocolateMuffin.set("")
                self.b5.focus()
            elif var13.get() == off_value_1:
                self.b5.configure(state=state_entry)
                varChocolateMuffin.set("0")

        self.b1 = Label(self.Data_middle_frame,
                        text="Dessert",
                        font=(font_1, h2, style_title))
        self.b1.grid(row=0, column=0, columnspan=2, sticky=sticky_Entry)

        self.B2 = Checkbutton(self.Data_middle_frame,
                              variable=var9,
                              onvalue=on_value_1,
                              offvalue=off_value_1,
                              command=A1,
                              text="Hash Brown" + space_items_cost + "$1.40" + space_entry,
                              font=(font_1, h1, style_app))
        self.B2.grid(row=1, column=0, sticky=sticky_label)

        self.B3 = Checkbutton(self.Data_middle_frame,
                              variable=var10,
                              onvalue=on_value_1,
                              offvalue=off_value_1,
                              command=A2,
                              text="Toasted Bagel" + space_items_cost + "$1.60" + space_entry,
                              font=(font_1, h1, style_app))
        self.B3.grid(row=2, column=0, sticky=sticky_label)

        self.B4 = Checkbutton(self.Data_middle_frame,
                              variable=var11,
                              onvalue=on_value_1,
                              offvalue=off_value_1,
                              command=A3,
                              text="Pineapple Stick" + space_items_cost + "$1.20" + space_entry,
                              font=(font_1, h1, style_app))
        self.B4.grid(row=3, column=0, sticky=sticky_label)

        self.B5 = Checkbutton(self.Data_middle_frame,
                              variable=var12,
                              onvalue=on_value_1,
                              offvalue=off_value_1,
                              command=A4,
                              text="Chocolate Muffin" + space_items_cost + "$1.40" + space_entry,
                              font=(font_1, h1, style_app))
        self.B5.grid(row=4, column=0, sticky=sticky_label)

        self.B6 = Checkbutton(self.Data_middle_frame,
                              variable=var13,
                              onvalue=on_value_1,
                              offvalue=off_value_1,
                              command=A5,
                              text="Pancake Syrup" + space_items_cost + "$2.40" + space_entry,
                              font=(font_1, h1, style_app))
        self.B6.grid(row=5, column=0, sticky=sticky_label)

        # ----------------------------------------------------------------------------------------
        # TODO MIDDLE FRAME DATA ENTRY
        self.b1 = ttk.Entry(self.Data_middle_frame,
                            width=Width_entry,
                            justify=justify_entry,
                            state=state_entry,
                            textvariable=varHashBrown,
                            font=(font_1, h1, style_app))
        self.b1.grid(row=1, column=1, sticky=E)

        self.b2 = ttk.Entry(self.Data_middle_frame,
                            width=Width_entry,
                            textvariable=varToastedBagel,
                            justify=justify_entry,
                            state=state_entry,
                            font=(font_1, h1, style_app))
        self.b2.grid(row=2, column=1, sticky=E)

        self.b3 = ttk.Entry(self.Data_middle_frame,
                            width=Width_entry,
                            textvariable=varPancakesSyrup,
                            justify=justify_entry,
                            state=state_entry,
                            font=(font_1, h1, style_app))
        self.b3.grid(row=3, column=1, sticky=E)

        self.b4 = ttk.Entry(self.Data_middle_frame,
                            width=Width_entry,
                            textvariable=varPineappleStick,
                            justify=justify_entry,
                            state=state_entry,
                            font=(font_1, h1, style_app))
        self.b4.grid(row=4, column=1, sticky=E)

        self.b5 = ttk.Entry(self.Data_middle_frame,
                            width=Width_entry,
                            textvariable=varChocolateMuffin,
                            justify=justify_entry,
                            state=state_entry,
                            font=(font_1, h1, style_app))
        self.b5.grid(row=5, column=1, sticky=E)

        # ----------------------------------------------------------------------------------------
        # TODO MIDDLE PAYMENT
        varChange = StringVar()
        varTax = StringVar()
        varSubTotal = StringVar()
        varTotal = StringVar()

        var22 = IntVar()
        var23 = IntVar()
        var24 = IntVar()
        var25 = IntVar()
        var28 = IntVar
        var27 = IntVar()

        varChange.set('')
        varTax.set('0')
        varSubTotal.set('0')
        varTotal.set('0')

        self.line = Label(self.Data_middle_frame,
                          font=("Time", 12),
                          text='_________________________________________________')
        self.line.grid(row=6, column=0, columnspan=2)

        self.l1 = Label(self.Data_middle_frame,
                        text="Payment Method",
                        pady=pad_y,
                        font=(font_1, h1, style_app))
        self.l1.grid(row=7, column=0, sticky=sticky_label_cost, padx=pad_x_all)

        self.l2 = Label(self.Data_middle_frame,
                        pady=pad_y,
                        text="Cash",
                        font=(font_1, h1, style_app))
        self.l2.grid(row=8, column=0, sticky=sticky_label_cost, padx=pad_x_all)

        self.l3 = Label(self.Data_middle_frame,
                        pady=pad_y,
                        text="Tax",
                        font=(font_1, h1, style_app))
        self.l3.grid(row=9, column=0, sticky=sticky_label_cost, padx=pad_x_all)

        self.l4 = Label(self.Data_middle_frame,
                        pady=pad_y,
                        text="Sub Total",
                        font=(font_1, h1, style_app))
        self.l4.grid(row=10, column=0,
                     sticky=sticky_label_cost, padx=pad_x_all)

        self.l5 = Label(self.Data_middle_frame,
                        pady=pad_y,
                        text="Total",
                        font=(font_1, h1, style_app))
        self.l5.grid(row=11, column=0,
                     sticky=sticky_label_cost, padx=pad_x_all)

        self.l6 = Label(self.Data_middle_frame,
                        pady=pad_y,
                        text="Change",
                        font=(font_1, h1, style_app))
        self.l6.grid(row=12, column=0,
                     sticky=sticky_label_cost, padx=pad_x_all)

        self.payment_Method = ttk.Combobox(self.Data_middle_frame,
                                           width=10,
                                           justify=justify_entry,
                                           font=(font_1, h1, style_app))
        self.payment_Method.grid(row=7, column=1, sticky=E)

        self.payment_Method['value'] = (
            '', 'Cash', 'Master Card', 'Visa Card', 'Debit Card', 'Credit Card')
        # self.payment_Method.current(0)

        self.e2 = ttk.Entry(self.Data_middle_frame,
                            textvariable=var27,
                            width=10,
                            justify=justify_entry,
                            state=state_entry,
                            font=(font_1, h1, style_app))
        self.e2.grid(row=8, column=1, sticky=E)

        self.e3 = ttk.Entry(self.Data_middle_frame,
                            width=10,
                            textvariable=var22,
                            justify=justify_entry,
                            state=state_entry,
                            font=(font_1, h1, style_app))
        self.e3.grid(row=9, column=1, sticky=E)

        self.e4 = ttk.Entry(self.Data_middle_frame,
                            width=10,
                            textvariable=var23,
                            justify=justify_entry,
                            state=state_entry,
                            font=(font_1, h1, style_app))
        self.e4.grid(row=10, column=1, sticky=E)

        self.e5 = ttk.Entry(self.Data_middle_frame,
                            width=10,
                            textvariable=var24,
                            justify=justify_entry,
                            state=state_entry,
                            font=(font_1, h1, style_app))
        self.e5.grid(row=11, column=1, sticky=E)

        self.e6 = ttk.Entry(self.Data_middle_frame,
                            width=10,
                            textvariable=var25,
                            justify=justify_entry,
                            state=state_entry,
                            font=(font_1, h1, style_app))
        self.e6.grid(row=12, column=1, sticky=E)

        self.line2 = Label(self.Data_middle_frame,
                           font=("Time", 12),
                           text='_________________________________________________')
        self.line2.grid(row=13, column=0, columnspan=2)

        self.Total = ttk.Button(self.Data_middle_frame,
                                command=cost_of_meal,
                                text=space_button + "TOTAL" + space_button)
        self.Total.grid(row=14, column=0, sticky=W, padx=pad_x_total)
        master.bind('<Return>', cost_of_meal)

        self.Change = ttk.Button(self.Data_middle_frame,
                                 command=Change_1,
                                 text=space_button + "CHANGE" + space_button, width="12")
        self.Change.grid(row=14, column=1, padx=pad_x_total, sticky=E)

        # ----------------------------------------------------------------------------------------
        # TODO CALCULATOR

    def Cal(self, event=""):
        self.master_3 = Toplevel(self.master)
        self.master_3.title("Calculator")
        self.master_3.resizable(0, 0)

        self.display = Entry(self.master_3,
                             font=(font_1, 35),
                             relief=SUNKEN,
                             justify=RIGHT,
                             bg='#ddffee', bd=8, width=9)
        # self.display.insert(0,"0")
        # self.display.focus()
        self.display.grid(row=1, column=0, columnspan=4)
        self.master_3.iconbitmap('m1.ico')

        # local variables for Calc
        font_2 = "Helvertica"
        h = 18
        style = "italic"

        fg_1 = "white"
        fg_2 = "black"
        fg_on = "red"
        fg_off = "blue"
        fg_exit = "light blue"
        color = "grey"
        borderwidth_1 = 3
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

        # ROW 1
        self.but1 = Button(self.master_3,
                           bg=color,
                           text="on",
                           fg=fg_on,
                           font=(font_2, h, style),
                           relief=relief_1,
                           command=lambda: self.On_button(),
                           borderwidth=borderwidth_1)
        self.but1.grid(row=5, column=0, sticky="NWNESWSE")

        self.but2 = Button(self.master_3,
                           bg=color,
                           text="off",
                           fg=fg_off,
                           font=(font_2, h, style),
                           relief=relief_1,
                           command=lambda: self.Off_button(),
                           borderwidth=borderwidth_1)
        self.but2.grid(row=5, column=1, sticky="NWNESWSE")

        self.but3 = Button(self.master_3,
                           bg=color,
                           text="E",
                           fg=fg_exit,
                           font=(font_2, h, style),
                           relief=relief_1,
                           command=self.iExit_2,
                           borderwidth=borderwidth_1)
        self.but3.grid(row=5, column=2, sticky="NWNESWSE")

        self.but4 = Button(self.master_3,
                           bg=color,
                           text="C",
                           fg=fg_1,
                           font=(font_2, h, style),
                           relief=relief_1,
                           command=lambda: self.clearText(),
                           borderwidth=borderwidth_1)
        self.but4.grid(row=5, column=3, sticky="NWNESWSE")

        # ROW 2
        self.but5 = Button(self.master_3,
                           bg=color,
                           text="%",
                           fg=fg_1,
                           font=(font_2, h, style),
                           relief=relief_1,
                           command=lambda: self.append_To_display("%"),
                           borderwidth=borderwidth_1)
        self.but5.grid(row=7, column=0, sticky="NWNESWSE")

        self.but6 = Button(self.master_3,
                           bg=color,
                           text="(",
                           fg=fg_2,
                           font=(font_2, h, style),
                           relief=relief_1,
                           command=lambda: self.append_To_display("("),
                           borderwidth=borderwidth_1)
        self.but6.grid(row=7, column=1, sticky="NWNESWSE")

        self.but7 = Button(self.master_3,
                           bg=color,
                           text=")",
                           fg=fg_2,
                           font=(font_2, h, style),
                           relief=relief_1,
                           command=lambda: self.append_To_display(")"),
                           borderwidth=borderwidth_1)
        self.but7.grid(row=7, column=2, sticky="NWNESWSE")

        self.but8 = Button(self.master_3,
                           bg=color,
                           text="+",
                           fg=fg_2,
                           font=(font_2, h, style),
                           relief=relief_1,
                           command=lambda: self.append_To_display("+"),
                           borderwidth=borderwidth_1)
        self.but8.grid(row=7, column=3, sticky="NWNESWSE")

        # ROW 3
        self.but9 = Button(self.master_3,
                           bg=color,
                           text="7",
                           fg=fg_2,
                           font=(font_2, h, style),
                           relief=relief_1,
                           command=lambda: self.append_To_display("7"),
                           borderwidth=borderwidth_1)
        self.but9.grid(row=8, column=0, sticky="NWNESWSE")

        self.but10 = Button(self.master_3,
                            bg=color,
                            text="8",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.append_To_display("8"),
                            borderwidth=borderwidth_1)
        self.but10.grid(row=8, column=1, sticky="NWNESWSE")

        self.but11 = Button(self.master_3,
                            bg=color,
                            text="9",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.append_To_display("9"),
                            borderwidth=borderwidth_1)
        self.but11.grid(row=8, column=2, sticky="NWNESWSE")

        self.but12 = Button(self.master_3,
                            bg=color,
                            text="÷",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.append_To_display("/"),
                            borderwidth=borderwidth_1)
        self.but12.grid(row=8, column=3, sticky="NWNESWSE")

        # ROW 4
        self.but13 = Button(self.master_3,
                            bg=color,
                            text="4",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.append_To_display("4"),
                            borderwidth=borderwidth_1)
        self.but13.grid(row=9, column=0, sticky="NWNESWSE")

        self.but14 = Button(self.master_3,
                            bg=color,
                            text="5",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.append_To_display("5"),
                            borderwidth=borderwidth_1)
        self.but14.grid(row=9, column=1, sticky="NWNESWSE")

        self.but15 = Button(self.master_3,
                            bg=color,
                            text="6",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.append_To_display("6"),
                            borderwidth=borderwidth_1)
        self.but15.grid(row=9, column=2, sticky="NWNESWSE")

        self.but16 = Button(self.master_3,
                            bg=color,
                            text="x",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.append_To_display("*"),
                            borderwidth=borderwidth_1)
        self.but16.grid(row=9, column=3, sticky="NWNESWSE")

        # ROW 7
        self.but17 = Button(self.master_3,
                            bg=color,
                            text="1",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.append_To_display("1"),
                            borderwidth=borderwidth_1)
        self.but17.grid(row=10, column=0, sticky="NWNESWSE")

        self.but18 = Button(self.master_3,
                            bg=color,
                            text="2",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.append_To_display("2"),
                            borderwidth=borderwidth_1)
        self.but18.grid(row=10, column=1, sticky="NWNESWSE")

        self.but19 = Button(self.master_3,
                            bg=color,
                            text="3",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.append_To_display("3"),
                            borderwidth=borderwidth_1)
        self.but19.grid(row=10, column=2, sticky="NWNESWSE")

        self.but20 = Button(self.master_3,
                            bg=color,
                            text="-",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.append_To_display("-"),
                            borderwidth=borderwidth_1)
        self.but20.grid(row=10, column=3, sticky="NWNESWSE")

        # ROW 8
        self.but21 = Button(self.master_3,
                            bg=color,
                            text="0",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.append_To_display("0"),
                            borderwidth=borderwidth_1)
        self.but21.grid(row=11, column=0, sticky="NWNESWSE")

        self.but22 = Button(self.master_3,
                            bg=color,
                            text="←",
                            fg=fg_1,
                            font=(font_2, h, style),
                            command=lambda: self.Delete_Entry(),
                            relief=relief_1,
                            borderwidth=borderwidth_1)
        self.but22.grid(row=11, column=1, sticky="NWNESWSE")

        self.but23 = Button(self.master_3,
                            bg=color, text=".",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.append_To_display("."),
                            borderwidth=borderwidth_1)
        self.but23.grid(row=11, column=2, sticky="NWNESWSE")

        self.but24 = Button(self.master_3,
                            bg=color,
                            text="=",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.CalculateExpression(),
                            borderwidth=borderwidth_1)
        self.but24.grid(row=11, column=3, sticky="NWNESWSE")

        self.label = Label(self.master_3, text="", bg='#b5b5b5')
        self.label.grid(row=0, column=0, sticky="NWNESWSE", columnspan=4)

    def Off_button(self):
        self.display.delete(0, END)
        self.display.insert(0, "")
        # self.but1.config(state = DISABLED)
        # self.but2.config(state = DISABLED)
        self.but3.config(state=DISABLED)
        self.but4.config(state=DISABLED)
        self.but5.config(state=DISABLED)
        self.but6.config(state=DISABLED)
        self.but7.config(state=DISABLED)
        self.but8.config(state=DISABLED)
        self.but9.config(state=DISABLED)
        self.but10.config(state=DISABLED)
        self.but11.config(state=DISABLED)
        self.but12.config(state=DISABLED)
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

    def On_button(self):
        self.display.insert(0, "0")
        # self.but1.config(state = NORMAL)
        # self.but2.config(state = NORMAL)
        self.but3.config(state=NORMAL)
        self.but4.config(state=NORMAL)
        self.but5.config(state=NORMAL)
        self.but6.config(state=NORMAL)
        self.but7.config(state=NORMAL)
        self.but8.config(state=NORMAL)
        self.but9.config(state=NORMAL)
        self.but10.config(state=NORMAL)
        self.but11.config(state=NORMAL)
        self.but12.config(state=NORMAL)
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

    def Delete_Entry(self):
        # self.display.delete(0,END)
        # self.display.configure(justify=LEFT)
        self.display.delete(0, 1)

    def replaceText(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)

    def append_To_display(self, text):
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
        self.expression = self.expression.replace("%",
                                                  "/100")  # we have to replace all the %/100 so that typton will not considere it as modulo.
        self.result = eval(self.expression)
        # self.replaceText(self.result)# this will put the result on the screen

        try:
            self.result = eval(self.expression)
            self.replaceText(self.result)

        except:
            messagebox.showinfo("Error", "Invalid Input")

    def iExit_2(self):
        self.qExit = messagebox.askyesno("Calculator",
                                         "Are you sure that you want to close?",
                                         icon="warning")
        if self.qExit > 0:
            self.master_3.destroy()
            return

        # ----------------------------------------------------------------------------------------
        # TODO FEEDBACK

    def Feedback(self):
        master_1 = Toplevel(self.master)
        master_1.title("Feedback")
        master_1.resizable(0, 0)
        master_1.configure(background='#e1d8b9')

        f1 = Frame(master_1, background='#e1d8b9')
        f1.pack(side=TOP)
        f2 = Frame(master_1, background='#e1d8b9')
        f2.pack(side=TOP)
        f3 = Frame(master_1, background='#e1d8b9')
        f3.pack(side=TOP)

        def clear():
            entry_name.delete(0, END)
            entry_email.delete(0, END)
            text.delete(1.0, END)

        def submit():
            print('Name: {}'.format(entry_name.get()))
            print('Email: {}'.format(entry_email.get()))
            print('Comments: {}'.format(text.get(1.0, 'end')))
            clear()
            messagebox.showinfo(title='Feedback',
                                message='Feedback Submitted!')

        from tkinter import messagebox

        def iExit():
            qExit = messagebox.askyesno("Feedback",
                                        "You program is still running!\n"
                                        "Do you want to quit?", icon="warning")
            if qExit > 0:
                master_1.destroy()
                return

        l1 = ttk.Label(f1, text='Employee Comments or Concerned',
                       background='#e1d8b9',
                       font=('time', 18, 'bold'), )
        l1.grid(row=0, column=1)

        label_name = ttk.Label(f2,
                               background='#e1d8b9',
                               text='Name:')
        label_name.grid(row=0, column=0, padx=5, sticky='sw')

        label_email = ttk.Label(f2,
                                background='#e1d8b9',
                                font=(),
                                text='Email:')
        label_email.grid(row=0, column=1, padx=5, sticky='sw')

        label_content = ttk.Label(f2,
                                  background='#e1d8b9',
                                  text='Comments:')
        label_content.grid(row=2, column=0, padx=5, sticky='sw')

        entry_name = ttk.Entry(f2, width=30, font=('Arial', 10))
        entry_name.grid(row=1, column=0, padx=5, sticky='sw')

        entry_email = ttk.Entry(f2, width=30, font=('Arial', 10))
        entry_email.grid(row=1, column=1, padx=5, sticky='sw')

        text = Text(f2, width=48,
                    height=10,
                    font=('Arial', 12))
        text.grid(row=3, column=0, padx=5, columnspan=2)

        yscroll = ttk.Scrollbar(f2, orient=VERTICAL, command=text.yview)
        text.config(yscrollcommand=yscroll.set)
        yscroll.grid(row=3, column=2, sticky='ns')

        ttk.Button(f3, text='Submit',
                   command=submit).grid(row=4, column=0, padx=5, pady=5, sticky='w')

        ttk.Button(f3, text='Clear',
                   command=clear).grid(row=4, column=1, padx=5, pady=5, sticky='ns')

        ttk.Button(f3, text='Exit',
                   command=lambda: iExit()).grid(row=4, column=2, padx=5, pady=5, sticky='e')


# ==============================================================================================
def main():
    root = Tk()
    app = login(root)
    root.mainloop()


if __name__ == '__main__':
    main()

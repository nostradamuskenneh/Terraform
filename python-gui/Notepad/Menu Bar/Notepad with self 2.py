import os
from datetime import time, datetime
from tkinter import *
from tkinter import ttk, colorchooser
from tkinter import messagebox
from tkinter import filedialog
import webbrowser
from tkinter.font import families
from turtledemo import clock
import time

background_image = '#c1e7fd'
current_open_file = ''


def about_notepad():
    webbrowser.open('https://www.youtube.com/watch?v=RXge_eMkSvU')


def view_help():
    webbrowser.open(
        'https://www.bing.com/search?q=get+help+with+notepad+in+windows+10&filters=guid:%224466414-en-dia%22%20lang:%22en%22&form=T00032&ocid=HelpPane-BingIA')


class text_editor:
    def New_file(self, event=None):
        if self.current_open_file is None:
            self.text.delete(1.0, END)

        if self.current_open_file is not None:
            T = messagebox.askyesnocancel('Exit', 'Do you want to save change to\n', icon="warning")
            if T is True:
                self.save_file()
                self.text.delete(1.0, END)
                self.text.focus()

            elif T is False:
                self.text.delete(1.0, END)
                self.text.focus()

    def open_files(self, event=None):
        open_result = filedialog.askopenfile(initialdir='/', title='Select file',
                                             filetype=(('text file', '.txt'), ('All files', '*.*')))

        # if open_result != None:
        try:
            if open_result is not None:
                self.text.delete(1.0, END)
                for line in open_result:
                    self.text.insert(END, line)
                self.current_open_file = open_result.name
                open_result.close()

        except:
            answer = messagebox.showerror('open file',
                                          'This is not txt file.\nPlease check your file extension and try again')

    def save_as_file(self):
        if self.current_open_file is None:
            f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
            if f is None:
                return
            text_save_as = self.text.get(1.0, END)
            self.current_open_file = f.name
            f.write(text_save_as)
            f.close()

        else:
            f = open(self.current_open_file, 'w+')
            f.write(self.text.get(1.0, END))
            f.close()

    def save_file(self, event=None):
        if self.current_open_file is None:
            f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
            if f is None:
                return
            text_save_as = self.text.get(1.0, END)
            self.current_open_file = f.name
            f.write(text_save_as)
            f.close()

        else:
            f = open(self.current_open_file, 'w+')
            f.write(self.text.get(1.0, END))
            f.close()

    def Exit(self, event=None):
        if self.current_open_file is None:
            T = messagebox.askyesnocancel('Exit', 'Do you want to save change to\n', icon="warning")
            if T is True:
                self.save_file()
                self.master.destroy()

            elif T is False:
                self.master.destroy()

        elif self.current_open_file is not None:

            T = messagebox.askyesnocancel('Exit', 'Do you want to save change to\n', icon="warning")
            if T is True:
                self.save_file()
                self.master.destroy()

            elif T is False:
                self.master.destroy()

    def background_color(self):
        global clr
        clr = colorchooser.askcolor(title='Select Background Color')
        self.text.configure(bg=clr[1])

    def text_color(self):
        global clr
        clr = colorchooser.askcolor(title='Select Text Color')
        self.text.configure(fg=clr[1])

    def copy_text(self, event=None):
        self.text.event_generate("<<Copy>>")

    def cut_text(self, event=None):
        self.text.event_generate("<<Cut>>")

    def paste_text(self, event=None):
        self.text.event_generate("<<Paste>>")

    def redo(self, event=None):
        try:
            self.text.edit_redo()
        except:
            pass

    def undo(self, event=None):
        try:
            self.text.edit_undo()
        except:
            pass

    def select_all(self, event=None):
        self.text.tag_add('sel', '1.0', 'end')
        return 'break'

    def delete_text(self, event=None):
        self.text.delete(1.0, END)
        self.text.focus()

    def bind_event(self, event):
        try:
            self.right_click_menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.right_click_menu.grab_release()

    def __init__(self, master):

        width_of_window = 1370
        height_of_window = 700

        width_value = master.winfo_screenwidth()
        height_value = master.winfo_screenheight()

        X_coordinate = (width_value / 2) - (width_of_window / 2)
        Y_coordinate = (height_value / 2) - (height_of_window / 2)

        master.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window,
                                         X_coordinate, Y_coordinate))

        self.current_open_file = None

        self.open_file = None
        self.master = master
        self.master.title("Notepad")
        self.master.wm_iconbitmap("note.ico") # the image must be ico image

        self.shortcut_bar = Frame(self.master, height=35, background=background_image)
        self.shortcut_bar.pack(expand='no', fill='x', side=TOP)

        global status_bar
        status_bar = Label(self.master, height=1, font=('Time', 12),
                           text='Welcome to Notepad', bg=background_image,
                           anchor=W,
                           relief=GROOVE)
        status_bar.pack(side=BOTTOM, fill=X)

        # ----------------------------------------------------------------------------
        self.print = PhotoImage(file="print.png")
        self.print_button = Button(self.shortcut_bar, font=('Time', 8),
                                   text='Print',
                                   image=self.print, bg=background_image,
                                   relief=FLAT,
                                   )
        self.print_button.pack(side=LEFT, padx=1)
        self.print_button.config(image=self.print, compound=TOP)

        self.new = PhotoImage(file="new.png")
        self.new_button = Button(self.shortcut_bar, font=('Time', 8),
                                 text='New File',
                                 image=self.new, bg=background_image,
                                 relief=FLAT,
                                 command=self.New_file)
        self.new_button.pack(side=LEFT, padx=1)
        self.new_button.config(image=self.new, compound=TOP)

        self.open = PhotoImage(file="open.png")
        self.open_button = Button(self.shortcut_bar, font=('Time', 8),
                                  text='Open File',
                                  image=self.open, bg=background_image,
                                  relief=FLAT,
                                  command=self.open_files)
        self.open_button.pack(side=LEFT, padx=1)
        self.open_button.config(image=self.open, compound=TOP)

        self.save_as = PhotoImage(file="save as.png")
        self.save_as_button = Button(self.shortcut_bar, font=('Time', 8),
                                     text='Save as',
                                     image=self.save_as, bg=background_image,
                                     relief=FLAT,
                                     command=self.save_as_file)
        self.save_as_button.pack(side=LEFT, padx=1)
        self.save_as_button.config(image=self.save_as, compound=TOP)

        self.save = PhotoImage(file="save.png")
        self.save_button = Button(self.shortcut_bar, font=('Time', 8),
                                  text='Save File',
                                  image=self.save, bg=background_image,
                                  relief=FLAT,
                                  command=self.save_file)
        self.save_button.pack(side=LEFT, padx=1)
        self.save_button.config(image=self.save, compound=TOP)

        self.redo_1 = PhotoImage(file="redo.png")
        self.redo_button = Button(self.shortcut_bar, font=('Time', 8),
                                  text='Redo',
                                  image=self.redo_1, bg=background_image,
                                  relief=FLAT,
                                  command=self.redo)
        self.redo_button.pack(side=LEFT, padx=1)
        self.redo_button.config(image=self.redo_1, compound=TOP)

        self.undo_1 = PhotoImage(file="undo.png")
        self.undo_button = Button(self.shortcut_bar, font=('Time', 8),
                                  text='Undo',
                                  image=self.undo_1, bg=background_image,
                                  relief=FLAT,
                                  command=self.undo)
        self.undo_button.pack(side=LEFT, padx=1)
        self.undo_button.config(image=self.undo_1, compound=TOP)

        self.cut_1 = PhotoImage(file="cut.png")
        self.cut_button = Button(self.shortcut_bar, font=('Time', 8),
                                 text='Cut',
                                 image=self.cut_1, bg=background_image,
                                 relief=FLAT,
                                 command=self.cut_text)
        self.cut_button.pack(side=LEFT, padx=1)
        self.cut_button.config(image=self.cut_1, compound=TOP)

        self.copy_1 = PhotoImage(file="copy.png")
        self.copy_button = Button(self.shortcut_bar, font=('Time', 8),
                                  text='Copy',
                                  image=self.copy_1, bg=background_image,
                                  relief=FLAT,
                                  command=self.copy_text)
        self.copy_button.pack(side=LEFT, padx=1)
        self.copy_button.config(image=self.copy_1, compound=TOP)

        self.paste_1 = PhotoImage(file="paste.png")
        self.paste_button = Button(self.shortcut_bar, font=('Time', 8),
                                   text='Paste',
                                   image=self.paste_1, bg=background_image,
                                   relief=FLAT,
                                   command=self.paste_text)
        self.paste_button.pack(side=LEFT, padx=1)
        self.paste_button.config(image=self.paste_1, compound=TOP)

        self.select = PhotoImage(file="select all.png")
        self.select_button = Button(self.shortcut_bar, font=('Time', 8),
                                    text='Select all',
                                    image=self.select, bg=background_image,
                                    relief=FLAT,
                                    command=self.select_all)
        self.select_button.pack(side=LEFT, padx=1)
        self.select_button.config(image=self.select, compound=TOP)

        self.delete = PhotoImage(file="delete.png")
        self.delete_button = Button(self.shortcut_bar, font=('Time', 8),
                                    text='Delete',
                                    image=self.delete, bg=background_image,
                                    relief=FLAT,
                                    command=self.delete_text)
        self.delete_button.pack(side=LEFT, padx=1)
        self.delete_button.config(image=self.delete, compound=TOP)

        self.color1 = PhotoImage(file="color1.png")
        self.color1_button = Button(self.shortcut_bar, font=('Time', 8),
                                    text='Background color',
                                    image=self.color1, bg=background_image,
                                    relief=FLAT,
                                    command=self.background_color)
        self.color1_button.pack(side=LEFT, padx=1)
        self.color1_button.config(image=self.color1, compound=TOP)

        self.color2 = PhotoImage(file="color2.png")
        self.color2_button = Button(self.shortcut_bar, font=('Time', 8),
                                    text='Text color',
                                    image=self.color2, bg=background_image,
                                    relief=FLAT,
                                    command=self.text_color)
        self.color2_button.pack(side=LEFT, padx=1)
        self.color2_button.config(image=self.color2, compound=TOP)

        self.cal = PhotoImage(file="cal.png")
        self.cal_button = Button(self.shortcut_bar, font=('Time', 8),
                                 command=self.Exit,
                                 text='Calculator',
                                 image=self.cal, bg=background_image,
                                 relief=FLAT,
                                 )
        self.cal_button.pack(side=LEFT, padx=1)
        self.cal_button.config(image=self.cal, compound=TOP)

        self.help = PhotoImage(file="help.png")
        self.help_button = Button(self.shortcut_bar, font=('Time', 8),
                                  command=view_help,
                                  text='Help',
                                  image=self.help, bg=background_image,
                                  relief=FLAT,
                                  )
        self.help_button.pack(side=LEFT, padx=1)
        self.help_button.config(image=self.help, compound=TOP)

        L = LabelFrame(self.shortcut_bar, text='Font', bg=background_image, font=('Time', 10))
        L.pack(side=LEFT, padx=10)

        V = self.available_fonts = sorted(families())
        self.Combo = ttk.Combobox(L, height=20, width=39, value=V, font=('Time', 9))
        self.Combo.grid(row=0, column=0, sticky=W + E, padx=1)

        for family in self.available_fonts:
            self.Combo.insert(END, family)
        self.Combo.set('Times New Roman')

        But = ttk.Button(L, text='Save changes')
        But.grid(row=1, column=1, sticky=W + E, padx=1)

        V2 = list(range(5, 100))
        Combo2 = ttk.Combobox(L, value=V2, height=15, width=30)
        Combo2.grid(row=0, column=1, sticky=W + E, padx=1)
        Combo2.set('12')

        V3 = StringVar()
        Combo3 = ttk.Combobox(L, value=V3, height=3, width=40)
        Combo3.grid(row=1, column=0, sticky=W + E, padx=1)
        Combo3.config(values=('regular', 'bold', 'italic', 'bold italic'))
        Combo3.set('regular')

        self.close = PhotoImage(file="close.png")
        self.close_button = Button(self.shortcut_bar, font=('Time', 8),
                                   command=self.Exit,
                                   text='Close',
                                   image=self.close, bg=background_image,
                                   relief=FLAT,
                                   )
        self.close_button.pack(side=RIGHT)
        self.close_button.config(image=self.close, compound=TOP)

        Date_1 = StringVar()
        Time_1 = StringVar()

        Date_1.set(time.strftime("%d/%m/%y"))
        Time_1.set(time.strftime("%H:%M:%S"))

        def tick():
            time_string = time.strftime("%H:%M:%S")
            clock.config(text=time_string)
            clock.after(200, tick)

        label_date = Label(self.shortcut_bar, textvariable=Date_1,
                           font=("arial", 20, "bold"),
                           bd=5,
                           fg="blue",
                           bg=background_image,
                           padx=2)
        label_date.pack(side=RIGHT)

        clock = Label(self.shortcut_bar, font=("arial", 20, "bold"),
                      bg=background_image,
                      bd=5,
                      fg="black",
                      padx=5)
        clock.pack(side=RIGHT)
        tick()  # we just call the tick function so that it can display the time.

        self.scroll = Scrollbar(master)
        self.scroll.pack(side=RIGHT, fill=Y)

        self.text = Text(self.master, wrap=WORD, undo=True, font=("Time", 14),
                         yscrollcommand=self.scroll.set)
        self.text.pack(fill=BOTH, expand=YES, padx=5)
        self.text.focus()
        self.scroll.configure(command=self.text.yview)

        # TODO MENU
        master.option_add('*tearOff', False)
        self.menubar = Menu(master)
        master.config(menu=self.menubar)

        self.file_ = Menu(self.menubar)
        self.edit_ = Menu(self.menubar)
        self.format_ = Menu(self.menubar)
        self.view_ = Menu(self.menubar)
        self.help_ = Menu(self.menubar)
        # this to add the menu to the menu bar.
        self.menubar.add_cascade(menu=self.file_, label='File')
        self.menubar.add_cascade(menu=self.edit_, label='Edit')
        self.menubar.add_cascade(menu=self.format_, label='Format')
        self.menubar.add_cascade(menu=self.view_, label='View')
        self.menubar.add_cascade(menu=self.help_, label='Help')

        # the separator is to separator the first submenu with others.
        self.file_.add_command(label='New...', command=self.New_file)
        self.file_.add_separator()
        self.file_.add_command(label='Open...', command=self.open_files)
        self.file_.add_command(label='Save...', command=self.save_file)

        self.save_as1 = PhotoImage(file="save as.png")
        self.file_.add_command(label='Save As...', image=self.save_as1, compound='left', command=self.save_as_file)

        self.file_.add_separator()
        self.file_.add_command(label='Page Setup...')
        self.file_.add_command(label='Print...', command=self.bind_event)
        self.file_.add_separator()
        self.file_.add_command(label='Exit...', command=self.Exit)

        # this is to create a pop up menu at a specific location.
        # self.file_.post(400, 300)

        # this to add keyboard shot cut.

        self.new2 = PhotoImage(file="new.png")
        self.file_.entryconfig('New...', image=self.new2, compound='left', accelerator='Ctrl+N')

        self.open2 = PhotoImage(file="open.png")
        self.file_.entryconfig('Open...', image=self.open2, compound='left', accelerator='Ctrl+O')

        self.save2 = PhotoImage(file="save.png")
        self.file_.entryconfig('Save...', image=self.save2, compound='left', accelerator='Ctrl+S')

        self.print2 = PhotoImage(file="print.png")
        self.file_.entryconfig('Print...', image=self.print2, compound='left', accelerator='Ctrl+P')

        self.close4 = PhotoImage(file="close.png")
        self.file_.entryconfig('Exit...', image=self.close4, compound='left', accelerator='Ctrl+E')

        # the separator is to separator the first submenu with others.
        self.edit_.add_command(label='Undo', command=self.undo)
        self.edit_.add_command(label='Redo', command=self.redo)
        self.edit_.add_separator()
        self.edit_.add_command(label='Cut', command=self.cut_text)
        self.edit_.add_command(label='Copy', command=self.copy_text)
        self.edit_.add_command(label='Paste', command=self.paste_text)
        self.edit_.add_command(label='Delete', command=self.delete_text)
        self.edit_.add_separator()
        self.edit_.add_command(label='Find...', command=self.find_replace)
        self.edit_.add_command(label='Replace...')
        self.edit_.add_separator()
        self.edit_.add_command(label='Select All', command=self.select_all)
        # edit_.add_command(label='Time/Date')

        # this to add keyboard shot cut.
        self.undo2 = PhotoImage(file="undo.png")
        self.edit_.entryconfig('Undo', image=self.undo2, compound='left', accelerator='Ctrl+Z')

        self.redo2 = PhotoImage(file="redo.png")
        self.edit_.entryconfig('Redo', image=self.redo2, compound='left', accelerator='Ctrl+Y')

        self.cut2 = PhotoImage(file="cut.png")
        self.edit_.entryconfig('Cut', image=self.cut2, compound='left', accelerator='Ctrl+X')

        self.copy2 = PhotoImage(file="copy.png")
        self.edit_.entryconfig('Copy', image=self.copy2, compound='left', accelerator='Ctrl+C')

        self.paste2 = PhotoImage(file="paste.png")
        self.edit_.entryconfig('Paste', image=self.paste2, compound='left', accelerator='Ctrl+V')

        self.delete3 = PhotoImage(file="delete.png")
        self.edit_.entryconfig('Delete', image=self.delete3, compound='left', accelerator='Del')

        self.edit_.entryconfig('Find...', accelerator='Ctrl+F')
        self.edit_.entryconfig('Replace...', accelerator='Ctrl+H')

        self.select2 = PhotoImage(file="select all.png")
        self.edit_.entryconfig('Select All', image=self.select2, compound='left', accelerator='Ctrl+A',
                               command=self.select_all)

        self.format_.add_command(label='Word Wrap')
        self.format_.add_separator()
        self.format_.add_command(label='Font...', command=self.font_change)

        self.Colors = Menu(self.format_)
        self.format_.add_cascade(menu=self.Colors, label='Colors')

        self.color4 = PhotoImage(file="color2.png")
        self.Colors.add_command(label='Text Color', image=self.color4, compound='left', command=self.text_color)

        self.color5 = PhotoImage(file="color1.png")
        self.Colors.add_command(label='Background Color', image=self.color5, compound='left', command=self.text_color)

        self.view_.add_command(label='Status Bar')

        # TODO KEYBOARD EVENTS
        self.help_.add_command(label='View Help', command=view_help)
        self.help_.add_separator()
        self.help_.add_command(label='About Notepad', command=about_notepad)

        self.master.bind('<Control-n>', self.New_file)
        self.master.bind('<Control-N>', self.New_file)

        self.master.bind('<Control-s>', self.save_file)
        self.master.bind('<Control-S>', self.save_file)

        self.master.bind('<Control-o>', self.open_files)
        self.master.bind('<Control-O>', self.open_files)

        self.master.bind('<Control-s>', self.save_file)
        self.master.bind('<Control-S>', self.save_file)

        # self.master.bind('<Control-c>', self.copy_text)
        # self.master.bind('<Control-C>', self.copy_text)
        #
        # self.master.bind('<Control-v>', self.paste_text)
        # self.master.bind('<Control-V>', self.paste_text)

        self.master.bind('<Control-x>', self.cut_text)
        self.master.bind('<Control-X>', self.cut_text)

        self.master.bind('<Control-r>', self.find_replace)
        self.master.bind('<Control-R>', self.find_replace)

        self.master.bind('<Control-e>', self.Exit)
        self.master.bind('<Control-E>', self.Exit)

        self.master.bind("<Button-3>", self.bind_event)

        # TODO CONTEXT MENU
        self.right_click_menu = Menu(master, tearoff=0, fg='black', bg='white')
        self.right_click_menu.add_command(label='New...', command=self.New_file)
        self.right_click_menu.add_separator()
        self.right_click_menu.add_command(label='Open...', command=self.open_files)
        self.right_click_menu.add_command(label='Save...', command=self.save_file)

        self.save_as4 = PhotoImage(file="save as.png")
        self.right_click_menu.add_command(label='Save As...', image=self.save_as4, compound='left',
                                          command=self.save_as_file)

        self.right_click_menu.add_separator()
        self.right_click_menu.add_command(label='Print...', command=self.bind_event)
        self.right_click_menu.add_separator()

        self.new3 = PhotoImage(file="new.png")
        self.right_click_menu.entryconfig('New...', image=self.new3, compound='left', accelerator='Ctrl+N')

        self.open3 = PhotoImage(file="open.png")
        self.right_click_menu.entryconfig('Open...', image=self.open3, compound='left', accelerator='Ctrl+O')

        self.save3 = PhotoImage(file="save.png")
        self.right_click_menu.entryconfig('Save...', image=self.save3, compound='left', accelerator='Ctrl+S')

        self.print3 = PhotoImage(file="print.png")
        self.right_click_menu.entryconfig('Print...', image=self.print3, compound='left', accelerator='Ctrl+P')

        self.right_click_menu.add_command(label='Undo', command=self.undo)
        self.right_click_menu.add_command(label='Redo', command=self.redo)
        self.right_click_menu.add_separator()
        self.right_click_menu.add_command(label='Cut', command=self.cut_text)
        self.right_click_menu.add_command(label='Copy', command=self.copy_text)
        self.right_click_menu.add_command(label='Paste', command=self.paste_text)
        self.right_click_menu.add_command(label='Delete', command=self.delete_text)
        self.right_click_menu.add_separator()
        self.right_click_menu.add_command(label='Find...', command=self.find_replace)
        self.right_click_menu.add_command(label='Replace...')
        self.right_click_menu.add_separator()
        self.right_click_menu.add_command(label='Select All', command=self.select_all)

        self.undo3 = PhotoImage(file="undo.png")
        self.right_click_menu.entryconfig('Undo', image=self.undo3, compound='left', accelerator='Ctrl+Z')

        self.redo3 = PhotoImage(file="redo.png")
        self.right_click_menu.entryconfig('Redo', image=self.redo3, compound='left', accelerator='Ctrl+Y')

        self.cut3 = PhotoImage(file="cut.png")
        self.right_click_menu.entryconfig('Cut', image=self.cut3, compound='left', accelerator='Ctrl+X')

        self.copy3 = PhotoImage(file="copy.png")
        self.right_click_menu.entryconfig('Copy', image=self.copy3, compound='left', accelerator='Ctrl+C')

        self.paste3 = PhotoImage(file="paste.png")
        self.right_click_menu.entryconfig('Paste', image=self.paste3, compound='left', accelerator='Ctrl+V')

        self.delete5 = PhotoImage(file="delete.png")
        self.right_click_menu.entryconfig('Delete', image=self.delete5, compound='left', accelerator='Del')

        self.right_click_menu.entryconfig('Replace...', accelerator='Ctrl+H')
        self.right_click_menu.entryconfig('Select All', accelerator='Ctrl+A')

        self.right_click_menu.add_command(label='Font...', command=self.font_change)
        self.right_click_menu.entryconfig('Font...', accelerator='Ctrl+F')

        self.color3 = PhotoImage(file="color1.png")
        self.right_click_menu.add_cascade(menu=self.Colors, label='Colors', image=self.color3, compound='left')

        self.right_click_menu.add_separator()
        self.close1 = PhotoImage(file="close.png")
        self.right_click_menu.add_command(label='Exit...', command=self.Exit)
        self.right_click_menu.entryconfig('Exit...', image=self.close1, compound='left', accelerator='Ctrl+G')

        self.right_click_menu.post(300, 200)

    def find_replace(self, event=None):
        window1 = Toplevel(self.master)
        app = Find(window1)

    def font_change(self, event=None):
        window2 = Toplevel(self.master)
        app = fonts(window2)


class Shortcut_Bar:
    def __init__(self, master, **kwargs):
        pass


class fonts:
    def __init__(self, master, **kwargs):
        width_of_window = 790
        height_of_window = 350

        width_value = master.winfo_screenwidth()
        height_value = master.winfo_screenheight()

        X_coordinate = (width_value / 2) - (width_of_window / 2)
        Y_coordinate = (height_value / 2) - (height_of_window / 2)

        master.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window,
                                         X_coordinate, Y_coordinate))

        self.master = master
        master.title('Choose Font and Size')
        master.resizable(FALSE, FALSE)

        # ------------------------------------------------------------------------------
        self.frame_void1 = LabelFrame(self.master, width=20)
        self.frame_void1.pack(side=LEFT)

        self.frame = LabelFrame(self.master, text='Choose Text Font', font=('Time', 16))
        self.frame.pack(side=LEFT)
        self.scrollbar = Scrollbar(self.frame)

        self.font_list = Listbox(self.frame, font=('Time', 12),
                                 width=25,
                                 height=15,
                                 exportselection=FALSE,
                                 yscrollcommand=self.scrollbar.set)

        self.available_fonts = sorted(families())
        for family in self.available_fonts:
            self.font_list.insert(END, family)

        self.E = ttk.Entry(self.frame, width=40)
        self.E.pack()
        self.E.focus()

        self.font_list.pack(side=LEFT)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.font_list.yview)

        # -----------------------------------------------------------------------

        self.frame_void2 = LabelFrame(self.master, width=35)
        self.frame_void2.pack(side=LEFT)

        self.frame4 = LabelFrame(self.master,
                                 text='font Style:',
                                 font=('Time', 16))
        self.frame4.pack(side=LEFT)

        self.E3 = ttk.Entry(self.frame4, width=27)
        self.E3.pack()

        self.listbox2 = Listbox(self.frame4, bg='white',
                                fg='black',
                                width=15,
                                height=12,
                                font=('Time', 14),
                                selectmode=SINGLE)  # BROWSE, SINGLE, MULTIPLE, EXTENDED

        self.listbox2.insert(1, 'regular')
        self.listbox2.insert(2, 'bold')
        self.listbox2.insert(2, 'italic')
        self.listbox2.insert(3, 'bold italic')
        self.listbox2.pack(side=LEFT)

        # --------------------------------------------------------------------------

        self.frame_void3 = LabelFrame(self.master, width=35)
        self.frame_void3.pack(side=LEFT)

        self.frame3 = LabelFrame(self.master,
                                 text='Size',
                                 font=('Time', 16))
        self.frame3.pack(side=LEFT)

        self.E2 = ttk.Entry(self.frame3, width=18)
        self.E2.pack()

        self.scroll = Scrollbar(self.frame3)
        self.scroll.pack(side=RIGHT, fill=Y)

        # height=25 is to set 25 items in the listbox
        self.listbox2 = Listbox(self.frame3, height=15, width=10, font=('Time', 12),
                                yscrollcommand=self.scroll.set)  # yscroll command it is to make the scroll bar communique with the listbox
        for i in range(5, 99):
            self.listbox2.insert(END, str(i))

        self.listbox2.pack(side=LEFT)
        self.scroll.configure(command=self.listbox2.yview)  # this yview is in the master windows

        self.frame5 = Frame(self.master)
        self.frame5.pack(side=BOTTOM)
        self.b = ttk.Button(self.frame5, text='Save')
        self.b.grid(row=0, column=0, pady=5)

        self.b = ttk.Button(self.frame5, text='Cancel')
        self.b.grid(row=0, column=1, pady=5)


class Find:
    def __init__(self, master):
        width_of_window = 310
        height_of_window = 115

        width_value = master.winfo_screenwidth()
        height_value = master.winfo_screenheight()

        X_coordinate = (width_value / 2) - (width_of_window / 2)
        Y_coordinate = (height_value / 2) - (height_of_window / 2)

        master.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window,
                                         X_coordinate, Y_coordinate))
        self.master = master
        # self.master.geometry('350x100')
        self.master.title('Find and Replace')

        self.text_to_find = StringVar()
        self.text_to_replace = StringVar()

        label1 = Label(self.master, text='Find')
        label1.grid(row=0, column=0, padx=5, pady=10)

        label2 = Label(self.master, text='Replace')
        label2.grid(row=1, column=0)

        entry1 = ttk.Entry(self.master, textvariable=self.text_to_find, width=40)
        entry1.grid(row=0, column=1, padx=5, pady=10)
        entry1.focus()

        entry2 = ttk.Entry(self.master, textvariable=self.text_to_replace, width=40)
        entry2.grid(row=1, column=1, padx=5, pady=10)

        button1 = ttk.Button(self.master, text='Find', command=self.on_find)
        button1.grid(row=2, column=1, sticky=E)

        button1 = ttk.Button(self.master, text='Replace', command=self.on_find)
        button1.grid(row=2, column=1, sticky=W)

    def on_find(self):
        self.master.find(self.text_to_find.get())

    def on_replace(self):
        self.master.replace(self.text_to_find.get(), self.text_to_replace.get())


def main():
    root = Tk()
    app = text_editor(root)
    root.mainloop()


if __name__ == '__main__':
    main()

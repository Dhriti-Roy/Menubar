import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('Menubar')

def func():
    print('func called')

def aboutus():
    print('Developer- Dhriti Roy')
    print('Program Type- "Menubar"')

#MENU

main_menu = tk.Menu(win)

file_menu= tk.Menu(main_menu,tearoff=0)
file_menu.add_command(label='New File', command=func)
file_menu.add_command(label='New Window', command=func)
file_menu.add_separator()
file_menu.add_command(label='Open File', command=func)
file_menu.add_command(label='Open Folder', command=func)
file_menu.add_separator()
file_menu.add_command(label='Save File', command=func)
file_menu.add_command(label='Save As', command=func)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=func)

main_menu.add_cascade(label='File', menu=file_menu)

edit_menu= tk.Menu(main_menu, tearoff=0)
edit_menu.add_command(label='Undo', command=func)
edit_menu.add_command(label='Redo', command=func)
edit_menu.add_separator()
edit_menu.add_command(label='Cut', command=func)
edit_menu.add_command(label='Copy', command=func)
edit_menu.add_command(label='Paste', command=func)
main_menu.add_cascade(label='Edit', menu=edit_menu)

about_menu= tk.Menu(main_menu, tearoff=0)
about_menu.add_command(label='About', command=aboutus)
main_menu.add_cascade(label='About', menu=about_menu)

win.config(menu=main_menu)

win.mainloop()
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


#                                         MAIN MENU FUNCTIONALITY

url = ''

#                                        ^^  1. FILE FUNCTIONALITY :

#                                        >> new file functionality :

def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0, tk.END)

new_btn.configure(command=new_file)    

# open file functionality :
def open_file(even=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', '*.txt'),('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))        
 


#                                       >> open folder functionality:

open_btn.configure(command=open_file)    

def open_folder(even=None):
    global url
    url =filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Folder', filetypes=(('Text Folder', '*.txt'),('All floders', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))        


#                                          >> save functionality :

def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url,'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt' , filetypes=(('Text File', '*.txt'),('All files', '*.*')))
            content = text_editor.get(1.0, tk.END)
            url.write(content)
            url.close()
    except:
        return        


#                                          >> save as functionality :

def save_as_file(event=None):
    global url
    try:
        if url:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt' , filetypes=(('Text File', '*.txt'),('All files', '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt' , filetypes=(('Text File', '*.txt'),('All files', '*.*')))
            content = text_editor.get(1.0, tk.END)
            url.write(content)
            url.close()    
    except:
        return        


#                                           >>  exit functionality :

def exit_file(event=None):
    global url, text_change
    try:
        if text_change:
            msgbox = messagebox.askyesnocancel('Warning','Do you want to save current file ?')
            if msgbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url,'w', encoding='utf-8')as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt' , filetypes=(('Text File', '*.txt'),('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif msgbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return                     
exit_icon = tk.PhotoImage(file='images/logout.png')




win.config(menu=main_menu)

win.mainloop()

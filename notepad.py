import tkinter
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import font,colorchooser,filedialog
from PIL import ImageTk,ImageGrab
import os
import keyboard

window=tkinter.Tk()
window.title("My Notepad")
notepad_icon=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\notepad2.png")
window.iconphoto(True,notepad_icon)
window.geometry("900x600+0+0")

# importing images

# 1- file menubar
new_file_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\new_file.png")
open_file_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\open_file.png")
save_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\save.png")
saveAs_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\save_as.png")
print_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\print.png")
exit_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\exit.png")

# 2- edit menubar
cut_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\cut.png")
copy_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\copy.png")
paste_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\paste.png")
delete_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\delete.png")
find_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\find.png")
clearall_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\clear.png")

# 3- view mwnubar
status_bar_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\status_bar.png")
tool_bar_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\tool_bar.png")

# 4- color_theme menubar
baby_blue_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\colors\baby_blue.png")
baby_green_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\colors\baby_green.png")
baby_pink_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\colors\baby_pink.png")
blue_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\colors\blue.png")
grey_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\colors\grey.png")
light_grey_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\colors\light_grey.png")
peach_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\colors\peach.png")
white_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\colors\white.png")
yellow_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\colors\yellow.png")

# 5- font style image
bold_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\bold.png")
italic_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\italic.png")
underline_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\underline.png")
font_color_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\font_color.png")
right_just_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\rightjust.png")
left_just_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\leftjust.png")
centre_just_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\mayank\file_handling\icons\centrejust.png")


# menubar
menubar_space=tkinter.Menu(window)

# file menubar

# 1- new file function
def newfile_function(event=None):
    text_editor.delete(1.0,tkinter.END)

# 2- open file function
open_file_name=""
def openfile_function(event=None):
    global open_file_name
    open_file_name=filedialog.askopenfilename(initialdir=os.getcwd(),title="select file",filetypes=(("Text File","*.txt"),("All Files","*.*")))
    try:
        with open(open_file_name) as new_file:
            text_editor.delete(1.0,tkinter.END)
            text_editor.insert(tkinter.INSERT,new_file.read())
    
    except FileNotFoundError:
        return 

    except:
        return
    window.title(os.path.basename(open_file_name))
    
# 3- save function
def savefile_function(event=None):
    global open_file_name
    try:
        if (open_file_name):
            data1=str(text_editor.get(1.0,tkinter.END))
            with open(open_file_name,"w") as new_file:
                new_file.write(data1)
    
        else:
            open_file_name=filedialog.asksaveasfile(mode="w",defaultextension="txt",filetypes=(("Text File","*.txt"),("All Files","*.*")))
            data2=str(text_editor.get(1.0,tkinter.END))
            open_file_name.write(data2)
            open_file_name.close()
    except:
        return

# 4- saveas function
def saveasfile_function(event=None):
    try:
        open_file_name=filedialog.asksaveasfile(mode="w",defaultextension="txt",filetypes=(("Text File","*.txt"),("All Files","*.*")))
        data3=str(text_editor.get(1.0,tkinter.END))
        open_file_name.write(data3)
        open_file_name.close()

    except:
        return 


# 5- screenshot function
def screenshotfile_function(event=None):
    screenshot=ImageGrab.grab()
    screenshot.save("screenshot.png")


# 6- exit function
def exit_function(event=None):
    global open_file_name,text_editing
    try:
        if (text_editing):
            msgbox=mb.askyesnocancel("Warning",f"Do you want to save to {os.getcwd()}")
            if (msgbox==True):
                if (open_file_name):
                    data4=text_editor.get(1.0,tkinter.END)
                    with open(open_file_name,"w") as new_file:
                        new_file.write(data4)
                    window.destroy()
            
                else:
                    open_file_name=filedialog.asksaveasfile(mode="w",defaultextension="txt",filetypes=(("Text File","*.txt"),("All Files","*.*")))
                    data4=text_editor.get(1.0,tkinter.END)
                    open_file_name.write(data4)
                    open_file_name.close()
                    window.destroy()

            elif (msgbox==False):
                window.destroy()

        else:
            window.destroy()

    except:
        return


file_menubar=tkinter.Menu(menubar_space,tearoff=0)
file_menubar.add_command(label="New",accelerator="Ctrl+N",image=new_file_image,compound=tkinter.LEFT,command=newfile_function)
file_menubar.add_command(label="Open",accelerator="Ctrl+O",image=open_file_image,compound=tkinter.LEFT,command=openfile_function)
file_menubar.add_command(label="Save",accelerator="Ctrl+S",image=save_image,compound=tkinter.LEFT,command=savefile_function)
file_menubar.add_command(label="SaveAs...",accelerator="Ctrl+Alt+S",image=saveAs_image,compound=tkinter.LEFT,command=saveasfile_function)
file_menubar.add_separator()
file_menubar.add_command(label="Page Setup")
file_menubar.add_command(label="Screenshot",accelerator="Ctrl+P",image=print_image,compound=tkinter.LEFT,command=screenshotfile_function)
file_menubar.add_separator()
file_menubar.add_command(label="Exit",image=exit_image,compound=tkinter.LEFT,command=exit_function)
menubar_space.add_cascade(label="File",menu=file_menubar)

# edit menubar

# find/replace function

def find_replace_function(event=None):
    find_popup=tkinter.Toplevel()
    find_popup.geometry("500x300+0+0")
    find_popup.title("find")
    find_popup.resizable(0,0)

    # label frame
    find_label_frame=tkinter.LabelFrame(find_popup,text="Find/Replace",foreground="blue")
    find_label_frame.place(x=105,y=60)

    ttk.Label(find_label_frame,text="Find").grid(row=0,column=0,padx=5,pady=5)
    ttk.Label(find_label_frame,text="Replace").grid(row=1,column=0,padx=5,pady=5)

    find_input=tkinter.StringVar()
    find_entry=ttk.Entry(find_label_frame,width=30,textvariable=find_input)
    find_entry.grid(row=0,column=1,padx=5,pady=5)

    replace_input=tkinter.StringVar()
    replace_entry=ttk.Entry(find_label_frame,width=30,textvariable=replace_input)
    replace_entry.grid(row=1,column=1,padx=5,pady=5)

    for i in find_label_frame.winfo_children():
        i.grid_configure(padx=10,pady=10)

    # find fnction
    def find_function():
        find_input_get=find_entry.get()
        text_editor.tag_remove("find","1.0",tkinter.END)
        
        if (find_input_get):
            start_position="1.0"
            count=0
            while True:
                character_index=text_editor.search(find_input_get,start_position,stopindex=tkinter.END)
                if not (character_index):
                    break
                last_position=f"{character_index}+{len(find_input_get)}c"
                text_editor.tag_add("find",character_index,last_position)
                count+=1  
                text_editor.tag_config("find",background="#BBBBAF")
                start_position=last_position 
    
    # replace function
    def replace_function():
        input_character=find_input.get()
        replace_input_get=replace_input.get()
        text_input=text_editor.get(1.0,tkinter.END)
        new_data=text_input.replace(input_character,replace_input_get)
        text_editor.delete(1.0,tkinter.END)
        text_editor.insert(tkinter.INSERT,new_data)
        

    # buttons
    # 1- find button 
    find_button=ttk.Button(find_label_frame,text="Find",command=find_function)
    find_button.grid(row=2,column=0,padx=10,pady=10)

    # 2- replace button
    replace_button=ttk.Button(find_label_frame,text="Replace",command=replace_function)
    replace_button.grid(row=2,column=1,padx=10,pady=10)



edit_menubar=tkinter.Menu(menubar_space,tearoff=0)
edit_menubar.add_command(label="Cut",image=cut_image,compound=tkinter.LEFT,accelerator="Ctrl+X",command=lambda:text_editor.event_generate("<<Cut>>"))
edit_menubar.add_command(label="Copy",image=copy_image,compound=tkinter.LEFT,accelerator="Ctrl+C",command=lambda:text_editor.event_generate("<<Copy>>"))
edit_menubar.add_command(label="Paste",image=paste_image,compound=tkinter.LEFT,accelerator="Ctrl+V",command=lambda:text_editor.event_generate("<<Paste>>"))
edit_menubar.add_separator()
edit_menubar.add_command(label="Find",accelerator="Ctrl+F",image=find_image,compound=tkinter.LEFT,command=find_replace_function)
edit_menubar.add_command(label="ClearAll",image=clearall_image,compound=tkinter.LEFT,accelerator="Ctrl+Alt+X",command=lambda:text_editor.delete(1.0,tkinter.END))
menubar_space.add_cascade(label="Edit",menu=edit_menubar)

# view menubar

# 1- tool bar function
toolbar_input=tkinter.BooleanVar()
toolbar_input.set(True)
statusbar_input=tkinter.BooleanVar()
statusbar_input.set(True)

def toolbar_function():
    global toolbar_input
    if (toolbar_input):
        toolbar_space.pack_forget()
        toolbar_input=False

    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        toolbar_space.pack(side=tkinter.TOP,fill=tkinter.X)
        text_editor.pack(expand=True,fill="both")
        status_bar.pack(side=tkinter.BOTTOM)
        toolbar_input=True

def statusbar_function():
    global statusbar_input
    if (statusbar_input):
        status_bar.pack_forget()
        statusbar_input=False

    else:
        status_bar.pack(side=tkinter.BOTTOM)
        statusbar_input=True
        
view_menubar=tkinter.Menu(menubar_space,tearoff=0)
view_menubar.add_checkbutton(label="Status Bar",onvalue=True,offvalue=False,image=status_bar_image,compound=tkinter.LEFT,variable=statusbar_input,command=statusbar_function)

view_menubar.add_checkbutton(label="Tool Bar",onvalue=True,offvalue=False,image=tool_bar_image,compound=tkinter.LEFT,variable=toolbar_input,command=toolbar_function)
menubar_space.add_cascade(label="View",menu=view_menubar)


# colour_theme menubar
colour_theme_menubar=tkinter.Menu(menubar_space,tearoff=0)
colour_theme_tuple=(baby_blue_image,baby_green_image,baby_pink_image,blue_image,grey_image,light_grey_image,peach_image,white_image,yellow_image)
colour_combination_dict={
    "Baby Blue":("#CCFFFF","#39087c"),
    "Baby Green":("#00FF00","#63110e"),
    "Baby Pink":("#F5F1DE","#437c17"),
    "Blue":("#1FBED6","#725283"),
    "Grey":("#C0BCB6","#437c17"),
    "Light Grey":("#F5F5F5","#ec9670"),
    "Peach":("#FFFFCC","#32212a"),
    "White":("#FFFFFF","#000000"),
    "Yellow":("#FFCC00","#990000")
}

# colour theme function
colour_theme_input=tkinter.StringVar()
def colour_theme_function():
    colour_theme_input_get=colour_theme_input.get()
    colour_theme_selected=colour_combination_dict.get(colour_theme_input_get)
    foreground_colour,background_colour=colour_theme_selected[1],colour_theme_selected[0]
    text_editor.config(foreground=foreground_colour,background=background_colour)



c=0
for i in colour_combination_dict:
    colour_theme_menubar.add_radiobutton(label=i,image=colour_theme_tuple[c],compound=tkinter.LEFT,variable=colour_theme_input,command=colour_theme_function)
    c+=1


menubar_space.add_cascade(label="Colour Theme",menu=colour_theme_menubar)

# toolbar menubar space

toolbar_space=ttk.Label(window)
toolbar_space.pack(side=tkinter.TOP,fill=tkinter.X)

# font toolbar

fonts=font.families()
fonttheme=tkinter.StringVar()
fonttheme_entry=ttk.Combobox(toolbar_space,width=25,textvariable=fonttheme,stat="readonly")
fonttheme_entry.grid(row=0,column=0,padx=5,pady=5)
fonttheme_entry["values"]=fonts
fonttheme_entry.current(fonts.index("Algerian"))

# font size toolbar

font_size=tkinter.IntVar()
fontsize_entry=ttk.Combobox(toolbar_space,width=20,textvariable=font_size,stat="readonly")
fontsize_entry.grid(row=0,column=1,padx=5,pady=5)
fontsize_entry["values"]=tuple(range(8,82,2))
fontsize_entry.current(0)

# buttons

# 1- bold button
bold_button=ttk.Button(toolbar_space,image=bold_image)
bold_button.grid(row=0,column=2,padx=5,pady=5)

# 2- italic button
italic_button=ttk.Button(toolbar_space,image=italic_image)
italic_button.grid(row=0,column=3,padx=5,pady=5)

# 3- underline button
underline_button=ttk.Button(toolbar_space,image=underline_image)
underline_button.grid(row=0,column=4,padx=5,pady=5)

# 4- font_color button
font_color_button=ttk.Button(toolbar_space,image=font_color_image)
font_color_button.grid(row=0,column=5,padx=5,pady=5)

# 5- left_just button
left_just_button=ttk.Button(toolbar_space,image=left_just_image)
left_just_button.grid(row=0,column=6,padx=5,pady=5)

# 6- centre_just button
centre_just_button=ttk.Button(toolbar_space,image=centre_just_image)
centre_just_button.grid(row=0,column=7,padx=5,pady=5)

# 7- right_just button
right_just_button=ttk.Button(toolbar_space,image=right_just_image)
right_just_button.grid(row=0,column=8,padx=5,pady=5)

# text editor
text_editor=tkinter.Text(window)
text_editor.config(wrap="word")

# scroll bar
scrollbar1=ttk.Scrollbar(window)
scrollbar1.pack(side=tkinter.RIGHT,fill=tkinter.Y)

text_editor.focus_set()
text_editor.pack(expand=True,fill="both")

scrollbar1.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scrollbar1.set)


# status bar

status_bar=ttk.Label(window,text="Status Bar")
status_bar.pack(side=tkinter.BOTTOM)

# functions

# 1- word count
text_editing=False
def letter_change(event=None):
    global text_editing
    if (text_editor.edit_modified()):
        text_editing=True
        word_count=len(text_editor.get(1.0,tkinter.END).split())
        characters_count=len(text_editor.get(1.0,tkinter.END).replace(" ",""))
        status_bar.config(text=f"Words : {word_count}    Characters : {characters_count}")
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>",letter_change)


# 2- font theme
current_font_theme="Algerian"
current_font_size=8
def font_theme(event=None):
    global fontthemes
    fontthemes=fonttheme.get()
    text_editor.config(font=(fontthemes,current_font_size))
fonttheme_entry.bind("<<ComboboxSelected>>",font_theme)


# 3- font size
def fontsize(event=None):
    global font_size_get
    font_size_get=font_size.get()
    text_editor.config(font=(fontthemes,font_size_get))
fontsize_entry.bind("<<ComboboxSelected>>",fontsize)


# 4- bold font
def boldfont_function():
    font_get1=font.Font(font=text_editor["font"])
    # if ((font_get.actual())["weight"]=="normal"):
    #     text_editor.config(font=(fontthemes,font_size_get,"bold"))

    # or

    if ((font_get1.cget("weight"))=="normal"):
        text_editor.config(font=(fontthemes,font_size_get,"bold"))


    # if ((font_get.actual())["weight"]=="bold"):
    #     text_editor.config(font=(fontthemes,font_size_get,"normal"))
    
    # or

    elif ((font_get1.cget("weight"))=="bold"):
        text_editor.config(font=(fontthemes,font_size_get,"normal"))

bold_button.config(command=boldfont_function)


# 5- italic font
def italicfont_function():
    font_get2=font.Font(font=text_editor["font"])
    if (font_get2.cget("slant")=="roman"):
        text_editor.config(font=(fontthemes,font_size_get,"italic"))

    elif (font_get2.cget("slant")=="italic"):
        text_editor.config(font=(fontthemes,font_size_get,"roman"))
italic_button.config(command=italicfont_function)


# 6- underlining font
def underlinefont_function():
    font_get3=font.Font(font=text_editor["font"])
    if ((font_get3.cget("underline"))==False):
        text_editor.config(font=(fontthemes,font_size_get,"underline"))

    elif ((font_get3.cget("underline"))==True):
        text_editor.config(font=(fontthemes,font_size_get,"normal"))

underline_button.config(command=underlinefont_function)

# 7- coloring font
def colorfont_function():
    font_colors=colorchooser.askcolor()
    text_editor.config(foreground=font_colors[1])
font_color_button.config(command=colorfont_function)


# 8- left just font
def leftjustfont_function():
    text_get=text_editor.get(1.0,"end")
    text_editor.tag_config("left",justify=tkinter.LEFT)
    text_editor.delete(1.0,tkinter.END)
    text_editor.insert(tkinter.INSERT,text_get,"left")
left_just_button.config(command=leftjustfont_function)



# 9- centre just font
def centrejustfont_function():
    text_get=text_editor.get(1.0,"end")
    text_editor.tag_config("centre",justify=tkinter.CENTER)
    text_editor.delete(1.0,tkinter.END)
    text_editor.insert(tkinter.INSERT,text_get,"centre")
centre_just_button.config(command=centrejustfont_function)


# 10- right just font
def rightjustfont_function():
    text_get=text_editor.get(1.0,"end")
    text_editor.tag_config("right",justify=tkinter.RIGHT)
    text_editor.delete(1.0,tkinter.END)
    text_editor.insert(tkinter.INSERT,text_get,"right")
right_just_button.config(command=rightjustfont_function)





     



window.config(menu=menubar_space)

window.mainloop()
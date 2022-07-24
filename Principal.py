from email import message 
from tkinter import mainloop, messagebox as MessageBox
import tkinter as tk #import all of tkinter for new frame or window 
frame = tk.Tk()#new instance type TK
frame.title("### SYSTEM FOR ENCRYPTION YOUR MESSAGES ###")#write title at the top of window
frame.geometry("1000x670")#size of the window
#set the image for icon at the window
frame.iconbitmap("C:/Users/Acces/Documents/WORKSPACE/ENCRIPTADOR Y DESENCRIPTADOR/Images/Encryption.ico")
#remove resizable shape
frame.resizable(width=False,height=False)
#set image as background
imagen_bg = tk.PhotoImage(file = "C:/Users/Acces/Documents/WORKSPACE/ENCRIPTADOR Y DESENCRIPTADOR/Images/InputOuput.png")
imagen_bg1 = tk.Label(frame, image=imagen_bg).place(x=0,y=0,relwidth=1,relheight=1)
# --------------------------------- BUTTONS -----------------------------------------------------------------
# ----------------------------------- MODULE -> BUTTON CONVERT -----------------------------------------------------
def __Convert__():
    resultado = MessageBox.askquestion("ATENTION", "(YES) TO ENCRYPT, (NO) TO DECRYPT")#POP-UP WINDOW
    if resultado == "yes":
        message = EntryTxt.get(1.0, "end-1c")#Get text box content
        #print("LA LONGITUD ES: ",len(list_encrypt)) #this method is used to know the size of the list
        #print(list_encrypt[0])#show the element related to the index
        __Encrypt__(message)
    else:
        desmessage = EntryTxt.get(1.0, "end-1c")#Get text box content
        __Decrypt__(desmessage)
        #frame.destroy()  #REVISE THE TEXT
# ----------------------------------- MODULE -> DECRYPT ------------------------------------------------------------
def __Decrypt__(desmessage):
    list_encrypt = list(desmessage)# Convert string to list
    encrypt_mess = __Algorithm_DeC__(list_encrypt)# get encrypted list
    Message_fish = "".join(map(str, encrypt_mess))# 
    LbText = tk.Label(frame, text= Message_fish, wraplength=390,width=58, height=35, bg="white",justify=tk.CENTER)
    LbText.place(x=511,y=75)
def __Algorithm_DeC__(list_encrypt):
    new_list = []
    for char in list_encrypt:
        new_mess = int(ord(char))
        if new_mess == 255:
            new_mess = 0
            var = (new_mess -1)
            nchar = chr(var)
            new_list.append(nchar)
        else:
            var = (new_mess -1)
            nchar = chr(var)
            new_list.append(nchar)
    return new_list
# ----------------------------------- MODULE -> ENCRYPT ------------------------------------------------------------
def __Encrypt__(message):
    list_encrypt = list(message)# Convert string to list
    encrypt_mess = __Algorithm__(list_encrypt)# get encrypted list
    Message_fish = "".join(map(str, encrypt_mess))# 
    LbText = tk.Label(frame, text= Message_fish, wraplength=390,width=58, height=35, bg="white",justify=tk.CENTER)
    LbText.place(x=511,y=75)
def __Algorithm__(list_encrypt):
    new_list = []
    for char in list_encrypt:
        new_mess = int(ord(char))
        if new_mess == 255:
            new_mess = 0
            var = (new_mess +1)
            nchar = chr(var)
            new_list.append(nchar)
        else:
            var = (new_mess +1)
            nchar = chr(var)
            new_list.append(nchar)
    return new_list
# ----------------------------------------- colors ----------------------------------------------------------
color_buttons = "#224c8d"
color_panel = "#deeaf6"
# ----------------------------------- BUTTON CONFIGURATION ---------------------------------------------
button_convert = tk.Button(frame, text="CONVERT", cursor="hand2", command= __Convert__ ,bg=color_buttons, fg= "white",width=12, relief="flat",
    font=("Comic Sans MS",13, "bold"))
button_convert.place(x=280,y=615)#Button cordinates
# ----------------------------------- BUTTON CONFIGURATION 2 --------------------------------------------
button_copy = tk.Button(frame, text="COPY", cursor="hand2",bg=color_buttons, fg= "white",width=12, relief="flat",
    font=("Comic Sans MS",13, "bold"))
button_copy.place(x=615,y=615)
# ----------------------------------- TEXT'S BOX INPUT ----------------------------------------------------------
EntryTxt = tk.Text(frame, width=58, height=30, bg=color_panel)
EntryTxt.place(x=22,y=75)
# ----------------------------------- LABEL OUTPUT ---------------------------------------------------------
#LbText = tk.Label(frame, width=58, height=30, bg="white"l)
#EntryTxtO.place(x=511,y=75)
frame.mainloop()#method to show the window in the screen 
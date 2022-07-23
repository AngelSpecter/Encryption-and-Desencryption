from email import message 
from tkinter import messagebox as MessageBox
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
    resultado = MessageBox.askquestion("ATENTION", "ADDED A LINE BREAK FOR EACH LINE?")#POP-UP WINDOW
    if resultado == "no":
        frame.destroy()  #REVISE THE TEXT
    message = EntryTxt.get(1.0, "end-1c")#Get text box content
    LbText = tk.Label(frame, text= message, width=58, height=30, bg="white",justify=tk.CENTER)
    LbText.place(x=511,y=75)
    list_encrypt = list(message)
    #print("LA LONGITUD ES: ",len(list_encrypt)) #this method is used to know the size of the list
    #print(list_encrypt[0])#show the element related to the index
    __Encrypt__(list_encrypt)
# ----------------------------------- MODULE -> ENCRYPTION ------------------------------------------------------------
def __Encrypt__(list_encrypt):
    print("LA LONGITUD ES: ",len(list_encrypt)) #this method is used to know the size of the list
    print(list_encrypt[0])#show the element related to the index
# ----------------------------------------- colors ----------------------------------------------------------
color_buttons = "#224c8d"
color_panel = "#deeaf6"
# ----------------------------------- BUTTON CONFIGURATION ---------------------------------------------
button_convert = tk.Button(frame, text="CONVERT", cursor="hand2", command= __Convert__ ,bg=color_buttons, fg= "white",width=12, relief="flat",
    font=("Comic Sans MS",13, "bold"))
button_convert.place(x=280,y=615)#Button cordinates
# ----------------------------------- BUTTON CONFIGURATION 2 --------------------------------------------
button_send = tk.Button(frame, text="SEND", cursor="hand2",bg=color_buttons, fg= "white",width=12, relief="flat",
    font=("Comic Sans MS",13, "bold"))
button_send.place(x=615,y=615)
# ----------------------------------- TEXT'S BOX INPUT ----------------------------------------------------------
EntryTxt = tk.Text(frame, width=58, height=30, bg=color_panel)
EntryTxt.place(x=22,y=75)
# ----------------------------------- LABEL OUTPUT ---------------------------------------------------------
#LbText = tk.Label(frame, width=58, height=30, bg="white"l)
#EntryTxtO.place(x=511,y=75)
frame.mainloop()#method to show the window in the screen 
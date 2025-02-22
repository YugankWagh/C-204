#------------- Boilerplate Code Start------
import socket
from tkinter import *
from  threading import Thread
from PIL import ImageTk, Image

screen_width = None
screen_height = None

SERVER = None
PORT = None
IP_ADDRESS = None


canvas1 = None

playerName = None
nameEntry = None
nameWindow = None

#------------- Boilerplate Code End------


# Student write saveName() here
def saveName():
    global SERVER
    global playerName
    global nameWindow
    global nameEntry
    playerName=nameEntry.get()
    nameEntry.delete(0,END)
    nameWindow.destroy()
    SERVER.send(playerName.encode())



def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow
    global canvas1
    global screen_width
    global screen_height

    nameWindow  = Tk()
    nameWindow.title("Ludo Ladder")
    nameWindow.attributes('-fullscreen',True)


    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file = "./assets/background.png")

    canvas1 = Canvas( nameWindow, width = 500,height = 500)
    canvas1.pack(fill = "both", expand = True)
    # Display image
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    canvas1.create_text( screen_width/2, screen_height/5 , text = "Enter Name", font=("Chalkboard SE",50), fill="white")

    nameEntry = Entry(nameWindow, width=10, justify='center', font=('Chalkboard SE', 50), bd=5, bg='white')
    nameEntry.place(x = screen_width/2 - 220, y=screen_height/4 + 100)

    button = Button(nameWindow, text="Save", font=("Chalkboard SE", 30),width=10, command=saveName, height=1, bg="green", bd=3)
    button.place(x = screen_width/2 - 130, y=screen_height/2 - 30)

    button = Button(nameWindow, text="Next Screen", font=("Chalkboard SE", 30),width=10, command=saveName, height=1, bg="White", bd=3)
    button.place(x = screen_width/2 - 130, y=screen_height/2 + 60 )

    nameWindow.resizable(True, True)
    nameWindow.mainloop()



# Boilerplate Code
def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT  = 5000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))


    # Creating First Window
    askPlayerName()




setup()

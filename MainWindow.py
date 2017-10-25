from tkinter import *

from tkinter import messagebox

# Set window size
top = Tk()
top.geometry("500x500")
top.title("Rocket GUI")
frame = Frame(top, bg="#333333")
frame.pack(fill='both', expand='yes')

# Global variables
isLaunched = False
hasAborted = False
verifyOkToLaunch = False


# Function to show abort message box
def abortMessageCallBack():
    abort_response = messagebox.askyesno("Abort Mission?", "Do you really want to abort the mission?")
    if abort_response:
        hasAborted = True
        verifyOkToLaunch = False
        abortButton.config(state=DISABLED)


# Function to show verify message box
def verifyMessageCallBack():
    verify_response = messagebox.askyesno("Verify Launch", "Do you want to verify for launch?")
    if verify_response:
        verifyOkToLaunch = True
        abortButton.config(state=NORMAL)


# Abort Mission Label
abortLabel = Label(top, text="Abort Mission:", bg="#333333", fg="#ffffff")
abortLabel.place(x=10, y=350)

# Verify Launch Label
verifyLabel = Label(top, text="Verify Launch:", bg="#333333", fg="#ffffff")
verifyLabel.place(x=10, y=400)

# Abort Mission Button
abortButton = Button(top, text="ABORT MISSION", state=DISABLED, bg="red", command=abortMessageCallBack)
abortButton.place(x=100, y=350)

# Verify Launch Button
verifyButton = Button(top, text="VERIFY LAUNCH", bg="green", command=verifyMessageCallBack)
verifyButton.place(x=100, y=400)

# Start window
top.mainloop()

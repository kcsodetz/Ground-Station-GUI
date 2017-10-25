from tkinter import *

from tkinter import messagebox

# Set window size
top = Tk()
top.geometry("500x500")

# Global variables
isLaunched = False
hasAborted = False
verifyOkToLaunch = False


# Function to show abort message box
def abortMessageCallBack():
    abortResponse = messagebox.askyesno("Abort Mission?", "Do you really want to abort the mission?")
    if abortResponse:
        hasAborted = True
        abortButton.config(state=DISABLED)


# Function to show verify message box
def verifyMessageCallBack():
    verifyResponse = messagebox.askyesno("Verify Launch", "Do you want to verify for launch?")
    if verifyResponse:
        verifyOkToLaunch = True
        abortButton.config(state=NORMAL)


# Abort Mission Button
abortButton = Button(top, text="ABORT MISSION", state=DISABLED, bg="red", command=abortMessageCallBack)
abortButton.place(x=50, y=350)

# Verify Launch Button
verifyButton = Button(top, text="Verify Launch", bg="green", command=verifyMessageCallBack)
verifyButton.place(x=50, y=400)

# Start window
top.mainloop()

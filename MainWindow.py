from tkinter import *
from tkinter import messagebox

# Set window options
top = Tk()
top.geometry("500x500")
top.title("Rocket GUI")
frame = Frame(top, bg="#333333")
frame.pack(fill='both', expand='yes')

subFrameLeft = Frame(top, bg="#3C3F41", height="300", width="245", relief=RAISED)
subFrameLeft.place(x=0, y=0)

subFrameRight = Frame(top, bg="#3C3F41", height="300", width="245", relief=RAISED)
subFrameRight.place(x=255, y=0)

# Global variables
isLaunched = False
hasAborted = False
verifyOkToLaunch = False
bgColor = "#333333"


# Function to show abort message box
def abortMessageCallBack():
    abort_response = messagebox.askyesno("Abort Mission?", "Do you really want to abort the mission?")
    if abort_response:
        hasAborted = True
        verifyOkToLaunch = False
        statusLabelChange("MISSION ABORTED")
        abortButton.config(state=DISABLED)
    else:
        hasAborted = False


# Function to show verify message box
def verifyMessageCallBack():
    verify_response = messagebox.askyesno("Verify Launch", "Do you want to verify for launch?")
    if verify_response:
        verifyOkToLaunch = True
        abortButton.config(state=NORMAL)
        statusLabelChange("VERIFIED")
    else:
        verifyOkToLaunch = False
        statusLabelChange("NOT VERIFIED")


# Abort Mission Label
abortLabel = Label(top, text="Abort Mission:", bg=bgColor, fg="white")
abortLabel.place(x=10, y=350)

# Verify Launch Label
verifyLabel = Label(top, text="Verify Launch:", bg=bgColor, fg="white")
verifyLabel.place(x=10, y=400)

# Status Label
statusLabel = Label(top, text="NOT VERIFIED", fg="orange", bg="#808080", width="20", height="2")
statusLabel.place(x=300, y=375)

# Label to mark status
statusTextLabel = Label(top, text="Current Status:", fg="white", bg=bgColor)
statusTextLabel.place(x=330, y=350)


# Function to change status label
def statusLabelChange(change_to):
    statusLabel.config(text=change_to)
    if change_to == "VERIFIED":
        statusLabel.config(fg="green")
    elif change_to == "NOT VERIFIED":
        statusLabel.config(fg="orange")
    elif change_to == "MISSION ABORTED":
        statusLabel.config(fg="red")


# Abort Mission Button
abortButton = Button(top, text="ABORT MISSION", state=DISABLED, bg="red", command=abortMessageCallBack, width="20")
abortButton.place(x=100, y=350)

# Verify Launch Button
verifyButton = Button(top, text="VERIFY LAUNCH", bg="green", command=verifyMessageCallBack, cursor="shuttle", width="20")
verifyButton.place(x=100, y=400)

# Start window
top.mainloop()

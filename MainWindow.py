from tkinter import *
from tkinter import messagebox

# Set window options
top = Tk()
top.geometry("600x600")
hxw = 600  # height and width of top frame
top.title("Rocket GUI V 0.1")

# ============================ #
# ========== FRAMES ========== #
# ============================ #

# Initialize uppermost frame
frame = Frame(top, width=hxw, height=hxw, bg="#333333")
frame.pack(fill='both', expand='yes')

# Initialize and place subFrameLeft
subFrameLeft = Frame(top, bg="#3C3F41", height="300", width=hxw / 2 - 5, relief=RAISED)
subFrameLeft.place(x=0, y=5)

# Initialize and place subFrameRight
subFrameRight = Frame(top, bg="#3C3F41", height="300", width=hxw / 2 - 5, relief=RAISED)
subFrameRight.place(x=hxw / 2 + 5, y=5)

# Initialize and place subFrameBottom
subFrameBottom = Frame(top, bg="#3C3F41", height="200", width=hxw, relief=RAISED)
subFrameBottom.place(x=0, y=hxw - 285)

# ============================ #
# ===== GLOBAL VARIABLES ===== #
# ============================ #

isLaunched = False  # has the rocket launched?
hasAborted = False  # has the process been aborted?
verifyOkToLaunch = False  # is the system verified for launch?
bgColor = "#333333"  # background color
subFrameColor = "#3C3F41"  # sub frame background color
standardTextWidth = 18


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


# ============================ #
# ========== LABELS ========== #
# ============================ #

# Abort Mission Label
abortLabel = Label(subFrameBottom, text="Abort Mission:", bg=bgColor, fg="white")
abortLabel.place(x=10, y=55)

# Verify Launch Label
verifyLabel = Label(subFrameBottom, text="Verify Launch:", bg=bgColor, fg="white")
verifyLabel.place(x=10, y=125)

# Status Label to show real time status
statusLabel = Label(subFrameBottom, text="NOT VERIFIED", fg="orange", bg="#808080", width="20", height="2")
statusLabel.place(x=hxw / 2 + hxw / 8, y=80)

# Label to mark status
statusTextLabel = Label(subFrameBottom, text="Current Status:", fg="white", bg=bgColor)
statusTextLabel.place(x=hxw / 2 + hxw / 8 + 30, y=50)

# SubFrameLeft Label: Environmental Data
frameLeftLabel = Label(subFrameLeft, text="Environmental Data:", fg="white", bg=subFrameColor)
frameLeftLabel.place(x=(hxw / 2) / 4 + 15, y=5)

# SubFrameLeft Label: System Data
frameRightLabel = Label(subFrameRight, text="System Data:", fg="white", bg=subFrameColor)
frameRightLabel.place(x=(hxw / 2) / 4 + 20, y=5)

# Temperature Label
tempLabel = Label(subFrameLeft, text="Temperature (Celsius): ", fg="white", bg=bgColor, width=standardTextWidth)
tempLabel.place(x=10, y=40)

# Altitude Label
altLabel = Label(subFrameRight, text="Altitude (Meters): ", fg="white", bg=bgColor, width=standardTextWidth)
altLabel.place(x=10, y=40)

# Pressure Label
pressureLabel = Label(subFrameLeft, text="Pressure (kPa): ", fg="white", bg=bgColor, width=standardTextWidth)
pressureLabel.place(x=10, y=80)

# Cardinal Direction Label
cardinalLabel = Label(subFrameRight, text="Direction (Degrees): ", fg="white", bg=bgColor, width=standardTextWidth)
cardinalLabel.place(x=10, y=80)

# Humidity Label
humidLabel = Label(subFrameLeft, text="Humidity (Percent): ", fg="white", bg=bgColor, width=standardTextWidth)
humidLabel.place(x=10, y=120)

# Acceleration Label
accLabel = Label(subFrameRight, text="Acceleration (M/s/s): ", fg="white", bg=bgColor, width=standardTextWidth)
accLabel.place(x=10, y=120)

# Velocity Label
velocityLabel = Label(subFrameRight, text="Velocity (M/s): ", fg="white", bg=bgColor, width=standardTextWidth)
velocityLabel.place(x=10, y=160)

# Angle Label
angleLabel = Label(subFrameRight, text="Angle (Degrees): ", fg="white", bg=bgColor, width=standardTextWidth)
angleLabel.place(x=10, y=200)


# Function to change status label
def statusLabelChange(change_to):
    statusLabel.config(text=change_to)
    if change_to == "VERIFIED":
        statusLabel.config(fg="green")
    elif change_to == "NOT VERIFIED":
        statusLabel.config(fg="orange")
    elif change_to == "MISSION ABORTED":
        statusLabel.config(fg="red")


# Function to update Environment Data
# def updateEnvironment ():

# Abort Mission Button
abortButton = Button(subFrameBottom, text="ABORT MISSION", state=DISABLED, bg="red", command=abortMessageCallBack,
                     width="20")
abortButton.place(x=100, y=55)

# Verify Launch Button
verifyButton = Button(subFrameBottom, text="VERIFY LAUNCH", bg="green", command=verifyMessageCallBack, cursor="shuttle",
                      width="20")
verifyButton.place(x=100, y=125)

# Start window
top.mainloop()

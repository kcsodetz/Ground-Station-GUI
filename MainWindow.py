from tkinter import *
from tkinter import messagebox

"""
ROCKET GUI Version 0.1

Author: Ken Sodetz
Since: 10/11/2017

Created for Purdue Orbital Electrical and Software Sub team

Parses and displays data from the a Raspberry Pi 3 to verbosely
display all pertinent system data (data that can be changed) and environmental 
data (data that cannot be changed). 

"""

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
# ==== MENU BAR & COMMANDS === #
# ============================ #

def donothing():
    file_window = Toplevel(top)
    button = Button(file_window, text="Close")
    button.pack()


def about():
    about_window = Toplevel(top, height=100, width=100)
    close_button = Button(about_window, text="Close")
    close_button.pack()


menuBar = Menu(top)
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Restart", command=donothing)
fileMenu.add_command(label="Close", command=donothing)

fileMenu.add_separator()

fileMenu.add_command(label="Exit", command=top.quit)
menuBar.add_cascade(label="File", menu=fileMenu)

helpmenu = Menu(menuBar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menuBar.add_cascade(label="Help", menu=helpmenu)

top.config(menu=menuBar)

# ============================ #
# ===== GLOBAL VARIABLES ===== #
# ============================ #

is_launched = False  # has the rocket launched?
has_aborted = False  # has the process been aborted?
verify_ok_to_launch = False  # is the system verified for launch?
bgColor = "#333333"  # background color
subFrameColor = "#3C3F41"  # sub frame background color
standardTextWidth = 18  # standard text width
standardDataWidth = 10  # standard data width
angle_result = "null"

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

# Temperature Data
tempDataLabel = Label(subFrameLeft, text="NULL", fg="white", bg=bgColor, width=standardDataWidth)
tempDataLabel.place(x=160, y=40)

# Altitude Label
altLabel = Label(subFrameRight, text="Altitude (Meters): ", fg="white", bg=bgColor, width=standardTextWidth)
altLabel.place(x=10, y=40)

# Altitude Data
altDataLabel = Label(subFrameRight, text="NULL", fg="white", bg=bgColor, width=standardDataWidth)
altDataLabel.place(x=160, y=40)

# Pressure Label
pressureLabel = Label(subFrameLeft, text="Pressure (kPa): ", fg="white", bg=bgColor, width=standardTextWidth)
pressureLabel.place(x=10, y=80)

# Pressure Data
pressureDataLabel = Label(subFrameLeft, text="NULL", fg="white", bg=bgColor, width=standardDataWidth)
pressureDataLabel.place(x=160, y=80)

# Cardinal Direction Label
cardinalLabel = Label(subFrameRight, text="Direction (°): ", fg="white", bg=bgColor, width=standardTextWidth)
cardinalLabel.place(x=10, y=80)

# Cardinal Direction Data
cardinalDataLabel = Label(subFrameRight, text="NULL", fg="white", bg=bgColor, width=standardDataWidth)
cardinalDataLabel.place(x=160, y=80)

# Humidity Label
humidLabel = Label(subFrameLeft, text="Humidity (Percent): ", fg="white", bg=bgColor, width=standardTextWidth)
humidLabel.place(x=10, y=120)

# Humidity Data
humidityDataLabel = Label(subFrameLeft, text="NULL", fg="white", bg=bgColor, width=standardDataWidth)
humidityDataLabel.place(x=160, y=120)

# Acceleration Label
accLabel = Label(subFrameRight, text="Acceleration (M/s/s): ", fg="white", bg=bgColor, width=standardTextWidth)
accLabel.place(x=10, y=120)

# Acceleration Data
accDataLabel = Label(subFrameRight, text="NULL", fg="white", bg=bgColor, width=standardDataWidth)
accDataLabel.place(x=160, y=120)

# Velocity Label
velocityLabel = Label(subFrameRight, text="Velocity (M/s): ", fg="white", bg=bgColor, width=standardTextWidth)
velocityLabel.place(x=10, y=160)

# Velocity Data
velocityDataLabel = Label(subFrameRight, text="NULL", fg="white", bg=bgColor, width=standardDataWidth)
velocityDataLabel.place(x=160, y=160)

# Angle Label
angleLabel = Label(subFrameRight, text="Angle (°): ", fg="white", bg=bgColor, width=standardTextWidth)
angleLabel.place(x=10, y=200)

# Angle Data
angleDataLabel = Label(subFrameRight, text="NULL", fg="white", bg=bgColor, width=standardDataWidth)
angleDataLabel.place(x=160, y=200)

# Angle Entry Label
angleEntryLabel = Label(subFrameLeft, text="Positive angle between 30° and 75°", fg="white", bg=subFrameColor,
                        width=26)
angleEntryLabel.place(x=40, y=230)


# ============================ #
# == UPDATE LABEL FUNCTIONS == #
# ============================ #

# Function to change status label
def statusLabelChange(change_to):
    statusLabel.config(text=change_to)
    if change_to == "VERIFIED":
        statusLabel.config(fg="green")
    elif change_to == "NOT VERIFIED":
        statusLabel.config(fg="orange")
    elif change_to == "MISSION ABORTED":
        statusLabel.config(fg="red")


# Function to show abort message box
def abortMessageCallBack():
    abort_response = messagebox.askyesno("Abort Mission?", "Do you really want to abort the mission?")
    if abort_response:
        has_aborted = True
        verify_ok_to_launch = False
        statusLabelChange("MISSION ABORTED")
        abortButton.config(state=DISABLED)
    else:
        has_aborted = False


# Function to show verify message box
def verifyMessageCallBack():
    verify_response = messagebox.askyesno("Verify Launch", "Do you want to verify for launch?")
    if verify_response:
        verify_ok_to_launch = True
        abortButton.config(state=NORMAL)
        statusLabelChange("VERIFIED")
    else:
        verify_ok_to_launch = False
        statusLabelChange("NOT VERIFIED")
        abortButton.config(state=DISABLED)


def getAngle():
    angle_result = angleEntry.get()
    angle_result = float(angle_result)
    if 30.0 <= angle_result <= 75.0:
        angleDataLabel.config(text=angle_result)


# TODO: Implement update function for environment data
# Function to update Environment Data
# def updateEnvironment ():

# ============================ #
# ==== BUTTONS AND ENTRIES === #
# ============================ #

# Abort Mission Button
abortButton = Button(subFrameBottom, text="ABORT MISSION", state=DISABLED, bg="red", command=abortMessageCallBack,
                     width="20")
abortButton.place(x=100, y=55)

# Verify Launch Button
verifyButton = Button(subFrameBottom, text="VERIFY LAUNCH", bg="green", command=verifyMessageCallBack, cursor="shuttle",
                      width="20")
verifyButton.place(x=100, y=125)

# Angle Entry
angleEntry = Entry(subFrameLeft, bd=5, bg=bgColor, fg="white", width=standardDataWidth, textvariable=angle_result)
angleEntry.place(x=40, y=260)

# Get Angle Input Button
angleInputButton = Button(subFrameLeft, text="ENTER", width=8, command=getAngle)
angleInputButton.place(x=160, y=260)

# Start window
top.mainloop()

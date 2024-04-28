import tkinter as tk
from FootballValuePredictorModel import *


# The below code was retrieved from:
# https://stackoverflow.com/questions/3352918/how-to-center-a-window-on-the-screen-in-tkinter on the 30/03/2024
# Creates and centres the main window, Stops it from being resizable by the user
win = tk.Tk()
win.title("Football Player Value Predictor")
win.resizable(False, False)
window_height = 300
window_width = 500
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
x_coordinate = int((screen_width/2) - (window_width/2))
y_coordinate = int((screen_height/2) - (window_height/2))

win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))


def calculatepressed():
    if ageVar.get().isdigit():
        if heightVar.get().isdigit():
            if weightVar.get().isdigit():
                if overallVar.get().isdigit():
                    if potentialVar.get().isdigit():
                        if wageVar.get().isdigit():
                            if reputationVar.get().isdigit():
                                if weakFootVar.get().isdigit():
                                    if skillMoveVar.get().isdigit():
                                        if paceVar.get().isdigit():
                                            if shootingVar.get().isdigit():
                                                if passingVar.get().isdigit():
                                                    if dribblingVar.get().isdigit():
                                                        if defendingVar.get().isdigit():
                                                            if physicalVar.get().isdigit():
                                                                predictvalue()
                                                            else:
                                                                ResultLabel.config(
                                                                    text="Please Only Enter Numbers Into The Physical "
                                                                         "Field")
                                                                ResultLabel.place(relx=0.5, rely=1, anchor="s")
                                                        else:
                                                            ResultLabel.config(
                                                                text="Please Only Enter Numbers Into The Defending "
                                                                     "Field")
                                                            ResultLabel.place(relx=0.5, rely=1, anchor="s")
                                                    else:
                                                        ResultLabel.config(
                                                            text="Please Only Enter Numbers Into The Dribbling Field")
                                                        ResultLabel.place(relx=0.5, rely=1, anchor="s")
                                                else:
                                                    ResultLabel.config(
                                                        text="Please Only Enter Numbers Into The Passing Field")
                                                    ResultLabel.place(relx=0.5, rely=1, anchor="s")
                                            else:
                                                ResultLabel.config(
                                                    text="Please Only Enter Numbers Into The Shooting Field")
                                                ResultLabel.place(relx=0.5, rely=1, anchor="s")
                                        else:
                                            ResultLabel.config(text="Please Only Enter Numbers Into The Pace Field")
                                            ResultLabel.place(relx=0.5, rely=1, anchor="s")
                                    else:
                                        ResultLabel.config(text="Please Only Enter Numbers Into The Skill Moves Field")
                                        ResultLabel.place(relx=0.5, rely=1, anchor="s")
                                else:
                                    ResultLabel.config(text="Please Only Enter Numbers Into The Weak Foot Field")
                                    ResultLabel.place(relx=0.5, rely=1, anchor="s")
                            else:
                                ResultLabel.config(text="Please Only Enter Whole Numbers Into The Reputation Field")
                                ResultLabel.place(relx=0.5, rely=1, anchor="s")
                        else:
                            ResultLabel.config(text="Please Only Enter Whole Numbers Into The Wage Field")
                            ResultLabel.place(relx=0.5, rely=1, anchor="s")
                    else:
                        ResultLabel.config(text="Please Only Enter Whole Numbers Into The Potential Field")
                        ResultLabel.place(relx=0.5, rely=1, anchor="s")
                else:
                    ResultLabel.config(text="Please Only Enter Whole Numbers Into The Overall Field")
                    ResultLabel.place(relx=0.5, rely=1, anchor="s")
            else:
                ResultLabel.config(text="Please Only Enter Whole Numbers Into The Weight Field")
                ResultLabel.place(relx=0.5, rely=1, anchor="s")
        else:
            ResultLabel.config(text="Please Only Enter Whole Numbers Into The Height Field")
            ResultLabel.place(relx=0.5, rely=1, anchor="s")
    else:
        ResultLabel.config(text="Please Only Enter Whole Numbers Into The Age Field")
        ResultLabel.place(relx=0.5, rely=1, anchor="s")


def predictvalue():
    playerinfo = (ageVar.get(), heightVar.get(), weightVar.get(), overallVar.get(), potentialVar.get(), wageVar.get(),
                  reputationVar.get(), weakFootVar.get(), skillMoveVar.get(), paceVar.get(), shootingVar.get(),
                  passingVar.get(), dribblingVar.get(), defendingVar.get(), physicalVar.get())
    valueprediction = modelToUse.predict([playerinfo])
    ResultLabel.config(text="You're Predicted Value Is: " + str(valueprediction))
    ResultLabel.place(relx=0.5, rely=1, anchor="s")


# Defines the variables needed for the Entry Widgets
ageVar = tk.StringVar()
heightVar = tk.StringVar()
weightVar = tk.StringVar()
overallVar = tk.StringVar()
potentialVar = tk.StringVar()
wageVar = tk.StringVar()
reputationVar = tk.StringVar()
weakFootVar = tk.StringVar()
skillMoveVar = tk.StringVar()
paceVar = tk.StringVar()
shootingVar = tk.StringVar()
passingVar = tk.StringVar()
dribblingVar = tk.StringVar()
defendingVar = tk.StringVar()
physicalVar = tk.StringVar()

# Creates the label that is placed next to the Age Entry Widget
ageLabel = tk.Label(win, text="Age:")
ageLabel.place(x=70, y=25)

# Creates the Age Entry Widget
ageEntry = tk.Entry(win, textvariable=ageVar, bg="light blue")
ageEntry.place(x=100, y=25)

# Create the label that is placed next to the Height Entry Widget
heightLabel = tk.Label(win, text="Height:")
heightLabel.place(x=255, y=25)

# Creates the Height Entry Widget
heightEntry = tk.Entry(win, textvariable=heightVar, bg="light blue")
heightEntry.place(x=300, y=25)

# Creates the label that is placed next to the Weight Entry Widget
weightLabel = tk.Label(win, text="Weight:")
weightLabel.place(x=50, y=50)

# Creates the Weight Entry Widget
weightEntry = tk.Entry(win, textvariable=weightVar, bg="light blue")
weightEntry.place(x=100, y=50)

# Create the label that is placed next to the Overall Entry Widget
overallLabel = tk.Label(win, text="Overall:")
overallLabel.place(x=255, y=50)

# Creates the Overall Entry Widget
overallEntry = tk.Entry(win, textvariable=overallVar, bg="light blue")
overallEntry.place(x=300, y=50)

# Creates the label that is placed next to the Potential Entry Widget
potentialLabel = tk.Label(win, text="Potential:")
potentialLabel.place(x=40, y=75)

# Creates the Potential Entry Widget
potentialEntry = tk.Entry(win, textvariable=potentialVar, bg="light blue")
potentialEntry.place(x=100, y=75)

# Create the label that is placed next to the Wage Entry Widget
wageLabel = tk.Label(win, text="Wage:")
wageLabel.place(x=260, y=75)

# Creates the Wage Entry Widget
wageEntry = tk.Entry(win, textvariable=wageVar, bg="light blue")
wageEntry.place(x=300, y=75)

# Creates the label that is placed next to the Reputation Entry Widget
reputationLabel = tk.Label(win, text="Reputation:")
reputationLabel.place(x=30, y=100)

# Creates the Reputation Entry Widget
reputationEntry = tk.Entry(win, textvariable=reputationVar, bg="light blue")
reputationEntry.place(x=100, y=100)

# Create the label that is placed next to the Weak Foot Entry Widget
weakFootLabel = tk.Label(win, text="Weak Foot:")
weakFootLabel.place(x=235, y=100)

# Creates the Weak Foot Entry Widget
weakFootEntry = tk.Entry(win, textvariable=weakFootVar, bg="light blue")
weakFootEntry.place(x=300, y=100)

# Creates the label that is placed next to the Skill Moves Entry Widget
skillMoveLabel = tk.Label(win, text="Skill Moves:")
skillMoveLabel.place(x=30, y=125)

# Creates the Skill Moves Entry Widget
skillMoveEntry = tk.Entry(win, textvariable=skillMoveVar, bg="light blue")
skillMoveEntry.place(x=100, y=125)

# Creates the label that is placed next to the Pace Entry Widget
paceLabel = tk.Label(win, text="Pace:")
paceLabel.place(x=265, y=125)

# Creates the Pace Entry Widget
paceEntry = tk.Entry(win, textvariable=paceVar, bg="light blue")
paceEntry.place(x=300, y=125)

# Create the label that is placed next to the Shooting Entry Widget
shootingLabel = tk.Label(win, text="Shooting:")
shootingLabel.place(x=40, y=150)

# Creates the Shooting Entry Widget
shootingEntry = tk.Entry(win, textvariable=shootingVar, bg="light blue")
shootingEntry.place(x=100, y=150)

# Creates the label that is placed next to the Passing Entry Widget
passingLabel = tk.Label(win, text="Passing:")
passingLabel.place(x=250, y=150)

# Creates the Passing Entry Widget
passingEntry = tk.Entry(win, textvariable=passingVar, bg="light blue")
passingEntry.place(x=300, y=150)

# Create the label that is placed next to the Dribbling Entry Widget
dribblingLabel = tk.Label(win, text="Dribbling:")
dribblingLabel.place(x=40, y=175)

# Creates the Dribbling Entry Widget
dribblingEntry = tk.Entry(win, textvariable=dribblingVar, bg="light blue")
dribblingEntry.place(x=100, y=175)

# Creates the label that is placed next to the Defending Entry Widget
defendingLabel = tk.Label(win, text="Defending:")
defendingLabel.place(x=235, y=175)

# Creates the Defending Entry Widget
defendingEntry = tk.Entry(win, textvariable=defendingVar, bg="light blue")
defendingEntry.place(x=300, y=175)

# Create the label that is placed next to the Physical Entry Widget
physicalLabel = tk.Label(win, text="Shooting:")
physicalLabel.place(x=40, y=200)

# Creates the Physical Entry Widget
physicalEntry = tk.Entry(win, textvariable=physicalVar, bg="light blue")
physicalEntry.place(x=100, y=200)


CalculateButton = tk.Button(win, text="Calculate", command=calculatepressed)
CalculateButton.place(x=218, y=250)
# Creates the calculate button

ResultLabel = tk.Label(win, text="Predicted Value: ")
ResultLabel.place(relx=0.5, rely=1, anchor="s")
# Creates the label that is used to display the predicted value and error messages and centres it at the bottom.

win.mainloop()
# Runs the window

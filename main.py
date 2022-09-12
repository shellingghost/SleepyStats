import PySimpleGUI as sg
from matplotlib import pyplot as plt


# data structures for axis building
dateX = []
bedtimeY = []
exerciseY = []
meditateY = []
moodY = []

def set_scale(scale):
    root = sg.tk.Tk()
    root.tk.call('tk', 'scaling',scale)
    root.destroy()

def stripFunc(general_dictionary):
    # strip input from general dictionary after 'Save' button is pressed
    # append onto appropriate lists to be used for graph building
    # '-INPUT-' is the date
    # '-INPUT-0' is in bed on time
    # '-INPUT-1' is exercise goals met
    # '-INPUT-2' is meditation level
    # '-INPUT-3' is mood level
    dateX.append(values['-INPUT-'])
    bedtimeY.append(values['-INPUT-0'])
    exerciseY.append(values['-INPUT-1'])
    meditateY.append(values['-INPUT-2'])
    moodY.append(values['-INPUT-3'])


# Define the window's contents
# Added parameter 'do_not_clear' to remove manual overwrite of values


layout = [[sg.Text("Welcome to SleepyStats!")],
          [sg.Text("Please rate your efforts on a scale of 1-10 for the following categories")],
          [sg.Text("Please enter the date in a Month/Day/Year format")],
          [sg.Input(key='-INPUT-', do_not_clear=False)],
          [sg.Text("How close were you to reaching bed goals?")],
          [sg.Input(key='-INPUT-', do_not_clear=False)],
          [sg.Text("Did you exercise enough?")],
          [sg.Input(key='-INPUT-', do_not_clear=False)],
          [sg.Text("Did you meditate enough?")],
          [sg.Input(key='-INPUT-', do_not_clear=False)],
          [sg.Text("Rate your mood")],
          [sg.Input(key='-INPUT-', do_not_clear=False)],

          # Buttons for events in 'while True' loop
          [sg.Button('Save')],
          [sg.Button("Visualize")],
          [sg.Button('Quit')]]

# Create the window
window = sg.Window('Window Title', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    print(event)
    print(values)
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    # Stripping Gen Dict for user input and clearing entered text*
    if event == 'Save':
        # call stripFunc and clear input areas
        stripFunc(values)

    # visualize all the information we inputted by creating a graph with plt
    if event == "Visualize":
        plt.title('Sleepy Stats')
        plt.xlabel('Dates')
        plt.ylabel('Scale')



        plt.plot(dateX, bedtimeY, label='Bed Time')
        plt.plot(dateX, exerciseY, label='Exercise')
        plt.plot(dateX, meditateY, label='Meditate')
        plt.plot(dateX,moodY, color='k', linestyle='--', label='Mood')

        # Create a legend for labels
        plt.legend()

        # Save graph we created and close the window
        plt.savefig('myfig.png')
        window.close()

# Finish up by removing from the screen
window.close()
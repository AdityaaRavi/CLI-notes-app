# This python file is meant to be used as a test-bed to test each offline server function.
# This file will also be the acting user-interface until a proper GUI client is built.

# importing all the features from the features directory
from OflineFeatures import TxtNoteCreatingFunctions as editor
from OflineFeatures import LabelIndexSearch as labeler

# Importing other required libraries
from datetime import date

# Actual program tester code
print("Welcome to LAN-wide notes app's server side intermittent UI.\n")

# A Dictionary that contains a list of all the commands that currently exist, and what they do.
commands_dict = dict()

# ### Creating a label object that indexes and keeps note of all the files currently in the app,
# ### and moves files to appropriate folders based on their labels
label = labeler.LabelInstance()

# Add all the commands that this program can currently execute in the above dict
commands_dict["label [old_label/file_name.txt] [new_label]"] = "Change the label of file_name.txt to the given [new_label]"
commands_dict["quit"] = "Quit this program"
commands_dict["start_txt_editor"] = "Start the inbuilt text editor which creates a text file with the given" + \
                                    " data, in the format needed for the other features of this app to work"
commands_dict["search"] = "Start searching for a note using its name, label and most recent date of modification" \
                          + "Or any combination of both"
commands_dict["open [path]"] = "Open the file at the given path if it exists"

# A function that reads the given user_command and calls the appropriate method to execute it.
def execute_command(command):
    # Quiting the program if requested by the user
    if(command.startswith("quit")):
        print("Saving all Changes and exiting the program...")
        label.updateDisk()
        quit()

    # calling the label method.
    if(command.startswith("label")):
        parameters = command.split(" ")
        if(len(parameters) != 3):
            print("Please recheck your format.")
        else:
            # Call the label function here.
            try:
                label.changeLabel(parameters[1], parameters[2], date.today().strftime("%m.%d.%Y"))
            except(FileNotFoundError):
                print("No such file found, please double check the label and name of the file! ")
                print("Call the command again with vaild parameters as defined in the help dialog and above line to"
                      + " continue")

    # starting the txt editor
    if(command.startswith("start_txt_editor")):
        # asking the user if they want create or edit a text file
        mode = input("Do you want to edit a text file or create a new one?\nAnswer"
                     + " \"" + editor.EDIT_FILE_TOKEN + "\" or \"" + editor.NEW_FILE_TOKEN + "\": ")

        if(not mode == editor.EDIT_FILE_TOKEN and not mode == editor.NEW_FILE_TOKEN):
            print("Invalid mode string, try again!")
            execute_command("start_txt_editor")

        # initiatating and starting the text editor
        file = editor.EditorInstance(mode, label)
        file.start()

    # Opening the text editor on a file at the path given by the user
    if (command.startswith("open")):
        parameters = command.split(" ")
        if (len(parameters) != 2):
            print("Please recheck your format.")
        else:
            given_path = parameters[1]
            editor.EditorInstance(label, given_path, 1)

    # Starting the search function
    if(command.startswith("search")):
        given_name = input("Name of the file (leave it blank if you don't know): ")
        given_label = input("What is the label of the file you are looking for (Leave it blank if you don't know): ")
        # ##### check if i can just pass a dictionary.
        if(not given_name == "" and not given_label == ""):
            print("Date modified, path respectively: ", label.searchFor(file_name=given_name, label=given_label))
        else:
            given_date = input("When was the last time you opened it using the inbuilt text editor?" +
                               " (Leave it blank if you don't know) MM.DD.YYYY: ")
            # Creating a dict() and filling it with all user-given non empty parameters.
            search_terms = dict()
            if(not given_name == ""):search_terms["file_name"] = given_name
            if(not given_label == ""): search_terms["label"] = given_label
            if(not given_date == ""): search_terms["date"] = given_date
            # Passing a dictionary with all given parameters to **kwarg
            labeler.printInIndexFormat(label.searchFor(**search_terms))

# An infinte loop that keeps taking in commands.
while True:
    print("\nThese are the available commands:\n", commands_dict)
    user_command = input("\nEnter the command to excute (following the same format as given above): ")
    execute_command(user_command)


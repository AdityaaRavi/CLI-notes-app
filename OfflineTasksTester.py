# This python file is meant to be used as a test-bed to test each offline server function.
# This file will also be the acting user-interface until a proper GUI client is built.

# importing all the features from the features directory
from OflineFeatures import TxtNoteCreatingFunctions as editor
# Actual program tester code
print("Welcome to LAN-wide notes app's server side intermittent UI.\n")

# A Dictionary that contains a list of all the commands that currently exist, and what they do.
commands_dict = dict()
# Add all the commands that this program can currently execute in the above dict
commands_dict["label [location/file_name.txt] [new label]"] = "Change the label of file_name.txt to the given [new_label]"
commands_dict["quit"] = "Quit this program"
commands_dict["start_txt_editor"] = "Start the inbuilt text editor which creates a text file with the given" + \
                                    " data, in the format needed for the other features of this app to work"

# A function that reads the given user_command and calls the appropriate method to execute it.
def execute_command(command):
    if(command.startswith("quit")):
        print("Exiting the program...")
        quit()

    # calling the label method.
    if(command.startswith("label")):
        parameters = command.split(" ")
        if(parameters.len() != 3):
            print("Please recheck your format.")
        else:
            # Call the label function here.
            pass

    # starting the txt editor
    if(command.startswith("start_txt_editor")):
        # asking the user if they want create or edit a text file
        mode = input("Do you want to edit a text file or create a new one?\nAnswer"
                     + " \"" + editor.EDIT_FILE_TOKEN + "\" or \"" + editor.NEW_FILE_TOKEN + "\": ")
        file = None

        if(not mode == editor.EDIT_FILE_TOKEN and not mode == editor.NEW_FILE_TOKEN):
            print("Invalid mode string, try again!")
            execute_command("start_txt_editor")

        # initiatating and starting the text editor
        file = editor.EditorInstance(mode)
        file.start()

# An infinte loop that keeps taking in commands.
while True:
    print("\nThese are the available commands:\n", commands_dict)
    user_command = input("\nEnter the command to excute (following the same format as given above): ")
    execute_command(user_command)


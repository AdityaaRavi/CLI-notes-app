# This python file is meant to be used as a test-bed to test each offline server function.
# This file will also be the acting user-interface until a proper GUI client is built.

print("Welcome to LAN-wide notes app's server side intermittent UI.\n")

# A Dictionary that contains a list of all the commands that currently exist, and what they do.
commands_dict = dict()
# Add all the commands that this program can currently execute in the above dict
commands_dict["label [location/file_name.txt] [new label]"] = "Change the label of file_name.txt to the given [new_label]"
commands_dict["quit"] = "Quit this program"


# A function that reads the given user_command and calls the appropriate method to execute it.
def execute_command(command):
    if(command.startswith("quit")):
        print("Exiting the program...")
        quit()

    if(command.startswith("label")):
        parameters = command.split(" ")
        if(parameters.len() != 3):
            print("Please recheck your format.")
        else:
            #Call the label function here.
            pass



# An infinte loop that keeps taking in commands.
while True:
    print("\nThese are the available commands:\n", commands_dict)
    user_command = input("\nEnter the command to excute (following the same format as given above): ")
    execute_command(user_command)


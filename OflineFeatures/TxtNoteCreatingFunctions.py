# This file contains the all the code and features for the first text file creator/editor
# This file contains the code needed to create a text file with the formatting currently needed for the labeling and index functions.

# Importing other required libraries
from datetime import date
from OflineFeatures import LabelIndexSearch as labelref

import os

NEW_FILE_TOKEN = "new"
EDIT_FILE_TOKEN = "edit"
# MANUAL_EDIT_TOKEN = "manual"
AUTO_EDIT_TOKEN = "auto"
NOTES_DIRECTORY = labelref.NOTES_DIRECTORY

class EditorInstance:
    task = ""
    file_name = ""
    label = ""
    lines = None
    labeler = None
    path_code = ""
    command_runner = None

    def __init__(self, labeler, mode, path, command_runner):
        if(mode == AUTO_EDIT_TOKEN):
            self.task = EDIT_FILE_TOKEN
            self.path_code = path
            self.label = str.join("/", path.split("/")[:-1])
            print("---- Editor instance created in auto mode, with the label:", self.label)
        else:
            print("---- Editor instance created in manual mode")
            self.task = mode
            self.path_code = -1

        self.lines = list()
        self.labeler = labeler
        self.command_runner = command_runner

    def start(self):
        if(self.task == NEW_FILE_TOKEN):
            self.newFile()
        elif(self.task == EDIT_FILE_TOKEN):
            self.editFile(self.path_code)

# ####### Method to create a new file and starting writing on it.
    def newFile(self):
        self.file_name = input("What do you want to be the name of your note? ")
        sure = input("Are you sure you want to proceed? Any files with the same name and label will be OVERRIDDEN...\n" +
                     "Press \"y\" to continue and anything else to quit: ")
        if(sure.lower() == "y"):
            self.label = input("What Label should this note go under? ")
            print("----------------------------------------")
            print("\nFile name: " + self.file_name)
            print("Label: " + self.label + "\n")

            # starting to take the data from the user.
            #lines = list()
            self.lines.append("File Name: " + self.file_name)
            self.lines.append("Label: " + self.label + "\n")

            # Printing a legend of all commands available
            self.printAvailableCommands()

            # listening to all commands and running the editor
            self.editorRunner()

# ####### Method to initiate the editing an existing file, pass "-1" to the "file_address" parameter if the user used
# ## start_txt_editor command to start the text editor.
    def editFile(self, file_address):
        try:
            if(file_address == -1):
                self.file_name = input("What is the name of the file you want to open" +
                                       " (Leave it blank if you don't know): ")
                self.label = input("What is the label of that file (Leave it blank if you don't know):")
                if (not self.file_name == "" and not self.label == ""):
                    file_address = NOTES_DIRECTORY + "/" + self.label + "/" + self.file_name
                else:
                    print("Ok, Starting the search feature to help you find the file....")
                    file_address = self.command_runner("search auto", getPathFromMatchingItems) # ##########################
                    self.path_code = file_address

            if (not file_address == -1): # adding edge case support in the case that 0 files match the user search terms
                file_handler = open(file_address, "r")
                self.lines = file_handler.readlines()
                file_handler.close()

                # This part of the code runs if there is in fact a file with the name the user gave
                print("File opened, here is a preview of what there is so far:\n----------------------------------------")
                for line in self.lines:
                    print(str(self.lines.index(line)) + ": "+ line, end="")
                print("\n----------------------------------------")

                # Printing a list of all available commands
                self.printAvailableCommands()
                # Starting the editor runner.
                self.editorRunner()

        except(FileNotFoundError):
            create_new_file = input("No such file exists, Do you want to create a new one? (reply \"yes\" or \"no\"): ")
            if(create_new_file.lower().startswith("yes")):
                self.newFile()
            else:
                quit_auth = input("Do you want to retry typing the name of the file correctly or quit the text editor?"
                                  + "(reply \"retry\" or \"quit\"): ").lower()
                if quit_auth.startswith("retry"): self.editFile(self.path_code)


# ######################################################## Commands common for both editing an existing file
    # #################################################### and creating a new file.

    def editorRunner(self):
        while True:
            current_line = input(str(len(self.lines)) + ": ")

            # checking if any special commands are called and executing them as necessary
            # and also quiting or skipping to the next iteration of the while loop as necessary.
            quit_auth, continue_auth = self.editorCommands(current_line)
            if (quit_auth): break
            if (continue_auth): continue

            # Adding the current line to a List for later use once it is confirmed to not be a command.
            self.lines.append(current_line)


    # ### special commands to control the text editor. Returns true if we need to leave the text editor.
    def editorCommands(self, current_line):
        lines = self.lines
        # command to quit the editor and save the text file
        if current_line == "****":
            print("----------------------------------------")
            confirmation = input("Are you sure that you want to quit? All your work till now will be saved.\n" +
                                 "Type \"y\" to confirm or any other key to cancel: ")
            if (confirmation.lower() == "y"):
                self.saveFile()
                # returning -- quit_auth and skip_while_loop_auth
                return True, False
            else:
                print("operation cancelled, continue typing")
                print("----------------------------------------")
                return False, True

        # command to edit a particular line of the file
        if current_line == "^^^^":
            print("----------------------------------------")

            line_number = int(input("Enter the line number of the line you wish to change: "))
            if (line_number > len(lines) or line_number < 1): ################################# MIGHT HAVE TO CHANGE THIS
                print("invalid line number, reissue command to try again.\nLines 0 and 1 are reserved by the program.")
                print("----------------------------------------")
                # returning -- quit_auth and skip_while_loop_auth
                return False, True

            replacement = input("Type the replacement text: ")
            lines[line_number] = replacement
            print("done! Continue typing the next line.")
            print("----------------------------------------")
            # returning -- quit_auth and skip_while_loop_auth
            return False, True
        # command to quit without saving
        if current_line == "**&&^":
            print("----------------------------------------")
            confirmation = input("Are you sure that you want to quit without saving?\n" +
                                 "Type \"y\" to confirm or any other key to cancel: ")
            if (confirmation.lower() == "y"):
                self.lines = list()
                # returning -- quit_auth and skip_while_loop_auth
                return True, False
            else:
                print("operation cancelled, continue typing")
                print("----------------------------------------")
                # returning -- quit_auth and skip_while_loop_auth
                return False, True

        # Printing available commands when asked
        if(current_line == "%%help"):
            self.printAvailableCommands()
            return False, True

        return False, False

    def printAvailableCommands(self):
        commands = dict()
        commands["****"] = "quit and save the file"
        commands["^^^^"] = "edit a previous line"
        commands["**&&^"] = "quit WITHOUT saving the file"
        commands["%%help"] = "show a list of possible commands"
        print("----------------------------------------")
        for key in commands:
            print("Type \"" + key + "\" to " + commands[key])
        print("----------------------------------------")

    def saveFile(self):
        print("Here is a preview of your file:\n----------------------------------------")
        for line in self.lines:
            print(line.strip())
        print("----------------------------------------")

        file_handler = None

        # save file tasks that have to be done when creating a new file.
        # file_handler = None
        if self.task == NEW_FILE_TOKEN:
            # creating a new text file in the base directory so that can be moved later by newFileSaved() method
            file_handler = open(self.file_name, "w")
        elif self.path_code == -1:
            # Replacing the old version of file edited here with the new one.
            file_handler = open(NOTES_DIRECTORY + "/" + self.label + "/" + self.file_name, "w")
        else:
            # Replacing the old version of file edited here with the new one.
            file_handler = open(self.path_code, "w")

        # Combining each line of the text into one string
        summative_string = ""
        for line in self.lines:
            summative_string += line.strip() + "\n"

        # Saving the file to the disk
        file_handler.write(summative_string)

        file_handler.close()

        # Updating the label index and moving the file to its appropriate place if there is any change/newly created
        new_label = self.lines[1].strip().split(" ")[1]
        if self.task == NEW_FILE_TOKEN:
            self.labeler.newFileSaved(self.file_name, new_label, date.today().strftime("%m.%d.%Y"))
        elif self.path_code == -1:
            self.labeler.changeLabel(self.label + "/" + self.file_name, new_label, date.today().strftime("%m.%d.%Y"), "not auto")
        else:
            self.labeler.changeLabel(self.path_code, new_label, date.today().strftime("%m.%d.%Y"), -1)

        print("----------------------------------------")
        print("Your file has been saved.")
        print("----------------------------------------")


# A method definition to dictate what the search feature does once it finds all possible results
def getPathFromMatchingItems(matching_items):
    answer = list()
    for name, label in matching_items:
        answer.append((name, label, matching_items[name, label][1]))

    if(len(answer) < 1):
        print("No results matched your search criteria, please try again.")
        return -1

    print("These are all the files that match your search terms. ")
    print("Sno. \t Name \t Label \t Path")
    print("-----------------------------------------------------")

    iteration = 0
    for tuple in answer:
        print(iteration, "\t", tuple[0], tuple[1], tuple[2])
        iteration += 1

    sno = int(input("Enter the Sno. of the file you want to open: "))
    return answer[sno][2]



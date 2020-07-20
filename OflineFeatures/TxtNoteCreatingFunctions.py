# This file contains the all the code and features for the first text file creator/editor
# This file contains the code needed to create a text file with the formatting currently needed for the labeling and index functions.

NEW_FILE_TOKEN = "new"
EDIT_FILE_TOKEN = "edit"


class EditorInstance:
    task = ""
    file_name = ""
    label = ""
    lines = None

    def __init__(self, mode):
        self.task = mode
        self.lines = list()
        # self.start()

    def start(self):
        if(self.task == NEW_FILE_TOKEN):
            self.newFile()
        elif(self.task == EDIT_FILE_TOKEN):
            self.editFile()

# ####### Method to create a new file and starting writing on it.
    def newFile(self):
        self.file_name = input("What do you want to be the name of your note? ")
        sure = input("Are you sure you want to proceed? Any files with the same name will be OVERRIDDEN...\n" +
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


# ####### Method to initiate the editing an existing file
    def editFile(self):
        try:
            self.file_name = input("What is the name of the file you want to open: ")
            file_handler = open(self.file_name, "r")
            self.lines = file_handler.readlines()
            file_handler.close()

            # This part of the code runs if there is in fact a file with the name the user gave
            print("File opened, here is a preview of what there is so far:\n----------------------------------------")
            for line in self.lines:
                print(str(self.lines.index(line)) + ": "+ line, end="")
            print("----------------------------------------")

            # Printing a list of all available commands
            self.printAvailableCommands()
            # Starting the editor runner.
            self.editorRunner()

        except():
            create_new_file = input("No such file exists, Do you want to create a new one? (reply \"yes\" or \"no\"): ")
            if(create_new_file.lower().startswith("yes")):
                self.newFile()
            else:
                quit_auth = input("Do you want to retry typing the name of the file correctly or quit the text editor?"
                                  + "(reply \"retry\" or \"quit\"): ").lower()
                if quit_auth.startswith("retry"): self.editFile()


# ######################################################## Commands common for both editing an existing file
    # #################################################### and creating a new file.

    def editorRunner(self):
        while True:
            current_line = input(str(len(self.lines) - 1) + ": ")

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
                return True, False
            else:
                print("operation cancelled, continue typing")
                return False, True
            print("----------------------------------------")
        # command to edit a particular line of the file
        if current_line == "^^^^":
            print("----------------------------------------")

            line_number = int(input("Enter the line number of the line you wish to change: "))
            if (line_number > len(lines) or line_number < 1):
                print("invalid line number, reissue command to try again.")
                print("----------------------------------------")
                return False, True

            replacement = input("Type the replacement text: ")
            lines[line_number + 1] = replacement
            print("done! Continue typing the next line.")
            print("----------------------------------------")
            return False, True
        # command to quit without saving
        if current_line == "**&&^":
            print("----------------------------------------")
            confirmation = input("Are you sure that you want to quit without saving?\n" +
                                 "Type \"y\" to confirm or any other key to cancel: ")
            if (confirmation.lower() == "y"):
                self.lines = list()
                return True, False
            else:
                print("operation cancelled, continue typing")
            print("----------------------------------------")

        # Printing available commands when asked
        if(current_line == "%%help"): self.printAvailableCommands()

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
        print("Here is a preview of your file:/n----------------------------------------")
        for line in self.lines:
            print(line)
        print("----------------------------------------")

        # save file tasks that have to be done when creating a new file.
        file_handler = open(self.file_name, "w")
        summative_string = ""
        for line in self.lines:
            summative_string += line + "\n"
            file_handler.write(summative_string)

        file_handler.close()
        print("----------------------------------------")
        print("Your file has been saved.")
        print("----------------------------------------")



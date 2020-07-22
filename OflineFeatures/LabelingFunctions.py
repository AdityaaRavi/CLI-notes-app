# Importing "os"-an inbuilt module that can be used to interact with the file system like creating and deleting folders
import os

print("The code here was run..................................")


class LabelInstance:
    current_dir = ""
    index = None

    def __init__(self):
        self.current_dir = os.getcwd()
        self.index = dict()
        # retriving previously stored indexes from the disk
        lines = open("AppData/index_storage.txt", "r").readlines()

        # storing data from the disk temporarly in the varaible "index"
        for line in lines:
            line.strip()
            data = line.split()
            # key = name, label |||| and value = date_of_creation, path
            self.index[data[0], data[1]] = (data[2], data[1] + "/" + data[0])
        # print(index)

    # method to move files to match their labels (pass -1 for current path if the file in in the home folder).
    def moveFiles(self, file_name, label, current_path):
        pass

    # method to add the details of a new file to the index
    def changeLabel(self, file_name, label, date):
        path_parameters = file_name.split("/")
        old_label = path_parameters[0]
        file_name = path_parameters[1]
        # find file in local database and remove old data
        self.index.pop(file_name, old_label)
        # change indexing data
        self.index[file_name, label] = (date, label + "/" + file_name)
        # call method to update the disk copy of indexing data
        self.updateDisk()
        # use "os" library to move the file.
        self.moveFiles(file_name, label, old_label)
        # Letting the user know its done!
        print("Label changed!")

    # method to add the details of a new file to the index
    def newFileSaved(self, file_name, label, date):
        self.index[file_name, label] = (date, label + "/" + file_name)
        self.moveFiles(file_name, label, -1)
        self.updateDisk(file_name, label)
        print("Added to index!")

    # Method to remove the details of a deleted note from the index
    def fileRemoved(self, file_name, label):
        self.index.pop(file_name, label)
        self.updateDisk()

    # #### Overloaded methods to help find each file from the index, each returns
    # #### all the valid results based on given parameters.

    # name of the file is the only parameter
    def searchFile(self, file_name):
        pass

    # All required parameters to find a file given
    def searchFile(self, file_name, label):
        pass

    # Name of the file and its date of the most recent modification are the only parameters
    def searchFile(self, file_name, date):
        pass

    # Date of creation is the only parameter
    def searchFile(self, date):
        pass

    # function that returns the date of most recent modification.
    def getDateOfModification(self, file_name, label):
        return self.index[file_name, label][0]

    # function to update the version of index stored on the disk --- call every time any change happens to labels
    # ##### Robustness more important than efficency !!
    def updateDisk(self):
        # creating a file handler to update on disk indez
        file_handler = open("AppData/index_storage.txt", "w")
        # Updating the on-disk index
        for file_name, label in self.index:
            file_handler.write(file_name + " " + label + " " + self.index[file_name, label][0])

        # closing the file_handler
        file_handler.close()






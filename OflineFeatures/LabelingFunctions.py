# Importing "os"-an inbuilt module that can be used to interact with the file system like creating and deleting folders
import os

print("The code here was run..................................")


class LabelInstance:
    current_dir = ""
    index = None

    def __init__(self):
        current_dir = os.getcwd()
        index = dict()
        # retriving previously stored indexes from the disk
        lines = open("AppData/index_storage.txt", "r").readlines()

        # storing data from the disk temporarly in the varaible "index"
        for line in lines:
            line.strip()
            data = line.split()
            # key = name, label |||| and value = date_of_creation, path
            index[data[0], data[1]] = (data[2], data[1] + "/" + data[0])
        # print(index)
        

    # method to move files to match their labels (pass -1 for current path if the file in in the home folder.
    def moveFiles(self, file_name, label, current_path):
        pass

    # method to add the details of a new file to the index
    def changeLabel(self, file_name, label, date):
        print("Label changed!")

    # method to add the details of a new file to the index
    def newFileSaved(self, file_name, label, date):
        print("Added to index!")

    # Method to remove the details of a deleted note from the index
    def fileRemoved(self, file_name, label):
        pass

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
        pass





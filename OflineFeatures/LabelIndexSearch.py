# Importing "os"-an inbuilt module that can be used to interact with the file system like creating and deleting folders
import os
import shutil
NOTES_DIRECTORY = "UserNotes"

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
            self.index[data[0], data[1]] = (data[2], NOTES_DIRECTORY + "/" + data[1] + "/" + data[0])
        # print(index)

    # method to move files to match their labels (pass -1 for current path if the file in in the home folder).
    # pass -1 to the "auto" parameter to denote that the file in question was openned automatically.
    def moveFiles(self, file_name, label, old_label, auto):
        old_path = file_name
        if(old_label is not -1 and auto is not -1):
            old_path = NOTES_DIRECTORY + "/" + old_label + "/" + file_name  ###########################
        elif(old_label is not -1):
            old_path = old_label + "/" + file_name

        if(not os.path.exists(NOTES_DIRECTORY + "/" + label)):
            # The current label is new and hence a new folder must be made
            os.mkdir(NOTES_DIRECTORY + "/" + label)

        # moving the file to the appropriate directory.
        shutil.move(old_path, NOTES_DIRECTORY + "/" + label + "/" + file_name)

    # method to add the details of a new file to the index
    # full_path, new_label, date
    def changeLabel(self, full_path, label, date, auto):
        path_parameters = full_path.split("/")
        old_label = ""
        file_name = ""
        if(len(path_parameters) > 1):
            old_label = str.join("/", path_parameters[:-1])
            file_name = path_parameters[-1]
        else:
            file_name = path_parameters[-1]
        # find file in local database and remove old data
        del self.index[file_name, path_parameters[-2]]
        # change indexing data
        self.index[file_name, label] = (date, NOTES_DIRECTORY + "/" + label + "/" + file_name)
        # use "os" library to move the file.
        self.moveFiles(file_name, label, old_label, auto)
        # call method to update the disk copy of indexing data
        self.updateDisk()
        # Letting the user know its done!
        print("Label updated!")

    # method to add the details of a new file to the index
    def newFileSaved(self, file_name, label, date):
        self.index[file_name, label] = (date, NOTES_DIRECTORY + "/" + label + "/" + file_name)
        self.moveFiles(file_name, label, -1, 0)
        self.updateDisk()
        print("Added to index!")

    # Method to remove the details of a deleted note from the index
    def fileRemoved(self, file_name, label):
        del self.index[file_name, label]
        self.updateDisk()

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
            file_handler.write(file_name + " " + label + " " + self.index[file_name, label][0] + "\n")

        # closing the file_handler
        file_handler.close()
        # print(self.index)

    # ------------------------------------------------------------------------------ Searching methods
    # #### Methods to help find each file from the index, each returns
    # #### all the valid results based on given parameters.

    # One stop shop method that can automatically call the appropriate search method and return their results based on
    # ### multiple optional arguements given by the user via the UI
    # ##### Vaild parmeters: file_name="name", label="label", date="date" ---> in any order or combination
    def searchFor(self, **kwargs):
        if("file_name" in kwargs and "label" in kwargs):
            return self.searchFileNameAndLabel(kwargs["file_name"], kwargs["label"])
        elif("file_name" in kwargs and "date" in kwargs):
            return self.searchFileNameAndDate(kwargs["file_name"], kwargs["date"])
        elif ("file_name" in kwargs):
            return self.searchFileNameOnly(kwargs["file_name"])
        elif ("date" in kwargs and "label" in kwargs):
            return self.searchFileLabelAndDate(kwargs['label'], kwargs['date'])
        elif("date" in kwargs):
            return self.searchFileDateOnly(kwargs["date"])
        elif("label" in kwargs):
            return self.searchFileLabelOnly(kwargs["label"])
        else:
            return self.getFullCopy()

    # All required parameters to find a file given
    def searchFileNameAndLabel(self, file_name, label):
        return self.index[file_name, label]

    # Name of the file and its date of the most recent modification are the only parameters
    def searchFileNameAndDate(self, file_name, date):
        matching_items = dict()
        for name, label in self.index:
            if (name == file_name and self.getDateOfModification(name, label) == date):
                matching_items[name, label] = self.index[name, label]
        return matching_items

    # name of the file is the only parameter
    def searchFileNameOnly(self, file_name):
        matching_items = dict()
        for name, label in self.index:
            if (name == file_name):
                matching_items[name, label] = self.index[name, label]
        return matching_items

    # Date and label are the only parameters
    def searchFileLabelAndDate(self, label, date):
        matching_items = dict()
        for name, i_label in self.index:
            if (i_label == label and self.getDateOfModification(name, i_label) == date):
                matching_items[name, i_label] = self.index[name, i_label]
        return matching_items

    # Label is the only parameter
    def searchFileLabelOnly(self, label):
        matching_items = dict()
        for name, i_label in self.index:
            if (i_label == label):
                matching_items[name, i_label] = self.index[name, i_label]
        return matching_items

    # Date of creation is the only parameter
    def searchFileDateOnly(self, date):
        matching_items = dict()
        for name, label in self.index:
            if (self.getDateOfModification(name, label) == date):
                matching_items[name, label] = self.index[name, label]
        return matching_items

    # Returns a dict() of all items that are currently indexed.
    def getFullCopy(self):
        matching_results = dict()
        for name, label in self.index:
            matching_results[name, label] = self.index[name, label]
        return matching_results

# ########## other functions


# Takes the given dictionary in index format and prints it out in a useable way
def printInIndexFormat(ref):
    print("-----------------------------------------------------")
    if(len(ref) == 0):
        print("NO results found! Please try again.")
    else:
        print("These are the items that match your search parameters: \n")
        print("\t%s\t%s\t%s\t%s\n" % ("Path", "Name of the file", "Label of the file", "Recent date of modification"))
        for name, label in ref:
            print("\t%s\t%s\t%s\t%s" % (ref[name, label][1], name, label, ref[name, label][0]))

    print("-----------------------------------------------------")



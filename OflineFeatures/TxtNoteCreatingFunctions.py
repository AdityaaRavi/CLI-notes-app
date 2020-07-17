# This file contains the all the code and features for the first text file creator/editor
# This file contains the code needed to create a text file with the formatting currently-
# needed for the labeling and index functions.

NEW_FILE_TOKEN = "new"
EDIT_FILE_TOKEN = "edit"

class EditorInstance:
    task = ""

    def __init__(self, mode):
        self.task = mode
        # self.start()

    def start(self):
        if(self.task == NEW_FILE_TOKEN):
            pass
        elif(self.task == EDIT_FILE_TOKEN):
            pass




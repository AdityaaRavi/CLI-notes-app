"""
The purpose of this code is to create a way for the user to purge all user data that this system has control
over to help him/her start afreah.
"""

from OflineFeatures import LabelIndexSearch as labelRef
from datetime import date

def resetProgram(labeler, **param):
    if("move" in param and param["move"]):
        ref = labeler.getIndexCopy()
        for name, label in ref:
            labeler.changeLabel(labelRef.NOTES_DIRECTORY + "/" + label + "/" + name,
                                "archive/" + label, date.today().strftime("%m.%d.%Y"), "reset")
        clearIndex(labeler)
        print("Indexes removed, data archived at UserNotes/archive/<label-name>.")

    elif("all" in param and param["all"]):
        print("Removing everything, I may not remember you, but I am still the same good program you loved!")
        deleteFile(labeler)
        print("Done!")

    elif("index" in param and param["index"]):
        print("-----------------")
        print("Removing all indexes.")
        print("-----------------")
        clearIndex(labeler)
        print("done")
    else:
        print("What do you want to remove? just the index? everything? want us to archive your files and move"
              + " them to a different folder?")

# method to only clear the indexes
def clearIndex(labeler):
    ref = labeler.getIndexCopy()
    for name, label in ref: labeler.fileRemoved(name, label, False)

# method to delete all files along with its index.
def deleteFile(labeler):
    ref = labeler.getIndexCopy()
    for name, label in ref: labeler.fileRemoved(name, label, True)



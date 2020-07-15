

## **LANwide-notes-app-serverside**
This repo contains the server-side code that organizes all the notes sent to it by the GUI clients based its type, 
user-given label, etc and indexes it for use by the searching functions in the GUI app. 

#### **Proof of concept (POC) stage overview**:
The proof of concept stage of this app will be split into multiple parts:
+ The first stage will deal with the offline sever tasks such as indexing and search features
+ The second stage will deal getting the program to keep running 24x7 and listening for data requests from clients
+ The third and final stage will test the feasibility of using android studio to create an app that will handle the client side functions need for this app.

**Proof of concept stage 1 - offline server tasks:** (Planned as of july 14, 2020 at 3 pm) 
+ Creating a temporary GUI-less interface to test all the processing tasks that the server will have to take care of. (Done as of July 14, 2020 @ 9:37 pm)
+ Indexing each note using a TBD method to help with finding a particular file.
+ Creating a searching class/function that takes in a search term and returns a dictionary, where each of the keys are the 
names of the files and each value is a list with all the line numbers where the given search term is found. 
(The method of returning data from the search feature may be updated later on)

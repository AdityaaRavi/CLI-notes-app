## CLI Notes App

A Command Line Interface based Notes app with support for Labeling, indexing, and searching.

### Usage instructions
Open your command line and type:

Navigate to the folder where you want to store your copy of this program and the notes you make with it, then:

1. To download the program, run this line regardless of your Operating System.
```shell
git clone https://github.com/AdityaaRavi/CLI-notes-app.git
```
2. Then, go into the directory where the file `CLI.py` is stored:
```shell
cd CLI-notes-app
```
3. Then to run the program,  
	- For UNIX based systems (i.e MacOS and Linux)
	```shell
	python3 CLI.py
	```
	- For Windows Computers
	```shell
	py CLI.py
	```
4. Use the commands printed out when you first open the program to use the respective features.

## Available commands
- `search` - Use the search feature to search, open, and edit an existing file created using this program.
- `start_txt_editor` - Create a new file or edit an existing file.
- `label` - Change the label of an existing file.
- `open` - Open the file at the given path (if it exists). Use this command to index a file you created with some other text editor.
- `reset` - (*Danger zone*) Remove or archive the file index (Needed by this program for its searching and labeling functions) and/or the user's notes.    
- `quit` or `exit` - Quit the program. 

## File Structure
- `AppData` - Directory to store all the information needed by the program to run properly, as of now, this folder only contains the persitent copy of the index.
- `UserNotes` - Directory that contains all files created and indexed by the user using this program. Each of the sub-directories hold all the notes classified under the respective label.
- `CLI.py` - The main script with the Command Line Interface needed to use this program.
- `OflineFeatures` - Contains all the code for each of the features of this program classified into multiple files.

## Screenshots
### Home screen
![image](https://user-images.githubusercontent.com/43429374/112095250-681ccc00-8b59-11eb-8e9c-c64e4ed83229.png)

### Search feature
![image](https://user-images.githubusercontent.com/43429374/112095425-b500a280-8b59-11eb-9320-2a187f0a8539.png)

### Using the in-built text editor
note: changing the line at index 1 is enough to change the label of the file.
![image](https://user-images.githubusercontent.com/43429374/112095929-9f3fad00-8b5a-11eb-8af3-017160d82cbd.png)

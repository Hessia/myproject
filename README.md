# Bookify

# GitHub Repository
The source code for this project is available on GitHub: https://github.com/Hessia/myproject

## Identification
- **Name:** Elif Eylül Ak
- **P-number:** P452642
- **Course code:** IY499 Introduction to Programming

## Declaration of Own Work
I confirm that this assignment is my own work.
Where I have referred to academic sources, I have provided in-text citations and included the sources in the final reference list.


## Introduction
Bookify is a user-friendly application designed for book lovers to manage their reading habits. Users can create playlists (like Spotify but for books), add books to those playlists with optional comments, and view their collections.

The project was developed as part of the IY499 Introduction to Programming course and serves as an example of basic Python GUI programming, file handling, and modular code design.


## Installation
Clone the repository: git clone https://github.com/Hessia/myproject.git
cd myproject

Run the project: No external libraries are required; Python's standard library is sufficient. Just make sure you have Python 3 installed.


## How to Use and Run the Application

- Launch the app: open the terminal and run "myproject_main.py"

- Register/Login: Users can register with a username and password and log in to access their playlists.

- Create Playlists: Use the "Create Playlist" button to create a new playlist.

- Add Books to Playlists: Add books to an existing playlist with optional comments.

- View Playlists: View all playlists and their associated books.


## Application Elements

- Registration/Login: Secure and user-friendly system to log in and access personal playlists.

- Playlist Management: Users can create multiple playlists and add books to each playlist.

- Comments: Option to add a comment for each book to personalize the playlist.

- File-Based Storage: Data is stored persistently in playlists.txt and users.txt.


## Libraries Used

- Tkinter: For creating the graphical user interface (GUI).

- messagebox and simpledialog: For interactive user messages and input prompts.

- os.path: For checking and managing file operations.


## Project Structure

The project is modular and consists of:

- myproject_main.py: The main entry point for the application, managing the GUI and user interactions.

- myproject_helper.py: Contains all helper functions for playlist management, including creating playlists, adding books, and viewing playlists.

- myproject_user.py: Handles user registration and login functionalities.

- playlists.txt: File to store user playlists and books.

- users.txt: File to store registered users' data.

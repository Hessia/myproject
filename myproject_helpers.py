from tkinter import messagebox


def create_playlist(username, playlist_name, file_path="playlists.txt"):
    """Create a new playlist for the user."""
    with open(file_path, "a") as file:
        file.write(f"{username}:{playlist_name}:\n")
    messagebox.showinfo("Success", f"Playlist '{playlist_name}' created succesfully!")
    pass

def add_book_to_playlist(username, playlist_name, book, comment="", file_path="playlists.txt"):
    """Add a book with an optional comment to a user's playlist."""
    updated_lines = []
    found = False

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    for line in lines:
        if line.startswith(f"{username}:{playlist_name}:"):
            found = True
            line = line.strip() + f"{book}|{comment},\n"
        updated_lines.append(line)

    if not found:
        messagebox.showerror("Error", "Playlist not found. Please create it first.")
        return
    with open(file_path, "w") as file:
        file.writelines(updated_lines)
    messagebox.showinfo("Success", f"Book '{book}' added to playlist '{playlist_name}'.")
    pass

def view_playlists(username, file_path="playlists.txt"):
    """Display all playlists and books for the given user."""
    playlists = {}

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    for line in lines:
        if line.startswith(username):
            _, playlist_name, books = line.strip().partition(":")[2].partition(":")
            if playlist_name not in playlists:
                playlists[playlist_name.strip()] = []
            if books:
                for book in books.split(","):
                    if book.strip():
                        book_name, _, comment = book.partition("|")
                        playlists[playlist_name.strip()].append((book_name.strip(), comment.strip()))


    if not playlists:
        messagebox.showinfo("Playlists", "No playlists found for this user.")
        return
    
    playlist_display = ""
    for playlist, books in playlists.items():
        playlist_display += f"Playlist: {playlist}\n"
        for book, comment in books:
            playlist_display += f"  Book: {book} (Comment: {comment if comment else 'No comment'})\n"
        playlist_display += "\n"

    messagebox.showinfo("Playlists", playlist_display.strip())
    pass


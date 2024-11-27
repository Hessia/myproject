import tkinter as tk
from tkinter import messagebox
from myproject_user import register_user, login_user

def handle_register():
    username = entry_username.get()
    password = entry_password.get()
    if username and password:
        register_user(username, password)
        messagebox.showinfo("Success", "User registered successfully!")
    else:
        messagebox.showerror("Error", "Please fill in both fields.")

def handle_login():
    username = entry_username.get()
    password = entry_password.get()
    if not username or not password:
        messagebox.showerror("Error", "Please fill in both fields.")
        return

    from myproject_user import hash_password
    hashed_password = hash_password(password)

    try:
        with open ("users.txt", "r") as file:
            users = file.readlines()
            for user in users:
                if "," in user:
                    stored_username, stored_password = user.strip().split(",", 1)
                    stored_username = stored_username.strip()
                    stored_password = stored_password.strip()
                    if username == stored_username and hashed_password == stored_password:
                        messagebox.showinfo("Success", "Login successful!")
                        return

            messagebox.showerror("Error", "Invalid username or password.")
    except FileNotFoundError:
        messagebox.showerror("Error", "No registered user found.")


def handle_exit():
    root.destroy()

def handle_enter(event):
    handle_register()
    handle_login()

root = tk.Tk()
root.title("Library App")
window_width = 800
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))

root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
root.configure(bg="#5E8BF2")

frame = tk.Frame(root, padx=20, pady=20, bg="#5E8BF2")
frame.pack()

label_title = tk.Label(frame, text="Welcome to the Library App", font=("Arial", 16), bg="#5E8BF2")
label_title.pack(pady=10)

label_username = tk.Label(frame, text="Username: ", bg="#5E8BF2")
label_username.pack()
entry_username = tk.Entry(frame)
entry_username.pack(pady=5)

label_password = tk.Label(frame, text="Password: ", bg="#5E8BF2")
label_password.pack()
entry_password = tk.Entry(frame, show="*")
entry_password.pack(pady=5)

button_register = tk.Button(frame, text="Register", command=handle_register, bg="#5E8BF2", takefocus=False, relief="flat", highlightthickness=0, bd=0)
button_register.pack(pady=5)

button_login = tk.Button(frame, text="Login", command=handle_login, bg="#5E8BF2", takefocus=False, relief="flat", highlightthickness=0, bd=0)
button_login.pack(pady=5)

button_exit = tk.Button(frame, text="Exit", command=handle_exit, bg="#5E8BF2", takefocus=False, relief="flat", highlightthickness=0, bd=0)
button_exit.pack(pady=5)

root.bind('<Return>', handle_enter)

root.mainloop()

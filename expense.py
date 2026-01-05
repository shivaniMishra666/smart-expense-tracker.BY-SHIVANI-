import tkinter as tk
from tkinter import messagebox
import datetime
import os

USERS_FILE = "users.txt"
EXPENSE_FILE = "expenses_gui.txt"

# ---------- LOGIN FUNCTIONS ----------
def register():
    user = username_entry.get()
    pwd = password_entry.get()

    if user == "" or pwd == "":
        messagebox.showerror("Error", "All fields required")
        return

    with open(USERS_FILE, "a") as f:
        f.write(f"{user},{pwd}\n")

    messagebox.showinfo("Success", "Registration Successful ✅")


def login():
    user = username_entry.get()
    pwd = password_entry.get()

    if not os.path.exists(USERS_FILE):
        messagebox.showerror("Error", "No users found. Register first.")
        return

    with open(USERS_FILE, "r") as f:
        for line in f:
            u, p = line.strip().split(",")
            if u == user and p == pwd:
                messagebox.showinfo("Login", "Login Successful 🎉")
                login_window.destroy()
                expense_app()
                return

    messagebox.showerror("Error", "Invalid Username or Password")


# ---------- EXPENSE TRACKER ----------
def expense_app():
    def add_expense():
        amt = amount_entry.get()
        cat = category_entry.get()

        if amt == "" or cat == "":
            messagebox.showerror("Error", "Fill all fields")
            return

        date = datetime.date.today().strftime("%d-%m-%Y")

        with open(EXPENSE_FILE, "a") as f:
            f.write(f"{date},{cat},{amt}\n")

        messagebox.showinfo("Success", "Expense Added ✅")
        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)

    def show_total():
        total = 0
        try:
            with open(EXPENSE_FILE, "r") as f:
                for line in f:
                    total += int(line.strip().split(",")[2])
        except:
            pass
        messagebox.showinfo("Total", f"Total Expense: ₹{total}")

    app = tk.Tk()
    app.title("Smart Expense Tracker")
    app.geometry("350x300")

    tk.Label(app, text="Expense Tracker", font=("Arial", 16, "bold")).pack(pady=10)

    tk.Label(app, text="Amount").pack()
    amount_entry = tk.Entry(app)
    amount_entry.pack()

    tk.Label(app, text="Category").pack()
    category_entry = tk.Entry(app)
    category_entry.pack()

    tk.Button(app, text="Add Expense", command=add_expense, bg="green", fg="white").pack(pady=10)
    tk.Button(app, text="Show Total", command=show_total, bg="blue", fg="white").pack()

    app.mainloop()


# ---------- LOGIN WINDOW ----------
login_window = tk.Tk()
login_window.title("Login System")
login_window.geometry("300x250")

tk.Label(login_window, text="Login System", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(login_window, text="Username").pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

tk.Label(login_window, text="Password").pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

tk.Button(login_window, text="Login", command=login, bg="blue", fg="white").pack(pady=5)
tk.Button(login_window, text="Register", command=register, bg="green", fg="white").pack()

login_window.mainloop()
# `import tkinter as tk` is importing the `tkinter` module and aliasing it as `tk`. This allows you to
# refer to the `tkinter` module using the shorter alias `tk` throughout your code. This is a common
# practice to make the code more concise and readable.
import tkinter as tk
from tkinter import messagebox

def submit():
    """
    The `submit` function retrieves user input for name, email, and age.
    """
    name = entry_name.get()
    email = entry_email.get()
    age = entry_age.get()
    

    # This block of code is performing basic validation on the user input fields for name, email, and
    # age. Here's what each part does:
    if not name:
        messagebox.showwarning("Warning", "Please enter your name")
        return
    if not email:
        messagebox.showwarning("Warning", "Please enter your email")
        return
    if not age:
        messagebox.showwarning("Warning", "Please enter your age")
        return
    
    
    # The line `messagebox.showinfo("Information", f"Name: {name}\nEmail: {email}\nAge: {age}")` is
    # displaying a message box with the title "Information" and the content showing the submitted
    # information entered by the user. The information displayed includes the user's name, email, and
    # age, which are retrieved from the input fields in the GUI form. The `f"..."` syntax is used for
    # string formatting in Python, allowing variables like `name`, `email`, and `age` to be inserted
    # into the message string.
    messagebox.showinfo("Information", f"Name: {name}\nEmail: {email}\nAge: {age}")    
    

# `root = tk.Tk()` creates the main window of the GUI application using the `Tk` class from the
# `tkinter` module. This window is commonly referred to as the root window.
root = tk.Tk()
root.title("Registration Form")

# The code snippet you provided is creating labels for the input fields in a registration form GUI.
# Here's what each part of the code is doing:

label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

label_age = tk.Label(root, text="Age:")
label_age.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

# These lines of code are creating entry fields (text input fields) for the user to enter their name,
# email, and age in the registration form GUI. Here's a breakdown of what each part of the code is
# doing:
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=5)

entry_email = tk.Entry(root, width=30)
entry_email.grid(row=1, column=1, padx=10, pady=5)

entry_age = tk.Entry(root, width=30)
entry_age.grid(row=2, column=1, padx=10, pady=5)

# The code snippet you provided is creating a button in the GUI registration form. Here's a breakdown
# of what each part of the code is doing:
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()
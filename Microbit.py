import os
from tkinter import *
from tkinter import simpledialog, messagebox

def open_project():
    # Ask for project name
    project_name = simpledialog.askstring("Project Name", "Enter your project name:")

    if project_name:
        # Optional: rename/copy HEX file with project name
        new_file = f"{project_name}.hex"

        try:
            # Copy template to new file
            with open("START_ROBOT.hex", "rb") as src:
                with open(new_file, "wb") as dst:
                    dst.write(src.read())

            # Open the new project
            os.startfile(new_file)

        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showinfo("Cancelled", "No project name entered")

# UI
root = Tk()
root.title("Robot Lab")

btn = Button(root, text="Start Robot Project", command=open_project, height=2, width=25)
btn.pack(pady=30)

root.mainloop()

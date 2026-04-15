import os
import webbrowser
from tkinter import *
from tkinter import simpledialog, messagebox

def open_project():
    project_name = simpledialog.askstring("Project Name", "Enter your project name:")

    if project_name:
        new_file = f"{project_name}.hex"

        try:
            # Copy template HEX (with extensions)
            with open("START_ROBOT.hex", "rb") as src:
                with open(new_file, "wb") as dst:
                    dst.write(src.read())

            # Open MakeCode in browser
            webbrowser.open("https://makecode.microbit.org")

            messagebox.showinfo(
                "Project Ready",
                f"{new_file} created!\n\nNow:\nImport → Import File → Select your file\n\nAll extensions will load automatically ✅"
            )

        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showinfo("Cancelled", "No project name entered")

# UI
root = Tk()
root.title("Robot Lab")

btn = Button(root, text="Start Robot Project", command=open_project, height=2, width=30)
btn.pack(pady=30)

root.mainloop()

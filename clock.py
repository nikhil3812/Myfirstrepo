import tkinter as tk
import time

def update_clock():
    current_time = time.strftime('%H:%M:%S')
    label.config(text=current_time)
    label.after(1000, update_clock)  # update every 1 second

# Create main window
root = tk.Tk()
root.title("Digital Clock")

# Configure label style
label = tk.Label(root, font=('Arial', 60), background='black', foreground='lime')
label.pack(anchor='center')

# Start the clock
update_clock()

# Run the GUI event loop
root.mainloop()

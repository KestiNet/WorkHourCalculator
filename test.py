import tkinter as tk

def submit():
    value1 = entry1.get()
    value2 = entry2.get()
    result_label.config(text=f"Text 1: {value1}\nText 2: {value2}")

# Create the main window
root = tk.Tk()
root.title("Side-by-Side Text Boxes")

# Create labels and text entry widgets
label1 = tk.Label(root, text="Text 1:")
entry1 = tk.Entry(root)
label2 = tk.Label(root, text="Text 2:")
entry2 = tk.Entry(root)

# Create a button to submit the text
submit_button = tk.Button(root, text="Submit", command=submit)

# Create a label to display the result
result_label = tk.Label(root, text="Result will be shown here")

# Use the grid geometry manager to arrange the widgets
label1.grid(row=0, column=0, sticky='e')
entry1.grid(row=0, column=1)
label2.grid(row=0, column=2, sticky='e')
entry2.grid(row=0, column=3)
submit_button.grid(row=1, column=0, columnspan=4)
result_label.grid(row=2, column=0, columnspan=4)

# Start the main event loop
root.mainloop()

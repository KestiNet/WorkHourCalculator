import tkinter as tk


#
# Create the main tkinter window
root = tk.Tk()
root.title("Work Time Calculator")
root.geometry("400x500")

# Create Labels
label1 = tk.Label(root, text="Monday:")
label2 = tk.Label(root, text="Tuesday:")
label3 = tk.Label(root, text="Wednesday:")
label4 = tk.Label(root, text="Thursday:")
label5 = tk.Label(root, text="Friday:")
label6 = tk.Label(root, text="test")
#label6 = tk.Label(root, text="Total:")
#label7 = tk.Label(root, text="TTL:")


# Create Entry widgets (textboxes)
textbox1 = tk.Entry(root)
textbox2 = tk.Entry(root)
textbox3 = tk.Entry(root)
textbox4 = tk.Entry(root)
textbox5 = tk.Entry(root)
textbox6 = tk.Entry(root)
textbox7 = tk.Entry(root)
textbox8 = tk.Entry(root)
textbox9 = tk.Entry(root)
textbox10 = tk.Entry(root)
textbox11 = tk.Entry(root)
textbox12 = tk.Entry(root)


#calculate_button = tk.Button(root, text="Calculate Total", command=workhour_calculator_total)
result = tk.Label(root, text= "Total: 0")
# Use the grid method to position the Labels and Entry widgets
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0)
label4.grid(row=3, column=0)
label5.grid(row=4, column=0)
label6.grid(row=0, column=1)
#label6.grid(row=5, column=0)
#label7.grid(row=5, column=0)

textbox1.grid(row=0, column=1)
textbox2.grid(row=1, column=1)
textbox3.grid(row=2, column=1)
textbox4.grid(row=3, column=1)
textbox5.grid(row=4, column=1)
textbox6.grid(row=0, column=1)
textbox7.grid(row=0, column=2)
textbox8.grid(row=1, column=2)
textbox9.grid(row=2, column=2)
textbox10.grid(row=3, column=2)
textbox11.grid(row=4, column=2)
textbox12.grid(row=0, column=2)
#textbox6.grid(row=5, column=1)
result.grid(row=5, column=0)

#calculate_button.grid(row=6, column=0, columnspan=2)
# Start the tkinter main loop
root.mainloop()

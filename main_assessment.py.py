import tkinter as tk

class HireStore:
    def __init__(self, master):
        self.master = master
        master.title("Julie's Party Hire Store")
        master.geometry("500x400")  # Set the window size to 500x400 pixels

        # create a frame for the input section
        self.frame_input = tk.Frame(master)
        self.frame_input.pack(pady=10)
        
        # create labels and entries for input
        self.label_name = tk.Label(self.frame_input, text="Full Name:")
        self.label_name.grid(row=0, column=0, sticky="w")
        self.entry_name = tk.Entry(self.frame_input)
        self.entry_name.grid(row=0, column=1)

        self.label_receipt = tk.Label(self.frame_input, text="Receipt Number:")
        self.label_receipt.grid(row=1, column=0, sticky="w")
        self.entry_receipt = tk.Entry(self.frame_input)
        self.entry_receipt.grid(row=1, column=1)

        self.label_item = tk.Label(self.frame_input, text="Item Hired:")
        self.label_item.grid(row=2, column=0, sticky="w")
        self.entry_item = tk.Entry(self.frame_input)
        self.entry_item.grid(row=2, column=1)

        self.label_quantity = tk.Label(self.frame_input, text="Quantity Hired:")
        self.label_quantity.grid(row=3, column=0, sticky="w")
        self.entry_quantity = tk.Entry(self.frame_input)
        self.entry_quantity.grid(row=3, column=1)

        # create a button to add the hire details to the list
        self.button_add = tk.Button(master, text="Add Hire", command=self.add_hire)
        self.button_add.pack(pady=10)

        # create a listbox to display the current hires
        self.listbox_hires = tk.Listbox(master)
        self.listbox_hires.pack(fill=tk.BOTH, expand=True, padx=10)

        # create a button to remove the selected hire from the list
        self.button_remove = tk.Button(master, text="Remove Hire", command=self.remove_hire)
        self.button_remove.pack(pady=10)

        # create a button to append another hire to the list
        self.button_append = tk.Button(master, text="Append Hire", command=self.append_hire)
        self.button_append.pack(pady=10)

        # create a dictionary to store the hire details
        self.hire_dict = {}

    def add_hire(self):
        # get the hire details from the entries
        name = self.entry_name.get()
        receipt = self.entry_receipt.get()
        item = self.entry_item.get()
        quantity = int(self.entry_quantity.get())

        # add the hire details to the dictionary
        self.hire_dict[receipt] = [name, item, quantity]

        # add the hire details to the listbox
        hire_string = f"{name} - Receipt: {receipt} - Item: {item} - Quantity: {quantity}"
        self.listbox_hires.insert(tk.END, hire_string)

        # clear the entry fields
        self.entry_name.delete(0, tk.END)
        self.entry_receipt.delete(0, tk.END)
        self.entry_item.delete(0, tk.END)
        self.entry_quantity.delete(0, tk.END)

    def remove_hire(self):
        # get the selected hire from the listbox
        selection = self.listbox_hires.curselection()
        if selection:
            hire_string = self.listbox_hires.get(selection[0])
            receipt = hire_string.split(" - ")[1].split(": ")[1]

            # remove the hire details from the dictionary
            del self.hire_dict[receipt]

            # remove the hire details from the listbox
            self.listbox_hires.delete(selection[0])

    def append_hire(self):
        # get the last hire details from the dictionary
        last_receipt = max(self.hire_dict.keys())
        last_name, last_item, last_quantity = self.hire_dict[last_receipt]

        # generate a new receipt number by adding one to the last receipt
        new_receipt = str(int(last_receipt) + 1)

        # append the same hire details with the new receipt to the dictionary
        self.hire_dict[new_receipt] = [last_name, last_item, last_quantity]

        # append the same hire details with the new receipt to the listbox
        hire_string = f"{last_name} - Receipt: {new_receipt} - Item: {last_item} - Quantity: {last_quantity}"
        self.listbox_hires.insert(tk.END, hire_string)
    
root = tk.Tk()
my_app = HireStore(root)
root.mainloop()

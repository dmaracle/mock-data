import csv
from tkinter import *
from generate_data import generate_array

class Frontend:
    def __init__(self):
        root = Tk()
        root.geometry("500x500")
        root.configure(pady=10, padx=10)
        

        # Label Widgets
        csv_label = Label(root, text="Rows to Generate: ")
        csv_label.grid(row=0, column=0, pady=5, sticky=E)
        clients_label = Label(root, text="Database Name: ")
        clients_label.grid(row=2, column=0, pady=5, sticky=E)
        self.hidden_label = Label(root, text="")
        self.hidden_label.grid(row=4, column=0, columnspan=2)
        
        # Entry Widgets
        self.rows_generated = Entry(root, text="", width=20)
        self.rows_generated.grid(row=0, column=1, sticky=W)
        self.clients_entry = Entry(root, text="", width=20)
        self.clients_entry.grid(row=2, column=1, sticky=W)
        
        # Button Widget
        generate_data_btn = Button(root, width=15, text="Generate Data", command=self.generate_data)
        generate_data_btn.grid(row=1, column=0, columnspan=2, pady=5)
        create_database_btn = Button(root, width=15, text="Create Database", command=self.save_as_csv)
        create_database_btn.grid(row=3, column=0, pady=5)
        save_csv_btn = Button(root, width=15, text="Save as CSV", command=self.save_as_csv)
        save_csv_btn.grid(row=3, column=1)
        
        
        # Listbox Widget
        self.listbox = Listbox(root, width=60, height=20)
        self.listbox.grid(row=5, column=0, columnspan=2, pady=10)
        root.mainloop()
    
    def generate_data(self):
        self.listbox.delete(0, END)
        self.data_array = generate_array(int(self.rows_generated.get()))
        for x in range(len(self.data_array)):
            self.listbox.insert(END, self.data_array[x])
    
    def save_as_csv(self):
        header_list = ['Name', 'Address', 'Phone', 'City', 'Email', 'Client Type', 'Client Acquisition',
                   'Client Occurence', 'Windows Price', 'Pressure Wash Price', 'Handywork Price',
                   'Expenses', 'Profit']
        with open(f"{self.csv_entry.get()}.csv","w",newline='') as my_csv:
            csvWriter = csv.writer(my_csv,delimiter=',')
            csvWriter.writerow(header_list)
            csvWriter.writerows(self.data_array)
        self.hidden_label.config(text=f"CSV File '{self.csv_entry.get()}.csv' created!", font=('Helvetica bold', 12))
        
Frontend()    
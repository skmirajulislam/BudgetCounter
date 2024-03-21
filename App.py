import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
from datetime import datetime


class TransactionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Transaction Manager")
        self.master.geometry("800x600")

        self.tab_control = ttk.Notebook(master)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab1, text='Daily Transactions')
        self.tab_control.add(self.tab2, text='Monthly Income')

        self.tab_control.pack(expand=1, fill='both')

        self.create_daily_transactions_tab()
        self.create_monthly_income_tab()

    def create_daily_transactions_tab(self):
        self.daily_tree = ttk.Treeview(self.tab1)
        self.daily_tree['columns'] = ('Product Name', 'Price', 'Family Member', 'Date', 'Time')
        self.daily_tree.heading('#0', text='ID')
        self.daily_tree.column("#0", minwidth=0, width=50, stretch=tk.NO)
        for col in self.daily_tree['columns']:
            self.daily_tree.heading(col, text=col)

        self.daily_tree.pack(expand=True, fill='both')

        # Add scrollbar
        scroll_y = ttk.Scrollbar(self.tab1, orient='vertical', command=self.daily_tree.yview)
        scroll_y.pack(side='right', fill='y')
        self.daily_tree.configure(yscrollcommand=scroll_y.set)

        # Add input fields
        input_frame = tk.Frame(self.tab1)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Product Name:").grid(row=0, column=0, padx=5, pady=5)
        self.product_name_entry = tk.Entry(input_frame)
        self.product_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Price:").grid(row=1, column=0, padx=5, pady=5)
        self.price_entry = tk.Entry(input_frame)
        self.price_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Family Member:").grid(row=2, column=0, padx=5, pady=5)
        self.family_member_entry = tk.Entry(input_frame)
        self.family_member_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(input_frame, text="Add Transaction", command=self.add_daily_transaction).grid(row=3, columnspan=2, pady=10)

        # Add download button
        download_button = tk.Button(input_frame, text="Download Daily Transactions", command=self.download_daily_transactions)
        download_button.grid(row=4, columnspan=2, pady=10)

    def create_monthly_income_tab(self):
        self.monthly_tree = ttk.Treeview(self.tab2)
        self.monthly_tree['columns'] = ('Paid Person', 'Amount Paid', 'Amount Not Paid', 'Date', 'Location')
        self.monthly_tree.heading('#0', text='ID')
        self.monthly_tree.column("#0", minwidth=0, width=50, stretch=tk.NO)
        for col in self.monthly_tree['columns']:
            self.monthly_tree.heading(col, text=col)

        self.monthly_tree.pack(expand=True, fill='both')

        # Add scrollbar
        scroll_y = ttk.Scrollbar(self.tab2, orient='vertical', command=self.monthly_tree.yview)
        scroll_y.pack(side='right', fill='y')
        self.monthly_tree.configure(yscrollcommand=scroll_y.set)

        # Add input fields
        input_frame = tk.Frame(self.tab2)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Paid Person:").grid(row=0, column=0, padx=5, pady=5)
        self.paid_person_entry = tk.Entry(input_frame)
        self.paid_person_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Amount Paid:").grid(row=1, column=0, padx=5, pady=5)
        self.amount_paid_entry = tk.Entry(input_frame)
        self.amount_paid_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Amount Not Paid:").grid(row=2, column=0, padx=5, pady=5)
        self.amount_not_paid_entry = tk.Entry(input_frame)
        self.amount_not_paid_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Date:").grid(row=3, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(input_frame)
        self.date_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Location:").grid(row=4, column=0, padx=5, pady=5)
        self.location_entry = tk.Entry(input_frame)
        self.location_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Button(input_frame, text="Add Income", command=self.add_monthly_income).grid(row=5, columnspan=2, pady=10)

        # Add download button
        download_button = tk.Button(input_frame, text="Download Monthly Income", command=self.download_monthly_income)
        download_button.grid(row=6, columnspan=2, pady=10)

    def add_daily_transaction(self):
        product_name = self.product_name_entry.get()
        price = self.price_entry.get()
        family_member = self.family_member_entry.get()
        date = datetime.now().strftime('%Y-%m-%d')
        time = datetime.now().strftime('%H:%M:%S')

        # Calculate the new ID
        new_id = len(self.daily_tree.get_children()) + 1

        self.daily_tree.insert('', 'end', text=str(new_id), values=(product_name, price, family_member, date, time))

        # Clear input fields
        self.product_name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.family_member_entry.delete(0, tk.END)

    def add_monthly_income(self):
        paid_person = self.paid_person_entry.get()
        amount_paid = self.amount_paid_entry.get()
        amount_not_paid = self.amount_not_paid_entry.get()
        date = self.date_entry.get()
        location = self.location_entry.get()

        # Calculate the new ID
        new_id = len(self.monthly_tree.get_children()) + 1

        self.monthly_tree.insert('', 'end', text=str(new_id), values=(paid_person, amount_paid, amount_not_paid, date, location))

        # Clear input fields
        self.paid_person_entry.delete(0, tk.END)
        self.amount_paid_entry.delete(0, tk.END)
        self.amount_not_paid_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)


    def download_daily_transactions(self):
        filename = "daily_transactions.xlsx"
        data = []
        for child in self.daily_tree.get_children():
                values = self.daily_tree.item(child, 'values')
                data.append(values)
        df = pd.DataFrame(data, columns=['Product Name', 'Price', 'Family Member', 'Date', 'Time'])
        df.to_excel(filename, index=False)
        messagebox.showinfo("Success", "Daily transactions downloaded successfully!")

    def download_monthly_income(self):
        filename = "monthly_income.xlsx"
        data = []
        for child in self.monthly_tree.get_children():
            values = self.monthly_tree.item(child, 'values')
            data.append(values)
        df = pd.DataFrame(data, columns=['Paid Person', 'Amount Paid', 'Amount Not Paid', 'Date', 'Location'])
        df.to_excel(filename, index=False)
        messagebox.showinfo("Success", "Monthly income downloaded successfully!")


def main():
    root = tk.Tk()
    app = TransactionApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

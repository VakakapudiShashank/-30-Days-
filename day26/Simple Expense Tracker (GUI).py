# Day 26 — Tkinter Expense Tracker (GUI)
# Built-in Tkinter (no extra install)

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
import csv
import os

CSV_FILE = "expenses.csv"

class ExpenseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Expense Tracker")
        self.total = 0.0

        # Form
        frm = tk.Frame(root, padx=10, pady=10)
        frm.pack(fill="x")

        tk.Label(frm, text="Date:").grid(row=0, column=0, sticky="e")
        tk.Label(frm, text="Description:").grid(row=1, column=0, sticky="e")
        tk.Label(frm, text="Category:").grid(row=2, column=0, sticky="e")
        tk.Label(frm, text="Amount:").grid(row=3, column=0, sticky="e")

        self.var_date = tk.StringVar(value=str(date.today()))
        self.var_desc = tk.StringVar()
        self.var_cat = tk.StringVar()
        self.var_amt = tk.StringVar()

        tk.Entry(frm, textvariable=self.var_date).grid(row=0, column=1)
        tk.Entry(frm, textvariable=self.var_desc).grid(row=1, column=1)
        tk.Entry(frm, textvariable=self.var_cat).grid(row=2, column=1)
        tk.Entry(frm, textvariable=self.var_amt).grid(row=3, column=1)

        tk.Button(frm, text="Add Expense", command=self.add_expense).grid(row=4, column=0, columnspan=2, pady=6)

        # Table
        self.tree = ttk.Treeview(root, columns=("date", "desc", "cat", "amt"), show="headings", height=8)
        for col, txt, w in [("date","Date",100), ("desc","Description",180), ("cat","Category",120), ("amt","Amount",80)]:
            self.tree.heading(col, text=txt)
            self.tree.column(col, width=w, anchor="center")
        self.tree.pack(fill="both", padx=10, pady=8, expand=True)

        # Total label
        self.lbl_total = tk.Label(root, text="Total: 0.00", font=("Segoe UI", 11, "bold"))
        self.lbl_total.pack(pady=5)

        # Load existing CSV
        self.load_csv()

    def add_expense(self):
        d, desc, cat, amt = self.var_date.get().strip(), self.var_desc.get().strip(), self.var_cat.get().strip(), self.var_amt.get().strip()
        if not (d and desc and cat and amt):
            messagebox.showwarning("Input Error", "All fields are required!")
            return
        try:
            amt = float(amt)
        except:
            messagebox.showwarning("Input Error", "Amount must be a number!")
            return

        self.tree.insert("", "end", values=(d, desc, cat, f"{amt:.2f}"))
        self.total += amt
        self.lbl_total.config(text=f"Total: {self.total:.2f}")
        self.save_row(d, desc, cat, amt)

        # Clear fields
        self.var_desc.set(""); self.var_cat.set(""); self.var_amt.set("")

    def save_row(self, d, desc, cat, amt):
        write_header = not os.path.exists(CSV_FILE)
        with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if write_header:
                w.writerow(["Date", "Description", "Category", "Amount"])
            w.writerow([d, desc, cat, amt])

    def load_csv(self):
        if not os.path.exists(CSV_FILE):
            return
        with open(CSV_FILE, "r", encoding="utf-8") as f:
            r = csv.DictReader(f)
            for row in r:
                amt = float(row["Amount"])
                self.tree.insert("", "end", values=(row["Date"], row["Description"], row["Category"], f"{amt:.2f}"))
                self.total += amt
        self.lbl_total.config(text=f"Total: {self.total:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseApp(root)
    root.mainloop()

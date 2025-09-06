# Day 28 — SQLite Personal Finance Tracker (CLI)
# Built-in sqlite3

import sqlite3
from datetime import date

DB = "finance.db"

def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS transactions(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                t_date TEXT,
                category TEXT,
                amount REAL,
                note TEXT
            )
        """)
    print("✅ Database ready.")

def add_transaction(t_date, category, amount, note):
    with sqlite3.connect(DB) as conn:
        conn.execute("INSERT INTO transactions(t_date, category, amount, note) VALUES(?,?,?,?)",
                     (t_date, category, amount, note))
    print("✅ Added.")

def list_transactions():
    with sqlite3.connect(DB) as conn:
        cur = conn.execute("SELECT id, t_date, category, amount, note FROM transactions ORDER BY id DESC")
        rows = cur.fetchall()
    if not rows:
        print("📭 No transactions.")
        return
    print("\nID | Date       | Category    | Amount  | Note")
    print("-"*60)
    for r in rows:
        print(f"{r[0]:<3}| {r[1]:<10} | {r[2]:<11} | {r[3]:>7.2f} | {r[4]}")

def summary_by_category():
    with sqlite3.connect(DB) as conn:
        cur = conn.execute("SELECT category, SUM(amount) FROM transactions GROUP BY category")
        rows = cur.fetchall()
    if not rows:
        print("📭 No data.")
        return
    print("\nCategory Summary")
    print("-"*30)
    for cat, total in rows:
        print(f"{cat:<12} : {total:.2f}")

def delete_transaction(tid):
    with sqlite3.connect(DB) as conn:
        conn.execute("DELETE FROM transactions WHERE id=?", (tid,))
    print("🗑 Deleted if existed.")

def main():
    init_db()
    while True:
        print("\n=== Personal Finance Tracker ===")
        print("1. Add Transaction")
        print("2. List Transactions")
        print("3. Summary by Category")
        print("4. Delete by ID")
        print("5. Exit")
        c = input("Enter choice: ").strip()
        if c == "1":
            d = input(f"Date (YYYY-MM-DD) [{date.today()}]: ").strip() or str(date.today())
            cat = input("Category: ").strip()
            amt = float(input("Amount: ").strip())
            note = input("Note: ").strip()
            add_transaction(d, cat, amt, note)
        elif c == "2":
            list_transactions()
        elif c == "3":
            summary_by_category()
        elif c == "4":
            tid = input("Enter ID to delete: ").strip()
            delete_transaction(tid)
        elif c == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

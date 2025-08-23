# Day 6: Dictionaries - Contact Book (CLI)

def display_contacts(contact_book):
    """Displays all saved contacts."""
    if not contact_book:
        print("\n📭 No contacts found.")
    else:
        print("\n📒 Contact List:")
        for name, phone in contact_book.items():
            print(f"   {name} : {phone}")

def add_contact(contact_book):
    """Adds a new contact."""
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    contact_book[name] = phone
    print(f"✅ Contact '{name}' added successfully!")

def search_contact(contact_book):
    """Searches for a contact by name."""
    name = input("Enter name to search: ").strip()
    if name in contact_book:
        print(f"📌 {name} : {contact_book[name]}")
    else:
        print("❌ Contact not found.")

def delete_contact(contact_book):
    """Deletes a contact."""
    name = input("Enter name to delete: ").strip()
    if name in contact_book:
        del contact_book[name]
        print(f"🗑️ Contact '{name}' deleted successfully!")
    else:
        print("❌ Contact not found.")

def contact_book_cli():
    """Main CLI loop."""
    contact_book = {}
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_contact(contact_book)
        elif choice == "2":
            display_contacts(contact_book)
        elif choice == "3":
            search_contact(contact_book)
        elif choice == "4":
            delete_contact(contact_book)
        elif choice == "5":
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    contact_book_cli()

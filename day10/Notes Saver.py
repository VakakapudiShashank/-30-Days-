# Day 10: File Handling - Notes Saver (CLI)

def save_note(filename, note):
    with open(filename, "a") as file:
        file.write(note + "\n")
    print("✅ Note saved successfully!")

def read_notes(filename):
    try:
        with open(filename, "r") as file:
            content = file.readlines()
            if content:
                print("\n📒 Your Notes:")
                for idx, line in enumerate(content, start=1):
                    print(f"{idx}. {line.strip()}")
            else:
                print("📭 No notes found!")
    except FileNotFoundError:
        print("❌ No notes file found. Please add a note first.")

def main():
    filename = "notes.txt"
    while True:
        print("\n=== Notes Saver ===")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            note = input("Enter your note: ")
            save_note(filename, note)
        elif choice == "2":
            read_notes(filename)
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("⚠ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

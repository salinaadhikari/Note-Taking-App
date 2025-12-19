
notes = []

while True:
    print("Note-Taking App")
    print("1. Add a note")
    print("2. View all notes")
    print("3. Clear all notes")
    print("4. Exit")
    print("Enter your choice(1-4)")

    choice = input()

    if choice == "1":
        note = input("Enter your note: ")
        notes.append(note)
        print("Note added")

    elif choice == "2":
        if len(notes) == 0:
            print("No notes")
        else:
            for note in notes:
                print(note)

    elif choice == "3":
        notes.clear()
        print("All notes cleared")

    elif choice == "4":
        print("Exit")
        break
def read_phone_numbers():
    """
    Ask the user for names and numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}  

    while True:
        name = input("Enter name (or press Enter to finish): ").strip()
        if name == "":
            break

     
        if name in phonebook:
            print(f"{name} already exists. Updating the number.")

        number = input("Enter number: ").strip()

      
        if not number.isdigit():
            print("Invalid number! Please enter digits only.")
            continue

        phonebook[name] = number  

    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names and numbers in the phonebook.
    """
    print("\nPhonebook Entries:")
    if not phonebook:
        print("Phonebook is empty.")
    else:
        for name, number in phonebook.items():
            print(f"{name} -> {number}")


def lookup_numbers(phonebook):
    """
    Allows the user to look up phone numbers by name (case-insensitive).
    """
    while True:
        name = input("\nEnter name to lookup (or press Enter to exit): ").strip()
        if name == "":
            break
        
        name_lower = name.lower()
        found = False

        for stored_name in phonebook:
            if stored_name.lower() == name_lower:
                print(f"{stored_name}'s number: {phonebook[stored_name]}")
                found = True
                break

        if not found:
            print(f"{name} is not in the phonebook.")


def delete_contact(phonebook):
    """
    Allows the user to delete a contact from the phonebook.
    """
    while True:
        name = input("\nEnter name to delete (or press Enter to exit): ").strip()
        if name == "":
            break
        
        name_lower = name.lower()
        found = False

        for stored_name in phonebook:
            if stored_name.lower() == name_lower:
                del phonebook[stored_name]
                print(f"{stored_name} has been deleted.")
                found = True
                break

        if not found:
            print(f"{name} is not in the phonebook.")


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)

    while True:
        print("\nOptions:")
        print("1 - Lookup a number")
        print("2 - Delete a contact")
        print("3 - Show all contacts")
        print("4 - Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            lookup_numbers(phonebook)
        elif choice == "2":
            delete_contact(phonebook)
        elif choice == "3":
            print_phonebook(phonebook)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == '__main__':
    main()

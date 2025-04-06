def add_three_copies(my_list, data):
    
    for i in range(3):
        my_list.append(data)

def main():
    message = input("Enter a message to copy: ")
    my_list = []  # Start with an empty list
    print("List before:", my_list)  # Print the list before modification
    add_three_copies(my_list, message)  # Add three copies of the message
    print("List after:", my_list)  # Print the list after modification

if __name__ == "__main__":
    main()

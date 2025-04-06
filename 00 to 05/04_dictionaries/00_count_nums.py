from collections import defaultdict

def get_user_numbers():
    """
    Collect numbers from user input until an empty line is entered.
    Returns a list of entered numbers.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        
        if user_input == "":
            break
        
        try:
            num = int(user_input)
            user_numbers.append(num)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    return user_numbers

def count_nums(num_lst):
    """
    Count occurrences of each number in the list using a dictionary.
    """
    num_dict = defaultdict(int)
    for num in num_lst:
        num_dict[num] += 1
    return num_dict

def print_counts(num_dict):
    """
    Print the count of each number in a formatted way.
    """
    for num, count in num_dict.items():
        print(f"{num} appears {count} times.")

def main():
    """
    Collect numbers from the user, count occurrences, and display the results.
    """
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)

if __name__ == '__main__':
    main()

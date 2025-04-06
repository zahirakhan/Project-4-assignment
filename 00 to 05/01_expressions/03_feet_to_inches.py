
INCHES_IN_FOOT: int = 12

def main():
    while True:
        try:
            feet: float = float(input("Enter number of feet (or type 'exit' to quit): "))
        except ValueError:
            print("Exiting program.")
            break
        
        inches: float = feet * INCHES_IN_FOOT  
        print(f"{feet} feet is equal to {inches} inches.\n")


if __name__ == '__main__':
    main()
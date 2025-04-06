
def main():
    while True:
        try:
            dividend: int = int(input("Please enter an integer to be divided (or type 'exit' to quit): "))
            divisor: int = int(input("Please enter an integer to divide by: "))
            
            if divisor == 0:
                print("Error: Division by zero is not allowed. Please try again.\n")
                continue
            
        except ValueError:
            print("Exiting program.")
            break
        
        quotient: int = dividend // divisor  # Integer division
        remainder: int = dividend % divisor  # Modulo operation
        
        print(f"The result of this division is {quotient} with a remainder of {remainder}\n")


if __name__ == '__main__':
    main()
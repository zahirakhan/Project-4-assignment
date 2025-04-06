def main():
    #user prompt
    num = float(input("Type a number to see its square: "))
    
    # Calculate the square of the number
    squared = num ** 2
    
    # Result
    print(f"{num} squared is {squared}")

if __name__ == '__main__':
    main()
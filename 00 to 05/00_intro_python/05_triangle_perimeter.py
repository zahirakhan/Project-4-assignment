def main():
    # user prompt
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))
    
    # Calculate the perimeter of the triangle
    perimeter = side1 + side2 + side3
    
    # Result
    print(f"The perimeter of the triangle is {perimeter}")


if __name__ == '__main__':
    main()

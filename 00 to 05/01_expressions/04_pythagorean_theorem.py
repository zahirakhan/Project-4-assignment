
import math  

def main():
    while True:
        try:
            ab: float = float(input("Enter the length of AB (or type 'exit' to quit): "))
            ac: float = float(input("Enter the length of AC: "))
        except ValueError:
            print("Exiting program.")
            break
        
     
        bc: float = math.sqrt(ab**2 + ac**2)
        print(f"The length of BC (the hypotenuse) is: {bc}\n")

if __name__ == '__main__':
    main()
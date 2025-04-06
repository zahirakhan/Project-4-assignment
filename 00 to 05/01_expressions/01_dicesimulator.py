
import random
NUM_SIDES = 6

def roll_dice():
   
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2
    print(f"Die 1: {die1}, Die 2: {die2}, Total: {total}")

def main():
    die1: int = 10  # Local variable in main()
    print(f"die1 in main() starts as: {die1}")
    
    for _ in range(3):  # Roll dice three times
        roll_dice()
    
    print(f"die1 in main() is: {die1}")


if __name__ == '__main__':
    main()
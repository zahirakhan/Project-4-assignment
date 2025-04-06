
import random 


NUM_SIDES: int = 6

def roll_dice():
    """Simulates rolling two dice and returns their values and total."""
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2
    return die1, die2, total

def main():
    while True:
        input("Press Enter to roll the dice (or type 'exit' to quit): ")
        
        die1, die2, total = roll_dice()
        
        print("\nRolling the dice...")
        print(f"First die: {die1}")
        print(f"Second die: {die2}")
        print(f"Total of two dice: {total}\n")

if __name__ == '__main__':
    main()

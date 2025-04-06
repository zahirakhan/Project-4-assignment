
C: int = 299792458

def main():
    while True:
        try:
            mass_in_kg: float = float(input("Enter kilos of mass (or type 'exit' to quit): "))
        except ValueError:
            print("Exiting program.")
            break
        
        # Calculate energy
        energy_in_joules: float = mass_in_kg * (C ** 2)
        
        # Display results
        print("e = m * C^2...")
        print(f"m = {mass_in_kg} kg")
        print(f"C = {C} m/s")
        print(f"{energy_in_joules} joules of energy!\n")


if __name__ == '__main__':
    main()
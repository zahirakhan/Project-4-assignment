
DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

def calculate_seconds_in_a_year() -> int:
    """Calculates and returns the number of seconds in a year."""
    return DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN

def main():
    seconds_in_year: int = calculate_seconds_in_a_year()
    print(f"There are {seconds_in_year} seconds in a year!")

if __name__ == '__main__':
    main()
3
# Refactored: Sums user-provided integers with improved structure and error handling

MAX = 100

def calculate_sum(numbers):
    """Return the sum of a list of numbers."""
    return sum(numbers)

def get_integer(prompt):
    """Prompt the user for an integer, retrying until valid input is given."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    try:
        n = get_integer(f"Enter the number of elements (1-{MAX}): ")
        if not 1 <= n <= MAX:
            print(f"Invalid input. Please provide a number from 1 to {MAX}.")
            return

        numbers = []
        print(f"Enter {n} integers:")
        for i in range(n):
            num = get_integer(f"Element {i+1}: ")
            numbers.append(num)

        total = calculate_sum(numbers)
        print("Sum of the numbers:", total)

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()

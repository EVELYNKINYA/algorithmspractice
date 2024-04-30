def print_pyramid(symbol, num):
    # Check if the input number is odd
    if num % 2 == 0:
        print("Please enter an odd number")
        return

    # Calculate the number of rows
    rows = (num + 1) // 2

    # Print the pyramid
    for i in range(rows):
        row = (symbol * (2 * i + 1)).center(num)
        print(row)

    # Print the reversed pyramid
    for i in range(rows - 2, -1, -1):
        row = (symbol * (2 * i + 1)).center(num)
        print(row)

# Example usage
symbol = input("Enter a symbol: ")
num = int(input("Enter an odd number: "))
print_pyramid(symbol, num)
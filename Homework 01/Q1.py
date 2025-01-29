def print_multiplication_table():
    # Define the range for the multiplication table
    size = 12

    # Print the header row
    print("   ", end="")
    for i in range(1, size + 1):
        print(f"{i:4}", end="")
    print()
    print("-" * (size * 4 + 4))

    # Print the table
    for i in range(1, size + 1):
        print(f"{i:2} |", end="")  # Row header
        for j in range(1, size + 1):
            print(f"{i * j:4}", end="")
        print()  # Newline after each row

# Call the function to display the table
print_multiplication_table()

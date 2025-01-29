def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

while True:
    try:
        user_input = input("Enter a year (or type 'q' to quit): ").strip()
        
        if user_input.lower() == 'q':
            print("Exiting the program.")
            break
        
        year = int(user_input)
        
        if is_leap_year(year):
            print(f"{year} is a leap year!")
        else:
            print(f"{year} is not a leap year.")
    
    except ValueError:
        print("Invalid input. Please enter a valid year (e.g., 2024).")
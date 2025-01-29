def is_palindrome(s):
    return s == s[::-1]

while True:
    user_input = input("Enter a string to check if it's a palindrome (or type 'q' to quit): ").strip().lower()
    
    if user_input == 'q':
        print("Exiting the program.")
        break

    if is_palindrome(user_input):
        print(f"The string '{user_input}' is a palindrome.")
    else:
        print(f"The string '{user_input}' is not a palindrome.")
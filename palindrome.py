def is_palindrome(num):
    # Convert number to string
    num_str = str(num)
    
    # Check if string is same when reversed
    if num_str == num_str[::-1]:
        return True
    else:
        return False

# Example usage
number = int(input("Enter a number: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")

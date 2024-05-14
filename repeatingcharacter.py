def find_first_repeating_character(s):
    char_count = {}  # Dictionary to store the count of each character

    for char in s:
        if char in char_count:
            # If the character is encountered again, print its memory address and return it
            print(f"First repeating character: {char}, Memory address: {id(char)}")
            return char
        else:
            char_count[char] = 1  # Store the count of the character

    # If no repeating character is found, return None
    return None

# Test cases
find_first_repeating_character("hello")
find_first_repeating_character("python")
find_first_repeating_character("abcdefg")

def reverse_string_ignore_special(s):
    # Convert the string into a list to make it mutable
    s_list = list(s)
    
    # Create two pointers
    left = 0
    right = len(s) - 1

    while left < right:
        # Skip non-alphabetic characters
        if not s_list[left].isalpha():
            left += 1
        elif not s_list[right].isalpha():
            right -= 1
        else:
            # Swap the alphabetic characters
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
    
    # Join the list back into a string
    return ''.join(s_list)


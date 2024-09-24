#valid pin

def is_valid_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        for char in pin:
            if char < '0' or char > '9':  # Check if character is not numeric
                return False
        return True
    return False
s=is_valid_pin("345123")
print(s)

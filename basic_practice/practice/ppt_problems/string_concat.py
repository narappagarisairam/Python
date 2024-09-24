# check the parameters that both are string or not  then concat or else print both are different perameters

def add_strings(str1, str2):
    if isinstance(str1, str) and isinstance(str2, str):  # Check if both are strings
        return str1 + str2
    else:
        return "Both parameters must be strings."


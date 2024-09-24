#3.	Write a Python function to check whether a string is a pangram or not.
#pangram is all the alphabets should be present in agiven string.
def pangram(name1):
    name1=name1.lower()
    name2="abcdefghijklmnopqrstuvwxyz"
    for letters in name2:
        if letters not in name1:
            print("it is a not pangram")
            return
    print("it is a panagram")
            
name1=input("enter the string")
pangram(name1)

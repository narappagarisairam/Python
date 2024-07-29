#while loop 
count = 0
while count < 5:
    print(count)
    count += 1
#output
0
1
2
3
4
#another example
password = ""
while password != "secret":
    password = input("Enter the password: ")
    if password == "secret":
        print("Access granted")
    else:
        print("Access denied")

#output
Enter the password: hello
Access denied
Enter the password: world
Access denied
Enter the password: secret
Access granted


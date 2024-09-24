#in a dictonary keys followed by value will be present but we need values should convert into keys and keys should convert values

d={1:"a",2:"b",3:"c"}
inverted={values:keys for keys,values in d.items()}
print(inverted)


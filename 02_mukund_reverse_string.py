string = input("Please enter your string: ")
string2 = ''
for i in string:
    string2 = i + string2
print("\nThe original string:", string)
print("\nReversed String:", string2)
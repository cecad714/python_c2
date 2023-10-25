
input_string = input("Enter a string: ")

char_frequency = {} #create a dictionary (key=char and value=count)

for char in input_string:
    if char in char_frequency:
        char_frequency[char] += 1   #counting
    else:
        char_frequency[char] = 1

print("Character frequencies in '"+input_string+"' :")
for char, count in char_frequency.items():
    print(f"{char} occurs {count} times.")

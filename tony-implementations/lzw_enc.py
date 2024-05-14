# Initialise an empty dictionary
dictionary = {}

# Initialise all asci characters in the dictionary
for i in range(256):
    dictionary[chr(i)] = i

input_text = "aababccabdabbdec"
current_sequence = ""
encoding = []

for char in input_text:
    if current_sequence + char in dictionary:
        current_sequence += char
    else:
        encoding.append(dictionary[current_sequence])
        dictionary[current_sequence+char] = len(dictionary)
        current_sequence = char

if current_sequence:
    encoding.append(dictionary[current_sequence])

print(encoding)

for key in dictionary:
    print(key, dictionary[key])
import pandas as pd


def lzw_compression(input_string):
    dictionary = {chr(i): i for i in range(256)}

    working = df = pd.DataFrame(columns=['Position', 'String', 'Token', 'What the token encodes'])

    dict_size = 256  # Next available dictionary index
    sequence = ""    # Current sequence
    compressed_output = []  # Store the compressed output
    new_dictionary = {}  # To store only new entries

    for char in input_string:
        new_sequence = sequence + char
        if new_sequence in dictionary:
            sequence = new_sequence
        else:
            compressed_output.append(dictionary[sequence])
            # Add the new sequence to both the main dictionary and the new dictionary
            dictionary[new_sequence] = dict_size
            new_dictionary[new_sequence] = dict_size
            dict_size += 1
            sequence = char

    if sequence:
        compressed_output.append(dictionary[sequence])

    return compressed_output, new_dictionary

# Input handling
input_string = str(input("Enter the string to encode: "))
input_string = input_string.replace('␣', ' ')  # Handling space character

# Calculate the LZW compressed output and get the modified dictionary
compressed_sequence, workings = lzw_compression(input_string)

#print workings

#show workings
print(workings)

print("The LZW compressed output is: ", compressed_sequence)


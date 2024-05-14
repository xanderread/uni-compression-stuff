import pandas as pd


def lzw_compression(input_string):
    dictionary = {chr(i) if chr(i) != ' ' else '␣': i for i in range(256)}
    working = pd.DataFrame(columns=['Position', 'String', 'Token', 'What the token encodes'])

    dict_size = 256  # Next available dictionary index
    sequence = ""    # Current sequence
    compressed_output = []  # Store the compressed output
    
    for char in input_string:
        new_sequence = sequence + char
        if new_sequence in dictionary:
            sequence = new_sequence
        else:
            compressed_output.append(dictionary[sequence])
            # Add the new sequence to both the main dictionary and the new dictionary
            dictionary[new_sequence] = dict_size
            string = new_sequence
            position = dict_size
            what_it_encodes = sequence
            token = dictionary[sequence]
            working = pd.concat([working, pd.DataFrame({'Position': [position], 'String': [string], 'Token': [token], 'What the token encodes': [what_it_encodes]})])   
            dict_size += 1
            sequence = char

    if sequence:
        compressed_output.append(dictionary[sequence])

    return compressed_output, working

# Input handling
input_string = str(input("Enter the string to encode: "))
input_string = input_string.replace(' ', '␣')  # Handling space character

# Calculate the LZW compressed output and get the modified dictionary
compressed_sequence, workings = lzw_compression(input_string)

#print workings
print("The dictionary and tokens are as follows:")
#show workings
print(workings)


print("Thus the compressed output is as follows (spaces are added for readability):")
for i in compressed_sequence:
    print(i, end=' ')
    



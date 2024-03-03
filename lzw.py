# Initialize the dictionary with all ASCII characters globally
dictionary = {chr(i): i for i in range(256)}

def lzw_compression(input_string):
    global dictionary
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
input_string = input_string.replace('␣', ' ')

# Calculate the LZW compressed output and get the modified dictionary
compressed_sequence, modified_dictionary = lzw_compression(input_string)

print("The LZW compressed output is: ", compressed_sequence)
print("\nNOTE: This method doesn't print the ␣ for spaces.\n")
print("The modified part of the dictionary is: ", modified_dictionary)

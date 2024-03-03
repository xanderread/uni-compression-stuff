
print('MAKE SURE TO INCLUDE THE SPACE STRING ␣ IN THE INPUT STRING')
inp = str(input("Enter the string to encode: "))

dictionary = {"": 0}


def lz78_compression(input_string):
    # Initialize the dictionary with the empty string
   
    # Initialize an empty list to store the compressed output tokens
    compressed_output = []
    # Initialize a temporary sequence variable
    sequence = ''
    # Initialize the dictionary index
    dict_index = 1

    for char in input_string:
        # Check if the sequence with the current character exists in the dictionary
        if sequence + char in dictionary.values():
            # If it exists, append the character to the sequence
            sequence += char
        else:
            # If it does not exist, find the index of the sequence (without the current character) in the dictionary
            # If the sequence is empty, its index is 0
            sequence_index = 0 if sequence == '' else list(dictionary.keys())[list(dictionary.values()).index(sequence)]
            # Append the new sequence to the dictionary
            dictionary[dict_index] = sequence + char
            # Append the token to the compressed output list
            compressed_output.append((sequence_index, char))
            # Reset the sequence to start building a new one
            sequence = ''
            # Increment the dictionary index
            dict_index += 1

    # Handle the case where the last sequence is not empty and needs to be added to the output
    if sequence:
        sequence_index = list(dictionary.keys())[list(dictionary.values()).index(sequence)]
        compressed_output.append((sequence_index, ''))

    return compressed_output

# Example input
print("Make sure you include the space string ␣ in the input string")
# Calculate the LZ78 compressed output
compressed_sequence = lz78_compression(inp)
print("The LZ78 compressed output is: ", compressed_sequence)

print("The dictionary is: ", dictionary)


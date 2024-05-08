import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os

# Example input
inp = str(input("Enter the string to encode: "))
inp = inp.replace(' ', '␣')  # Handling space character

# Initialize the dictionary with the empty string as the first entry
dictionary = {0: ""}

def lz78_compression(input_string):
    compressed_output = []
    sequence = ''
    dict_index = 1  # Start indexing from 1 for new entries

    for char in input_string:
        if sequence + char not in dictionary.values():
            # Find the index for the sequence without the current character
            sequence_index = [k for k, v in dictionary.items() if v == sequence][0] if sequence else 0
            # Add the new sequence to the dictionary and output
            dictionary[dict_index] = sequence + char
            compressed_output.append((sequence_index, char))
            # Reset the sequence
            sequence = ''
            dict_index += 1
        else:
            # Continue building the sequence
            sequence += char

    # Handle the last sequence if non-empty
    if sequence:
        sequence_index = [k for k, v in dictionary.items() if v == sequence][0]
        # Special handling for last sequence ending with a hyphen
        dictionary[dict_index] = sequence + '-'
        compressed_output.append((sequence_index, '-'))

    return compressed_output

# Calculate the LZ78 compressed output
compressed_sequence = lz78_compression(inp)

def dict_to_df(dictionary, compressed_output):
    # Convert dictionary to DataFrame
    data = []
    for index, (prev_index, char) in enumerate(compressed_output, start=1):
        # Adjust the 'String' entry to match the dictionary built during compression
        string = dictionary.get(index, '')
        # Format the 'Token' to match expected output (previous index from the compression output, not dictionary index)
        token = f"({prev_index}, '{char}')"
        data.append({'Position': index, 'String': string, 'Token': token})
    # Include the initial empty string
    data.insert(0, {'Position': 0, 'String': '', 'Token': 'ε'})
    df = pd.DataFrame(data, columns=['Position', 'String', 'Token'])
    return df

# Output the dictionary as a DataFrame
dictionary_df = dict_to_df(dictionary, compressed_sequence)
print("The dictionary is: ")
print(dictionary_df.to_string(index=False))
print("The LZ78 compressed output is: ", compressed_sequence)

















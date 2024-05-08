


def decompress(data):
    output = []
    for offset, length, next_char in data:
        start = len(output) - offset  # Calculate the start position
        # Append the specified characters from history
        if offset > 0 and length > 0:
            for i in range(length):
                output.append(output[start + i])
        # Append the new character
        output.append(next_char)
    return ''.join(output)

# Input data as specified, using Python tuples
compressed_data = [
    (0, 0, 'r'), (0, 0, 'i'), (0, 0, 'n'), (0, 0, 'g'), (0, 0, ' '),
    (0, 0, 'a'), (2, 1, 'r'), (7, 4, 'o'), (7, 2, 'o'), (0, 0, 's'), (9, 1, 'e'), (3, 1, ' '),
    (16, 2, 'p'), (9, 1, 'c'), (0, 0, 'k'), (9, 1, 't'), (7, 1, 'f'), (0, 0, 'u'), (0, 0, 'l'), (1, 1, ' '),
    (11, 1, 'f'), (15, 3, 's'), (24, 5, 't'), (6, 1, 's'), (0, 0, 'h'), (11, 1, 'o'), (8, 9, 'w'), (20, 1, ' '),
    (11, 1, 'l'), (33, 2, 'f'), (5, 4, 'd'), (15, 1, 'w'), (0, 0, 'n')
]


print('this program requires changing the input data to a list of tuples inside the script!!!')
print('the following is being decompressed:', compressed_data)

# Decompress and print the output
result = decompress(compressed_data)
print(result)

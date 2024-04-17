def lz77_encode(text, search_buffer_size=256, look_ahead_buffer_size=256):
    encoded = []
    i = 0
    while i < len(text):
        max_length = 0
        offset = 0
        next_char = ''
        match_found = False

        print(f"Processing '{text[i]}' at position {i}:")

        for j in range(max(0, i - search_buffer_size), i):
            length = 0
            while length < look_ahead_buffer_size and i + length < len(text) and text[j + length] == text[i + length]:
                length += 1
            if length > max_length:
                max_length = length
                offset = i - j
                next_char = text[i + length] if i + length < len(text) else ''
                match_found = True

        if match_found:
            print(f"  Match found: offset = {offset}, length = {max_length}, next character = '{next_char}'")
        else:
            next_char = text[i]
            print(f"  No match found, encoding character '{next_char}'")

        # Encode the result
        encoded.append((offset, max_length, next_char))

        if max_length == 0:
            i += 1
        else:
            i += max_length + 1

    return encoded

# Take user input

print("you must define the text inside the program for this one")
text = '''Peter Piper picked a peck of pickled peppers;A peck of pickled peppers Peter Piper picked;If Peter Piper picked a peck of pickled peppers,Where’s the peck of pickled peppers Peter Piper picked?'''

# Encode the text using LZ77
encoded_text = lz77_encode(text)

# Print the encoded output
print("\nEncoded text using LZ77:")
for token in encoded_text:
    if token[2] == '':
        token = list(token)
        token[2] = '-'
        token = tuple(token)
    print(token, end=' ')

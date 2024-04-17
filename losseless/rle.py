def run_length_encode(input_string, n):
    if n <= 0:
        raise ValueError("Number of occurrences for encoding must be greater than 0")

    encoded = ""
    count = 1
    prev_char = ''

    for char in input_string:
        if char == '\\':  # Escaping the backslash itself
            if count >= n:
                encoded += '\\' + prev_char + str(count)
            else:
                encoded += prev_char * count
            encoded += '\\\\'
            count = 1
            prev_char = ''
            continue

        if prev_char == char:
            count += 1
        else:
            if count >= n:
                encoded += '\\' + prev_char + str(count)
            else:
                encoded += prev_char * count
            count = 1
            prev_char = char

    # Handle the last sequence
    if count >= n:
        encoded += '\\' + prev_char + str(count)
    else:
        encoded += prev_char * count

    return encoded

# Example usage
inp = str(input("Enter the string to encode: "))
n = int(input("Enter the number of occurrences needed for encoding (1 if not needed): ")) 
encoded_string = run_length_encode(inp, n)
print("Encoded string:", encoded_string)

# Set an infinite search window size to get the best compression ratio
search_buffer_size = float('inf')

# Set the look-ahead buffer size of infinite
look_ahead_buffer_size = float('inf')

# Set the input string
input_string = "Peter Piper picked a peck of pickled peppers;"

encoding = []

curr_index = 0
while curr_index < len(input_string):

    # Initialise the offset, length and character
    offset = 0 
    char = input_string[curr_index]
    length = 0

    # Looks in the search buffer for the longest match
    for j in range(curr_index-1, -1, -1):

        search_buffer = input_string[j:curr_index]
        look_ahead_buffer = input_string[curr_index:]

        for i in range(1,len(search_buffer)+1):
            if look_ahead_buffer.startswith(search_buffer[:i]) and i > length:
                offset = curr_index - j
                length = i
                print(search_buffer[:i])
                print(i)
                if curr_index + i < len(input_string):
                    char = input_string[curr_index + i]
                else:
                    char = ''
    # if curr_index == 1: quit()     
    encoding.append((offset, length, char))

    curr_index += length + 1


print(encoding)
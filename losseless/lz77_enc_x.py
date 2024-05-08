import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os

# Example input

def lz77_encode(input_text, search_buf_size=100, look_ahead_buf_size=100):
    i = 0
    output = []
    while i < len(input_text):
        # Set the boundaries of the search buffer and the look-ahead buffer
        search_start = max(0, i - search_buf_size)
        search_end = i
        look_ahead_end = min(i + look_ahead_buf_size, len(input_text))
        
        search_buffer = input_text[search_start:search_end]
        look_ahead_buffer = input_text[i:look_ahead_end]
        
        match_len = 0
        match_pos = 0
        next_char = ''
        
        # Try to find the longest match
        for j in range(1, len(look_ahead_buffer)):
            substring = look_ahead_buffer[:j]
            pos = search_buffer.rfind(substring)
            if pos != -1 and j > match_len:
                match_len = j
                match_pos = pos
                if i + match_len < len(input_text):
                    next_char = input_text[i + match_len]
                else:
                    next_char = ''
        
        if match_len > 0:
            offset = search_end - match_pos - match_len
            output.append((offset, match_len, next_char))
            i += match_len + 1  # Move past the matched segment and next char
        else:
            next_char = input_text[i]
            output.append((0, 0, next_char))
            i += 1  # Move past this character

    return output
    
   
print('WARNING, this code has not been tested on any past papers / practicals - check this is correct')
   
inp =str(input("Enter the string to encode: "))
inp = inp.replace(' ', '␣')  # Handling space character
search_buffer_size = int(input("Enter the search buffer / window size: "))
look_ahead_buffer_size = int(input("Enter the look-ahead buffer size: "))
encoded = lz77_encode(inp, search_buffer_size, look_ahead_buffer_size)
print(encoded)















































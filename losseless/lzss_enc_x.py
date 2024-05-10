

'''for tony to review'''




inp = input("Enter the string to be encoded: ")

# the practicals input: 
# inp = '''Peter Piper picked a peck of pickled peppers; A peck of pickled peppers Peter Piper picked; If Peter
# Piper picked a peck of pickled peppers, Where’s the peck of pickled peppers Peter Piper picked?'''

inp = inp.replace(' ', '␣')  # Handling space character

look_ahead_buffer = int(input("Enter the look ahead buffer size: "))
search_buffer = int(input("Enter the search buffer size (enter 0 if you wish for the search buffer to be infinite) "))

if search_buffer == 0:
    search_buffer = len(inp)


# memory is just the search buffer
memory = [None] * search_buffer



# works like a queue
def add_to_memory(char):
    if None in memory:
        memory[memory.index(None)] = char
    else:
        memory.pop(0)
        memory.append(char)
        

# turns a list like [,'a','b','c'] to a string 'abc'
def memory_to_string(memory):
    # Filter out None values and concatenate remaining values to a string
    return ''.join(str(item) for item in memory if item is not None)


# gets all possible subsets of a list of chars (that are relevant) ie tonysmells = [tonysmells, tonysmell, tonysmel, tonysme, tonysm, tonys, tony, ton, to]
def get_subsets(considered_letters):
    if len(considered_letters) == 1:
        return []
    subsets = [considered_letters]
    while len(considered_letters) > 2:
        considered_letters = considered_letters[:-1 ]
        subsets.append(considered_letters)
    return subsets



# pointer to which letter we are looking at in the input
letter_index = 0
sol = []
while True:
    # fuck off if done
    if letter_index >= len(inp):
        break
    
    # get the letters in the look ahead buffer
    considered_letters = inp[letter_index:letter_index + look_ahead_buffer]
 
 
    # get all the possible substrings 
    possible = get_subsets(considered_letters)
    
    print("The possible subsets are: ", possible)
    
    
    print("The memory is ", memory)
    
    encoded = False
    for subset in possible:
        if encoded:
            break
        print("Looking at subset  ", subset)
        # split subset into a list of characters
        memory_string = memory_to_string(memory)
        print("The string in the memory is ", memory_string)
        if subset in memory_string:
            print("The subset is in memory!")
            encoded = True
            print("The subset ", subset, " is in the search buffer")
            
            length = len(subset)
            
           
            memory_inx = memory_string.rindex(subset)
            
        
            subsets_index = letter_index 
            
            
            
            offset = subsets_index - memory_inx 
            
            
            print("offset is ", offset)
            
            sol.append((length, offset))
            
            for char in subset:
                add_to_memory(char)
            
            letter_index += length
            
            
        
    if not encoded:
        print("nothing was found in the memory matches anything in search buffer")
        first_letter = considered_letters[0] 
        add_to_memory(first_letter)
        sol.append(first_letter)
        letter_index += 1
        continue
        
    
    
  
def display_output(output):
    sol = ''
    for item in output:
        if type(item) == tuple:
            sol += str(item)
        else:
            sol += item
            
    print(sol)
    
    
display_output(sol)
        
        





    








    
    





    










    




import pandas as pd
from decimal import Decimal

inp = 71753375
solution_len = 5
char_frequency = {"S":5, "W":1, "I":2, "M":1, "␣":1}

# calculate the probabilities of each character and the range
probs = {}
total = sum(char_frequency.values())
for char in char_frequency:
    probs[char] = char_frequency[char] / total

# calculate the range of each character
range = {}
current_sum = 1
for char in char_frequency:
    lx_hx = ((current_sum-probs[char]), (current_sum))
    range[char] = lx_hx
    current_sum -= probs[char]
    


# create a table with the character x, the frequency, the probability, and the range lx and hx
df = pd.DataFrame(columns=['Character', 'Frequency', 'Probability', 'Range'])

for char in char_frequency:
    new_row = pd.DataFrame({
    'Character': [char],
    'Frequency': [char_frequency[char]],
    'Probability': [probs[char]],
    'Range': [range[char]]
})
    df = pd.concat([df, new_row], ignore_index=True)


print("The table is:")
print(df)
print("the number to decode is: ", inp)

inp = "0." + str(inp)
number = Decimal(inp)
#move to 0.int



# start decoding
final_str = ''



sol = pd.DataFrame(columns=['x', 'L(x)', 'H(x)', 'C'])
# add in blank row
sol = pd.concat([sol, pd.DataFrame({'x': [''], 'L(x)': [''], 'H(x)': [''], 'C': ['']})], ignore_index=True)




while len(final_str) >= solution_len:
    # find where the number lies 
    print("the number is: ", number)
    for char in range:
        if range[char][0] <= number < range[char][1]:
            
            final_str += char
            sol = pd.concat([sol, pd.DataFrame({'x': [char], 'L(x)': [range[char][0]], 'H(x)': [range[char][1]], 'C': [round(number,5)]})], ignore_index=True)
            number = (number - Decimal(range[char][0])) / Decimal(probs[char])
            
            
            # update the number to the new range
            print("the number is now: ", number)
            print(sol)
            
            # if number is close to 1, we have finished
         
             
            

            
            
            
            
            
            
            
            
               
            
            
            
print("The final decoded string is: ", final_str)
    
    
     
    
    
    
    
    
    
    
    
    



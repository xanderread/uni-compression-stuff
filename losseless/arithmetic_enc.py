import pandas as pd
from decimal import Decimal, getcontext  #need to use Decimal to avoid floating point errors
  
getcontext().prec = 30

# Input string
inp = input("Enter the string to be encoded: ")

# Calculate frequencies
frequencies = {}
for char in inp:
    if char in frequencies:
        frequencies[char] += 1
    else:
        frequencies[char] = 1

# Sort the frequencies (not necessarily needed for encoding but useful for understanding)
frequencies = dict(sorted(frequencies.items(), key=lambda item: item[1], reverse=True))

print("The frequencies are:")

print(frequencies)

# Calculate intervals
interval_data = []
intervals = {}
start = Decimal(0)

for char, freq in frequencies.items():
    intervals[char] = (round(start,1), round(Decimal(start) + Decimal(freq) / Decimal(len(inp)),1))
    interval_data.append([char, intervals[char][0], intervals[char][1]])  # 'x' is now the character

    start += Decimal(freq) / Decimal(len(inp))

# Display intervals using pandas DataFrame
print("Therefore, we split the interval as follows:")
interval_df = pd.DataFrame(interval_data, columns=['x', 'L(x)', 'H(x)'])
print(interval_df.to_string(index=False))


print("The encoding then proceeds as follows:")

x = None
low = Decimal(0)
high = Decimal(1)
output = ""
lstar = 0
hstar = 9999
encoding_steps = []




def add_encoding_steps(x, lx, hx, low, high):
    '''adds variables to encoding_steps history'''
    encoding_steps.append({'x': x, 'L(x)': lx, 'H(x)': hx, 'Low': low, 'High': high})

add_encoding_steps(x, None, None, low, high)

# loop over string
for x in inp:
    range = high - low
    low = low + range * intervals[x][0]
    high = low + range * (intervals[x][1] - intervals[x][0])
    add_encoding_steps(x, intervals[x][0], intervals[x][1], low, high)
    

encoding_df = pd.DataFrame(encoding_steps, columns=['x', 'L(x)', 'H(x)', 'Low', 'High'])

print("We used real number arithmetic - this was allowed on the mock exam, and assumed to be allowed here:")
print(encoding_df.to_string(index=False))


print("Therefore the final encoded string is the low value")

final_encoded_value = low
final_encoded_string = str(final_encoded_value).removeprefix("0.")

# Print the final encoded string
print(f"The final encoded string is: {final_encoded_string}")

    
    

    
    








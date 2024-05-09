import pandas as pd

inp = input('Enter the string to encode: ')
inp = inp.replace(' ', '␣')  # Handling space character

# Initialize the dictionary 
dic = {}


for char in inp:
    if char not in dic:
        dic[char] = 1 
    else:
        dic[char] += 1

# sort dictionary by value if the same value sort by key
sorted_dic = {k: v for k, v in sorted(dic.items(), key=lambda item: (-item[1], item[0]))}

print("We first calculate the frequencies of each character in the input string:")
print(sorted_dic)


probs = {}

# find probalities of each letter 
total = sum(sorted_dic.values())

for char in sorted_dic:
    probs[char] = sorted_dic[char] / total
    

#hard coded probs


print("We then calculate the probalities of each character in the input string:")
print(probs)

print("We then calculate B(x) the sum of probalities up to x and their corresponding binary values")
print("We use a precision of 10 for the binary fraction")
dx = {}
current_sum = 0
for char in sorted_dic:
    dx[char] = current_sum
    current_sum += probs[char] 


#create a bx df 
df = pd.DataFrame(dx.items(), columns=['Character', 'B(x)'])
print(df)


def decimal_to_binary_fraction(decimal_num, precision=10):
    # Ensure the input is a float
    decimal_num = float(decimal_num)

    # Initialize the binary representation with '0.'
    binary_fraction = "0."

    # Multiply the decimal part repeatedly by 2 to find each binary digit
    while decimal_num and len(binary_fraction) <= precision + 2:
        decimal_num *= 2
        binary_digit = int(decimal_num)
        binary_fraction += str(binary_digit)
        decimal_num -= binary_digit

    return binary_fraction






decimal = {}
for char in dx:
    decimal[char] = decimal_to_binary_fraction(dx[char])

df = pd.DataFrame(decimal.items(), columns=['Character', 'Binary B(x)'])
print(df)



print("we then calculae L(x) - where L(x) is the ceiling of log2(1/p(x))")
    
lx = {}
import math
for char in probs:
    lx[char] = math.ceil(-math.log2(probs[char]))
    
df = pd.DataFrame(lx.items(), columns=['Character', 'L(x)'])
print(df)

print("we use this to work out how many bits to use for each character in the binary representation")
print("final encoding:")

result = {}

for char in lx:
    binary = str(decimal[char])
    #get rid of everything beofre the decimal point
    dot = binary.index('.')
    binary = binary[dot+1:]
    if binary == '':
        result[char] = '0'*lx[char]
        continue
   

    result[char] = binary[:lx[char]]
    
    
df = pd.DataFrame(result.items(), columns=['Character', 'Encoding'])
print(df)


print("Thus the encoding of the string is (seperated by spaces for readability):")
encoded = ''
for char in inp:
    encoded += (result[char] + ' ')

print(encoded)
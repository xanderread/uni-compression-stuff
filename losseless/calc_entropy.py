
import math

print("Please change the frequencies in the code to run this program")

#IF YOU WANT TO USE THE FREQUENCY OF EACH char fill it in here
frequency = {}
probabilities = {}

if frequency == {}: 

    #IF YOU WANT TO USE THE Probability OF EACH char fill it in here
    probabilities = {
        'runner 1': 1/6,
        'runner 2': 1/6,
        'runner 3': 1/6,
        'runner 4': 1/8,
        'runner 5': 1/8,
        'runner 6': 1/8,
        'runner 7': 1/8
    }

else:
    #calc the probabilities
    for char in frequency:
        probabilities[char] = frequency[char] / sum(frequency.values())


# Function to calculate entropy
def calculate_entropy(probabilities):
    entropy = 0
    for p in probabilities.values():
        entropy += p * math.log2(p)
    return -entropy

# Calculate the entropy for the given race
entropy = calculate_entropy(probabilities)

print("The entropy of the race is:", round(entropy,4))
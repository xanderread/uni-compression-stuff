import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from collections import Counter
import sys
import numpy as np
from decimal import *
import math

def frequencies_to_table(frequency):
    # Step 1: Calculate total number of characters
    total_chars = sum(frequency.values())

    # Step 2: Calculate probability and cumulative probability
    probability = {char: freq / total_chars for char, freq in frequency.items()}
    # sorted_chars = sorted(probability.items(), key=lambda x: x[1], reverse=False)

    # Remove _ and add it to the end
    if '_' in probability:
        prob = probability.pop('_')
        probability['_'] = prob

    # cumulative_prob = 1

    cumulative_prob = 0

    table_data = []
    for char in probability.keys():
        prob = probability[char]
        low = cumulative_prob
        high = cumulative_prob + prob
        # low = high - prob
        if low < 0.1e-10:
            low = 0
        table_data.append([char, frequency[char], prob, (round(Decimal(low),3), round(Decimal(high),3))])
        cumulative_prob += prob
    
    # Step 3: Create a DataFrame
    df = pd.DataFrame(table_data, columns=['Character x', 'Frequency', 'Probability', 'Range [L(x),H(x)]'])
    
    return df

def calculate_bounds(text):
    # Step 1: Calculate frequency of each character
    frequency = Counter(text)
    
    return frequencies_to_table(frequency)

def input_bounds():
    char = ""

    frequencies = {}

    while char != "DONE":
        char = input("Enter a character (DONE to finish): ")
        if char == "DONE":
            break
        freq = int(input("Enter frequency: "))
        frequencies[char] = freq
    
    return frequencies_to_table(frequencies)

def get_high_low(form):
    if form == 'float':
        high = Decimal(1)
        low = Decimal(0)
    elif form == 'int':
        high = 9999
        low = 0
    else:
        high = 1
        low = 0

    return high, low

def update_bounds(low,high, char_low, char_high, form):
    if form == 'float':
        low,high = low + ((high - low) * char_low), low + ((high - low) * char_high)
        return low, high, None
    elif form == 'int':
        low,high = low + ((high - low) * char_low), low + ((high - low) * char_high)
        print(low, high)
        low, high = int(math.ceil(low)), int(math.floor(high))
        # If any of the first digits are the same, output them and shift along the number
        additional_digits = ''
        while str(low)[0] == str(high)[0]:
            additional_digits += str(int(low))[0]
            # Remove the first digit of each number and add a 0 to the end of the low or 9 to the end of the high
            low = int(str(low)[1:] + '0')
            high = int(str(high)[1:] + '9')
        return low, high, additional_digits
    else:
        high = high * char_high
        low = low * char_low

    return high, low

def show_results (workings, form):
    if form == 'int':
        # Combine digits
        workings['Digit'] = workings['Digit'].astype(str)
        # Combine the string and output it, removing all None values
        return ''.join(workings['Digit'].values).replace('None','') + str(workings.iloc[-1]['Low'])
    elif form == 'float':
        # get the final row and output the low value
        return str(round(workings.iloc[-1]['Low'],20)).split('.')[1]


def save_table_to_pdf(df, filename):
    df = df.copy()

    # If the dataframe has any tuples in columns, convert them to strings
    for col in df.columns:
        df[col] = df[col].apply(lambda x: "["+str(round(float(x[0]),3))+","+str(round(float(x[0]),3))+")" if type(x) == tuple else x)

        # If the column could be a float, round it to 3 decimal places
        try:
            df[col] = df[col].apply(lambda x: round(float(x),15))
        except:
            pass


    # Step 4: Save DataFrame to PDF
    with PdfPages(filename) as pdf:
        fig, ax = plt.subplots(figsize=(8, 3))  # Adjust the size as needed
        ax.axis('tight')
        ax.axis('off')
        table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.auto_set_column_width(col=list(range(len(df.columns))))
        
        pdf.savefig(fig, bbox_inches='tight')

# Example usage: text encode no-calc-freq
if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Usage: python3 arithmetic.py <text|value> <encoding> <form>")
        sys.exit(1)

    encoding = True
    calc_freq = True
    form = 'float'

    text = sys.argv[1]

    if len(sys.argv) >= 3 and sys.argv[2] == 'decode':
        print("Decode mode activated")
        encoding = False
    
    if len(sys.argv) >= 4 and sys.argv[3] == 'no-calc-freq':
        calc_freq = False
    
    if len(sys.argv) >= 5:
        form = sys.argv[4]

    if encoding:
        # Replace spaces with _
        text = text.replace(" ", "_")

        # Calculate frequenicies
        if calc_freq:
            df = calculate_bounds(text)
        else:
            df = input_bounds()
        
        print("------------------------------------")
        print(df)
        save_table_to_pdf(df, 'calc_frequencies.pdf')
        print("------------------------------------")

        high, low = get_high_low(form)
        
        if form == 'int':
            workings = pd.DataFrame([], columns=['Character', 'L(x)', 'H(x)', 'Digit', 'Low', 'High'])
            workings = pd.concat([workings,pd.DataFrame([[' ', 0, 1,'' , Decimal(0), Decimal(1)]], columns=['Character', 'L(x)', 'H(x)', 'Digit', 'Low', 'High'])])
        elif form == 'float':
            workings = pd.DataFrame([], columns=['Character', 'L(x)', 'H(x)', 'Low', 'High'])
            workings = pd.concat([workings,pd.DataFrame([[' ', 0, 1, Decimal(0), Decimal(1)]], columns=['Character', 'L(x)', 'H(x)', 'Low', 'High'])])

        for char in text:
            row = df[df['Character x'] == char]

            low, high, additional_digits = update_bounds(low, high, row['Range [L(x),H(x)]'].values[0][0], row['Range [L(x),H(x)]'].values[0][1], form)

            if form == 'int':
                workings = pd.concat([workings,pd.DataFrame([[char, row['Range [L(x),H(x)]'].values[0][0], row['Range [L(x),H(x)]'].values[0][1], additional_digits, low, high]], columns=['Character', 'L(x)', 'H(x)', 'Digit', 'Low', 'High'])])
            elif form == 'float':
                workings = pd.concat([workings,pd.DataFrame([[char, row['Range [L(x),H(x)]'].values[0][0], row['Range [L(x),H(x)]'].values[0][1], low, high]], columns=['Character', 'L(x)', 'H(x)', 'Low', 'High'])])

        print("------------------------------------")
        print(workings)
        save_table_to_pdf(workings, 'workings.pdf')
        print("------------------------------------")
        # Final encoding is the values after the decimal point as an integer
        
        print(show_results(workings, form))
        
    else:

        C = int(text)
        # Make C = 0.C as a decimal
        C = Decimal(f'0.{C}')

        text = ""

        # Build frequency table using user inputs
        df = input_bounds()

        print("------------------------------------")
        print(df)
        print("------------------------------------")

        workings = pd.DataFrame([], columns=['Character', 'L(x)', 'H(x)', 'C'])
        workings = pd.concat([workings,pd.DataFrame([[' ', 0, 1, C]], columns=['Character', 'L(x)', 'H(x)', 'C'])])

        low = 0
        high = 1
        while C > 1e-5:
            iterations += 1
            for index, row in df.iterrows():
                if C >= row['Range [L(x),H(x)]'][0] and C < row['Range [L(x),H(x)]'][1]:
                    character = row['Character x']
                    low = row['Range [L(x),H(x)]'][0]
                    high = row['Range [L(x),H(x)]'][1]
                    break

            C = (C - low) / (high - low)

            workings = pd.concat([workings,pd.DataFrame([[character, low, high, C]], columns=['Character', 'L(x)', 'H(x)', 'C'])])
            text += character
        
        print("------------------------------------")
        print(workings)
        print("------------------------------------")



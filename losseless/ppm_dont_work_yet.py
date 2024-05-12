
import pandas as pd
from decimal import Decimal

arrow = '→'
escape = 'esc'

# a context column as per the lecture notes
class ContextColumn:
    def __init__(self, context_length, dic):
        self.context_length = context_length
        self.dic = dic
    
    def add(self, context, next_value):
        found = False
        probability = 0
        if context != self.context_length:
            raise ValueError(f'Context length must be {self.context_length}')

        key = context + arrow + next_value # ie xx→x'''
        if key in self.dic:
            self.dic[key] += 1
            found = True
        else:
            self.dic[key] = 1
            if self.dic[context + arrow + escape] in self.dic:
                self.dic[context + arrow + escape] += 1
            else:
                self.dic[context + arrow + escape] = 1
            
        # calculate the probability - which is the number of the same contexts vs the one you took
        
# the decoder table
class DecoderTable:
    # dic is a list of context columns ordered! - autos to cold start
    def __init__(self, context_length,context_columns=None):
        self.context_length = context_length
        
        self.low = Decimal(0)
        self.high = Decimal(1)
        
        # cold start boot up a load of context columns
        if context_columns is None:
            self.context_columns = [ContextColumn(context_length, {}) for i in range(0, context_length)]
        else:
            self.context_columns = context_columns
    
    def encode(self, previous_string, next_value):
        # we will extract out the relevant columns
        relevant_string = previous_string[-self.context_length:]
        
        print("the part of the previous string within our context length is: ", relevant_string)
        # go towards 1 from the context length
        print("we then loop over all of the substrings of this relevant string")
        for length in range(1, self.context_length+1):
            order = self.context_length - length
            context_column = self.context_columns[len(self.context_columns) - order -1]

            if order == 0:
                print("We look for: ", next_value, 'this is order ', order)
                # special case here
                found,probability = context_column.add("", next_value)
            else:
                print("We look for: ", relevant_string[length:] + arrow + next_value, 'this is order ', order)
                found,probability = context_column.add(relevant_string[length:], next_value)
            
            
            # change high and low values - using the probability metric
            
            
            if found:
                break
            
            
    def display(self):
        df_titles = []
        for i in range(0, ):
            df_titles.append(f'Order {i}')

        df = pd.DataFrame(columns=df_titles) 
        print(df)
    
    def get_encoding(self):
        return self.low


#here is where you would define a table
context_length = 3
order3 = ContextColumn(context_length=3, dic={'th→i': 1, 'th→esc': 1, 'hi→s': 1, 'hi→esc': 1, 'is→u': 2, 'is→esc': 1, 'su→i': 1, 'su→esc': 1, 'ui→s': 1, 'ui→esc': 1})
order2 = ContextColumn(context_length=2, dic={'t→h':1, 't→esc':1, 'h→i':1, 'h→esc':1, 'i→s':2, 'i→esc':1, 's→u':2, 's→esc':1, 'u→i':1, 'u→esc':1})
order1 = ContextColumn(context_length=1, dic={'t':1, 'h':1, 'i':2, 's':2, 'u':2, 'esc':1})
predefined_contexts = [order3, order2, order1]
# predefined_contexts = [] - if cold start
decoder_table = DecoderTable(context_length, context_columns=predefined_contexts)


old_string = 'this␣is'
print("the string previously encoded is ", old_string)
new_char = '␣'
print("the new character is ", new_char)
decoder_table.encode(old_string, new_char)


decoder_table.display()
# this just formats a table for display










    

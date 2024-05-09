print("For this program you must change the matrix defined in the code!")
import copy

''' the missing value is represented by 'x', make sure the matrix is defined properly!'''
pixels = [
          [50,65],
          [20,'x']
          ]


def show_matrix(matrix):
    # Determine the maximum width of each column for proper alignment
    col_widths = [max(len(str(item)) for item in col) for col in zip(*matrix)]
    
    # Print each row with aligned columns
    for row in matrix:
        formatted_row = ' '.join(f'{str(item):>{col_widths[i]}}' for i, item in enumerate(row))
        print(f'| {formatted_row} |')




print("Original pixel blocks")
show_matrix(pixels)


print('1. None Filter')
print("This filter does not change the original pixel block, defaults to 0")
none_filter = copy.deepcopy(pixels)
for row in none_filter:
    for i in range(len(row)):
        if row[i] == 'x':
            row[i] = 0
show_matrix(none_filter)
            
print("2. Sub Filter")
print("We simply use the value to the left of the missing value, if there is no value to the left we default to 0")
sub_filter = copy.deepcopy(pixels)
for row in sub_filter:
    for i in range(len(row)):
        if row[i] == 'x':
            row[i] = row[i-1] if i > 0 else 0
            
show_matrix(sub_filter)

print("3. Up Filter")
print("We simply use the value above the missing value, if there is no value above we default to 0")
up_filter = copy.deepcopy(pixels)
for row in range(1,len(up_filter)):
    for i in range(len(up_filter[row])):
        if up_filter[row][i] == 'x':
            up_filter[row][i] = up_filter[row-1][i]
            
show_matrix(up_filter)
            
print("4. Average Filter")
print("We use the average of the values to the left and above the missing value, if there is no value to the left or above we default that value to 0 and use it our calculations")
def apply_average_filter(pixels):
    # Get the number of rows and columns in the matrix
    rows = len(pixels)
    cols = len(pixels[0])

    # Create a copy of the matrix to modify without affecting the original
    filtered_pixels = [row[:] for row in pixels]

    # Iterate through each pixel in the matrix
    for i in range(rows):
        for j in range(cols):
            # Check if the current pixel is the missing value 'x'
            if pixels[i][j] == 'x':
                # Initialize values to the left and above, defaulting to 0
                left = 0
                above = 0

                # Determine the left value, if available
                if j > 0:
                    left = pixels[i][j-1]
               

                # Determine the above value, if available
                if i > 0:
                    above = pixels[i-1][j]
               
               

                # Calculate the average of available values
                
                predicted_value = (left + above) // 2  # Integer division
                print("x = ", left, "+", above, "// 2 = ", predicted_value)

                # Update the matrix with the predicted value
                filtered_pixels[i][j] = predicted_value

                # Print detailed explanation of the calculations
               
               
               

    return filtered_pixels
average_filter = copy.deepcopy(pixels)
average_filter = apply_average_filter(average_filter)
show_matrix(average_filter)


def paeth_predictor(a, b, c):
    """ Calculate the Paeth predictor """
    p = a + b - c  # Initial estimate
    pa = abs(p - a)
    pb = abs(p - b)
    pc = abs(p - c)
    
    print("We calculate the paeth predictor my calculating the initial estimate p = a + b - c", "which is", "p = ", a, "+", b, "-", c, "=", p)
    print("We then calculate the differences between the initial estimate and the values to the left, above and above-left of the missing value")
    print("pa = |p - a| = |", p, "-", a, "| = ", pa)
    print("pb = |p - b| = |", p, "-", b, "| = ", pb)
    print("pc = |p - c| = |", p, "-", c, "| = ", pc)
    print("We then select the value that is closest to the initial estimate p")
    
    # Selecting the closest value
    if pa <= pb and pa <= pc:
        print("The value closest to the initial estimate p is a")
        return a
    elif pb <= pc:
        print("The value closest to the initial estimate p is b")
        return b
    else:
        print("The value closest to the initial estimate p is c")
        return c

def apply_paeth_filter(pixels):
    rows = len(pixels)
    cols = len(pixels[0])
    filtered_pixels = [row[:] for row in pixels]

    for i in range(rows):
        for j in range(cols):
            if pixels[i][j] == 'x':
                left = pixels[i][j - 1] if j > 0 else 0
                above = pixels[i - 1][j] if i > 0 else 0
                above_left = pixels[i - 1][j - 1] if i > 0 and j > 0 else 0
                
                # Calculate the Paeth prediction
                print("The Paeth predictor is calculated by selecting the value that is closest to the initial estimate p")

                prediction = paeth_predictor(left, above, above_left)
                
                # Update the pixel value
                filtered_pixels[i][j] = prediction
                
    return filtered_pixels
print("5. Paeth Filter")
paeth_filter = copy.deepcopy(pixels)
paeth_filter = apply_paeth_filter(paeth_filter)
show_matrix(paeth_filter)


    











def process_line(line):
    # Extract the first and last digits
    first_digit = next(char for char in line if char.isdigit())
    last_digit = next(char for char in reversed(line) if char.isdigit())
    
    # Concatenate and convert to a number
    result = int(first_digit + last_digit)
    return result

# Initialize the variable to store the sum
total_sum = 0

# Specify the path to your text file
file_path = 'input.txt'

# Open the file and process each line
with open(file_path, 'r') as file:
    for line in file:
        # Ignore empty lines
        if line.strip():
            # Process the line and add to the total sum
            tmp_num = process_line(line)
            print(f'{tmp_num}')
            total_sum += tmp_num

# Print the final sum
print(f'The sum of concatenated numbers is: {total_sum}')
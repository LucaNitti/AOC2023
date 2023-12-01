import re
import sys
def process_line(line: str):
    # Define a mapping from spelled-out digits to numerical digits
    MAP_DIGITS = {
        "one" : '1',  "two" :  '2', "three": '3',
        "four": '4',  "five":  '5', "six"  : '6',
        "seven": '7', "eight": '8', "nine" : '9'
    }
    
    # Define a positive lookahead pattern for finding spelled-out digits or numerical digits
    PATTERN = '(?=(one|two|three|four|five|six|seven|eight|nine|\d))'
    
    # Use regular expression to find all occurrences of the pattern in the line
    # Map spelled-out digits to numerical digits using the MAP_DIGITS dictionary
    # MAP_DIGITS.get(i, i) to get the corresponding value from the MAP_DIGITS dictionary. 
    # If i is not found in the dictionary, it defaults to keeping the original value (i itself).
    digits = [MAP_DIGITS.get(i,i) for i in re.findall(PATTERN, line)]

    # Concatenate the first and last digit and convert to an integer
    return int(''.join([digits[0],digits[-1]]))

def main(file_path):
    # Initialize the variable to store the sum
    total_sum = 0
    # Open the file and process each line
    with open(file_path, 'r') as file:
        for line in file:
            # Ignore empty lines
            if line.strip():
                # Process the line and add to the total sum
                total_sum += process_line(line)

    # Print the final sum
    print(f'The sum of concatenated numbers is: {total_sum}')

if __name__ == "__main__":
    # Check if a file path is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    # Get the file path from the command-line arguments
    file_path = sys.argv[1]

    # Call the main function with the provided file path
    main(file_path)
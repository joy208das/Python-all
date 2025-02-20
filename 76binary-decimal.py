def binary_to_decimal(binary_str):
    decimal_value = 0
    length = len(binary_str)
    
    # Loop over each digit in the binary string
    for i in range(length):
        # Get the binary digit from left to right
        bit = int(binary_str[i])
        
        # Convert binary digit to decimal using the position formula
        decimal_value += bit * (2 ** (length - 1 - i))
    
    return decimal_value

# Input from the user
binary_str = input("Enter a binary number: ")
decimal_representation = binary_to_decimal(binary_str)
print(f"Decimal representation: {decimal_representation}")

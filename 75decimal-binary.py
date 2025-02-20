def decimal_to_binary(n):
    binary = ""
    
    # Special case for 0
    if n == 0:
        return "0"
    
    # Loop to convert decimal to binary
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    
    return binary

# Input from the user
decimal_number = int(input("Enter a decimal number: "))
binary_representation = decimal_to_binary(decimal_number)
print(f"Binary representation: {binary_representation}")

# Binary to Decimal
binary_num = "1101"
decimal_num = int(binary_num, 2)
print(f"Binary {binary_num} = Decimal {decimal_num}")

# Decimal to Binary
decimal_num = 13
binary_num = bin(decimal_num).replace("0b", "")
print(f"Decimal {decimal_num} = Binary {binary_num}")

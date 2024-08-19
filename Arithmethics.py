def start_byte_overflow_demo():
    num = 0
    i = 0
    while i < 10:
        print(num, end=" ")
        num += 30
        i += 1

def demonstrate_arithmetic_operations():
    x = int(input("Please provide a number for the first operand: "))
    y = int(input("Please provide a number for the second operand: "))
    print(f"{x} + {y} =", x+y)
    print(f"{x} - {y} =", x-y)
    print(f"{x} * {y} =", x*y)
    print(f"{x} / {y} =", x//y)
    print(f"{x} % {y} =", x%y)

def convert_to_binary():
    decimal = int(input("Please provide a number: "))
    while decimal > 0:
        b = decimal % 2
        print(b)
        decimal = decimal // 2

def convert_to_number(char):
    char = char.upper()
    if char >= '0' and char <= '9':
        return ord(char) - ord('0')
    elif char >= 'A' and char <= 'F':
        return 10 + ord(char) - ord('A')
    else:
        return -1

def convert_hex_to_dec():
    result = 0
    hexadecimal = input("Please provide a hexadecimal number: ")

    for char in hexadecimal:
        code = convert_to_number(char)
        result = 16 * result + code
        print(f"{char} -> {code}")

    print(f"Corresponding decimal number: {result}")

def main():
    choice = 1
    while choice != 0:
        print("\n\n1. Byte overflow demo")
        print("2. Demonstrate arithmetic operations")
        print("3. Convert decimal to binary")
        print("4. Convert Hexadecimal to decimal")
        print("0. Exit")

        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            start_byte_overflow_demo()
        elif choice == 2:
            demonstrate_arithmetic_operations()
        elif choice == 3:
            convert_to_binary()
        elif choice == 4:
            convert_hex_to_dec()
        elif choice == 0:
            print("Exit...")
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
from email.policy import default


def print_s1(number):
    for i in range(0, number):
        print(i*i, end=" ")

def print_s2(number):
    for i in range(1, number+1):
        if i % 2 == 1:
            print(i, end=" ")
        else:
            print(i * -1, end=" ")

def print_s3(number):
    for i in range(1, number+1):
        tria = i * (i+1) // 2
        print(tria, end=" ")

def print_Tri(number):
    for i in range(1, number+1):
        for j in range(i, number+1):
            print(" ", end="")
        for k in range(1, i+1):
            print("*", end="")
        print(" ")

def err_msg():
    print("Error.")

def main():
    choice = 1
    while choice != 0:
        print("\n\n1. Square Sequence")
        print("2. Simple Math Sequence")
        print("3. Triangular Number Sequence")
        print("4. Triangular Number Visualization")
        print("0. Exit\n")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            n = int(input("\nDetermine the length of sequence: "))
            if n >= 1:
                print_s1(n)
            else:
                err_msg()
            continue

        if choice == 2:
            n = int(input("\nDetermine the length of the sequence: "))
            if n >= 1:
                print_s2(n)
            else:
                err_msg()
            continue

        if choice == 3:
            n = int(input("\nDetermine the length of the sequence: "))
            if n >= 1:
                print_s3(n)
            else:
                err_msg()
            continue

        if choice == 4:
            n = int(input("Determine the length of the sequence: "))
            if n >= 1:
                print_Tri(n)
            else:
                err_msg()
            continue

        if choice == 0:
            print("Exit...")
            break

        else:
            print("Invalid number!")
            break

if __name__ == "__main__":
    main()
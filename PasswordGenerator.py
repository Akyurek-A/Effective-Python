import string
import random

str1 = list(string.ascii_lowercase)
str2 = list(string.ascii_uppercase)
str3 = list(string.digits)
str4 = list(string.punctuation)

user_input = input("How many characters do you want in your password? ")

while True:
    try:
        num_gen = int(user_input)
        if num_gen < 8:
            print("Your number should at least be 8.")
            user_input = input("Please, Enter your number again: ")

        else:
            break

    except:
        print("Please, Enter numbers only.")

        user_input = input("How many characters do you want in your password? ")
        continue

random.shuffle(str1)
random.shuffle(str2)
random.shuffle(str3)
random.shuffle(str4)

first = round(num_gen * (40/100))
second = round(num_gen * (20/100))

result = []

for i in range(first):
    result.append(str1[i])
    result.append(str2[i])

for i in range(second):
    result.append(str3[i])
    result.append(str4[i])

random.shuffle(result)

password = "".join(result)
print(f"Generated password: {password}")

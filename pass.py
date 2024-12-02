import random
length = int(input("Enter the desired character length: "))
password = ''
for i in range(length):
    r = random.randint(26, 133)
    password += chr(r)
    print(password)

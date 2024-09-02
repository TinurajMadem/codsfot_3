import random
import string

length = int(input("Enter the length of password:"))
characters=string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(length):
    password=password+random.choice(characters)
print(password)
import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nums=['0','1','2','3','4','5','6','7','8','9']
symbols=['~','!','@','#','$','%','^','&','*','(',')','_','/','?','<','>']

no_of_letters=int(input("Number of letters you want to include in password:"))
no_of_num=int(input("Number of number you want to include in password:"))
no_of_symbols=int(input("Number of symbols you want to include in password:"))

password=[]
for i in range(1, no_of_letters+1):
  rand_char=random.choice(letters)
  password += rand_char
for i in range(1, no_of_num+1):
  rand_char=random.choice(nums)
  password += rand_char
for i in range(1, no_of_symbols+1):
  rand_char=random.choice(symbols)
  password += rand_char
# shuffle the password 
random.shuffle(password)
# print(password)
# Creating list to string
Password =""
for char in password:
  Password += char
  # print(Password)
print(f"Here is the password: {Password}")
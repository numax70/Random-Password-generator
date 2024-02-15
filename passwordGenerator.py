import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("**RANDOM PASSWORD GENERATOR")
user_letter=int(input("Type how many letters:\n "))
user_number=int(input("Type how many numbers:\n "))
user_symbol=int(input("Type how many symbols:\n "))


password_list=[]
for x in range(1, user_letter+1):
    password_list.append(random.choice(letters))
    
for y in range(1, user_number+1):
    password_list.append(random.choice(numbers))  

for z in range(1, user_symbol+1):        
    password_list.append(random.choice(symbols))

my_password_shuffled=''
random.shuffle(password_list)
for password in password_list:
    my_password_shuffled+=password
print(f"Your password generated: {my_password_shuffled}")    





  
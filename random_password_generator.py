"""
1. The problem here is to generate a set of random password containing at least letters(upper and lower cases), numbers and symbols
2. From Research of this problem, we will need to import a bunch of modules and use some conditional statemaents
3. Planning: I want generate random letters first from a set of letters and expand it later to numbers and symbols and we want our password to be a specific length say 14
4. Now let us start writing some codes """



import random as rn
new_password = ""
choice_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!/&%()=?*#@€~+][{}\!' "
length_choice_list = (int((len(choice_list))/6))
print(length_choice_list)
for x in range(length_choice_list):
    new_password += rn.choice(choice_list)
print(new_password)

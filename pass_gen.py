import random
import string

def gen_pass(min_len, numbers=True , special_char=True):
    letters=string.ascii_letters
    digits=string.digits
    special= string.punctuation 
   
    characters=letters
    if numbers:
       characters+=digits
    if special_char:
       characters+=special

    pwd=""
    # meets_criteria=False
    # has_number=False
    # has_special=False
    # while not meets_criteria or 
    while len(pwd)<min_len:
       new_char = random.choice(characters)
       pwd += new_char
    #    if new_char in digits:
    #       has_number = True
    #    elif new_char in special:
    #       has_special = True

    #    meets_criteria=True
    #    if numbers:
    #        meets_criteria + has_number
    #    if special_char:
    #       meets_criteria=meets_criteria and has_special

    return pwd      
min_len=int(input("Enter the minimum length: "))
has_number=input("Do you want to have numbers (y/n)? ").lower()=="y"
has_special= input("Do you want to have special characters (y/n)? ").lower()=="y"
pwd=gen_pass(min_len,has_number,has_special)
print(pwd)
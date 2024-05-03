import random
import string


def generate_password(password_length, has_numbers = True, numbers_repeated = 0, has_special_chars = True, special_chars_repeated = 0):

    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation

    password = []
    is_process_done = False

    letters_repeated = password_length

    if(has_numbers):
        letters_repeated -= numbers_repeated
    
    if(has_special_chars):
        letters_repeated -= special_chars_repeated

    is_numbers_repeated = 0
    is_special_chars_repeated = 0

    while not is_process_done or len(password) < password_length :

        password.append(random.choice(letters))

        if not has_numbers:
            numbers_repeated = 0
        elif is_numbers_repeated < numbers_repeated:
            password.append(random.choice(digits))
            is_numbers_repeated += 1
        
        if not has_special_chars:
            special_chars_repeated = 0
        elif is_special_chars_repeated < special_chars_repeated:
            password.append(random.choice(special_characters))
            is_special_chars_repeated += 1

        
        if len(password) == password_length:
            random.shuffle(password)
            password_string = ''.join(password)
            is_process_done = (has_numbers == bool(numbers_repeated)) and (has_special_chars == bool(special_chars_repeated))

    return password_string





numbers_repeated = 0
special_chars_repeated = 0


length = int(input("Enter the length of the password : "))


has_number = input("Do you want to include numbers? [y/n]").upper() == 'Y'

if has_number:
    numbers_repeated = int(input("Enter how many time you want to repeat numbers : "))


has_special_chars = input("Do you want to include special characters? [y/n]").upper() == 'Y'

if has_special_chars:
    special_chars_repeated = int(input("Enter how many time you want to repeat special characters : "))



password = generate_password(length, has_number, numbers_repeated, has_special_chars, special_chars_repeated)

print(password)



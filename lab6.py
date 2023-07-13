# This program encodes and decodes an 8-digit password using the below encode and decode functions in a while loop.
# This is Lab 6 for UF Online COP3502C, Summer 2023.
# This program was written by Chance Nahuway (decode) and Dylan Dixon (main/encode).
# Chance and Dylan comprise Group 20 for this lab.

# This function prints the password encoder menu.
def print_menu():
    print("Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode \n"
          "3. Quit \n")


# This function encodes an 8-digit password by shifting each digit up by 3 and then returns the encoded password.
def encode(decoded_password):
    encoded_password = ""
    for num in decoded_password:
        encoded_password += str((int(num) + 3) % 10)
    return encoded_password


# This function decodes an 8-digit password by shifting each digit down by 3 and then returns the decoded password.
def decode(encoded_password):
    decoded_password = ""
    for num in encoded_password:
        decoded_password += str((int(num) - 3) % 10)
    return decoded_password


# Establish initial variables for menu option entered by user, password entered by user and password encoded by program.
menu_option = None
entered_password = None
entered_password_encoded = None

# Establish while loop that iterates until user enters '3' to quit program.
while menu_option != '3':
    print_menu()
    menu_option = input("Please enter an option: ")
    if menu_option == '1':  # If user requests menu option 1, program asks user to enter 8-digit password.
        entered_password = input("Please enter your password to encode: ")
        if len(entered_password) == 8 and entered_password.isnumeric():  # If password is 8 digits and numeric...
            entered_password_encoded = encode(entered_password)  # use encode function to encode password.
            print("Your password has been encoded and stored!\n")
        else:
            entered_password = None  # If password isn't 8 digits and fully numeric, instruct user to enter valid entry.
            print("Your password must be exactly 8 numeric digits.\n")
    elif menu_option == '2':  # If user requests menu option 2 after valid password has been stored...
        if entered_password is not None:  # print encoded and original password for user.
            print(f"The encoded password is {entered_password_encoded}, and the original password is {entered_password}.\n")
        else:  # If user requests menu option 2 before valid password has been stored, instruct user to enter...
            print("You must enter a valid password to encode before a password can be decoded.\n")  # valid entry.
    elif menu_option != '3':  # If user requests menu option that is not 1, 2 or 3...
        print("Invalid menu option entered. Please enter a valid menu option.\n")  # instruct user to pick valid option.

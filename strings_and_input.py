"""
    File: string_and_input.py
    Author: Xin Li
    Purpose: This program will read an input string from the
        keyboard and print a prompt and save the value which
        the user types.
"""
def main():
    string = input('input string: ')
    num_1=input()
    num_2=input()
    num_1 = int(num_1)
    num_2 = int(num_2)
    length = len(string)
    print(length)
    second_character = string[1]
    print(second_character)
    if len(string) >= 10:
        first_ten = string[:10]
    else:
        first_ten = string
    print(first_ten)
    if len(string) >= 5:
        last_five = string[len(string)-5:]
    print(last_five)
    upper_string = string.upper()
    print(upper_string)
    string_lower = string.lower()
    lst_1 = ['q','w','e','r','t','y']
    if string_lower[0] in lst_1:
        print('QWERTY')
    lst_2 = ['u','i','o','p']
    if string[0] in lst_2:
        print('UIOP')
    if string_lower[0] not in lst_1:
        if string[0] not in lst_2:
            if string[0].isalpha() == True:
                print('LETTER')
    if string[0].isdigit() == True:
        print('DIGIT')
    if string[0].isalpha() == False and string[0].isdigit() == False:
        print('OTHER')
    print(num_1*num_2)
main()

"""
    File: swap.py
    Author: Xin Li
    Purpose: This program will read an input string from the
        keyboard and print a prompt and read an input string.
"""
def main():
    string = input('Please give a string to swap:')
    string.strip()
    string_new = string[int(len(string) / 2):] + string[:int(len(string) / 2)]
    print(string_new)
main()

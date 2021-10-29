"""
    File: population.py
    Author: Xin Li
    Purpose: This program will read an input string from the
        keyboard and print a prompt and read an input string.
        Remove all leading and trailing whitespace from the
        input string, and then open a 铿乴e with that name. The
        program will then read through that 铿乴e, reading the
        lines one at a time, and performing a calculation on
        the data.
"""
import os
def main():
    # chdir to the same directory as where this script is ... so
    # that open() will open the file we expect.
    this_script = os.path.realpath(__file__)
    dir_of_script = os.path.dirname(this_script)
    os.chdir(dir_of_script)

    string = input('file: ')
    string.strip()
    file = open(string, 'r')
    lines = file.readlines()
    lst = []
    lst_new=[]
    population = 0
    name =''
    total_population = 0
    total_num = 0
    for line in lines:
        if line[0] != '#':
            lst.append(line)
    for k in lst:
        if k[:len(k)-2] != (len(k)-2)*' ':
            lst_new.append(k)
    for index in lst_new:
        index = index.strip('\n')
        information = index.split(' ')
        test = False
        for i in information:
            if len(i) >= 1:
                if i[0].isdigit()== True:
                    test = True
        if test == False:
            information = index.split('\t')
        for i in information :
            if len(i) >= 1:
                if i[0].isalpha() == True:
                    name += i
                if i[0].isdigit() == True:
                    population += int(i)
                    total_population += int(i)
        print('State/Territory: ',name)
        print('Population:      ',population)
        total_num +=1
        print('')
        name =''
        population =0
    print('# of States/Territories:',total_num)
    print('Total Population:       ',total_population)
main()

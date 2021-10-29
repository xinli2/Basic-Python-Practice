"""
    File: count_items.py
    Author: Xin Li
    Purpose: This program it will read an a imput from the
        keyboard and open the file, and read it's contents.
        Sort the lines by the values, in reverse order.
"""
def main():
    lst = []
    dic= {}
    print_lst=[]
    lst_new=[]
    new_dic={}
    word = ''
    num = 0
    filename = input('File to scan:')
    filename.strip()
    file = open(filename, 'r')
    lines = file.readlines()
    for line in lines:
        if line[0] != '#':
            lst.append(line)
    for k in lst:
        if k != len(k)*' ':
            lst_new.append(k)
    for index in lst_new:
        index = index.strip('\n')
        infor = index.split(' ')
        test = False
        for i in infor:
            if len(i) >= 1:
                if i[0].isdigit()== True:
                    test = True
                if i[0] =='-':
                    test = True
        if test == False:
            infor = index.split('\t')
        if infor[len(infor)-1] != '':
            if infor[0] != '':
                if infor[0] not in dic:
                    dic[infor[0]] = infor[len(infor)-1]
                    print_lst.append(infor[0])
                else:
                    num=int(dic[infor[0]])+int(infor[len(infor)-1])
                    dic[infor[0]] = num
    for j in print_lst:
        if int(dic[j]) in new_dic:
            new_dic[int(dic[j])].append(j)
            test_new = True
            while test_new == True :
                test_new = False
                for b in range(len(new_dic[int(dic[j])])-2,-1,-1):
                    if  new_dic[int(dic[j])][b+1] > new_dic[int(dic[j])][b]:
                        word = new_dic[int(dic[j])][b]
                        new_dic[int(dic[j])][b] = new_dic[int(dic[j])][b+1]
                        new_dic[int(dic[j])][b+1] = word
                        test = True
        else:
            new_dic[int(dic[j])] = [j]
    keys = sorted(new_dic.keys())
    for n in range (len(keys)-1,-1,-1):
        for v in range (len(new_dic[keys[n]])-1,-1,-1):
            print(new_dic[keys[n]][v], keys[n])
main()

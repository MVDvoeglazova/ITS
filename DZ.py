# -*- coding: utf-8 -*-
import random
#������ �������������� �����������
def triangle(a):
    for i in range(a+1):
       print(' '*(a-i), '*'*(i*2+1))

triangle(int(input()))


#������� �� �������� ������� ��� �������� ����������� ������� ��������� ��������� ����������
def calcHist(tdata):
#   hist is a List to store histogram. It contains [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    hist = [0]*10
    for i in tdata:
        if i < 100:
            hist[0]+=1
        elif i < 200:
            hist[1]+=1
        elif i < 300:
            hist[2]+=1
        elif i < 400:
            hist[3]+=1
        elif i < 500:
            hist[4]+=1
        elif i < 600:
            hist[5]+=1
        elif i < 700:
            hist[6]+=1
        elif i < 800:
            hist[7]+=1
        elif i < 900:
            hist[8]+=1
        else: hist[9]+=1
        
    return hist

#������� �� �������� ������� ��� �������� ������ � ���������� ����������
def initListWithRandomNumbers():

    rand_list=[]
    n = 1000

    for i in range(n):
        rand_list.append(random.randint(0,999))

    return rand_list

#������� ��� ������ ���������� � ����
#def in_file(hist): 
#    with open('students.txt', 'w') as student_file:
#        student_file.write(str(hist))
#        return None 
         

#hist = calcHist(initListWithRandomNumbers())
#in_file(hist)
#������� ��� ������ ���������� �� �����
def out_file(name_file): 
    with open(name_file, 'r') as student_file:
        f  = student_file.readlines()
        print(f)
out_file('students.txt')
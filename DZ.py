#задание 2
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

##задание 1
#data = []
#k = 0
#for i in range(1000000):
#    if k<1000:
#        data.append(k)
#        k+=1
#    else: k = 0

#a = calcHist(data)
#print(a)

import time
import random

def initListWithRandomNumbers():

    rand_list=[]
    n = 1000

    for i in range(n):
        rand_list.append(random.randint(0,999))

    return rand_list

a = initListWithRandomNumbers()

# starting time
l = []
for i in range(100):
    start = time.time()
    calcHist(a)
    # end time
    end = time.time()
    # total time taken
    l.append(end - start)
print('min time =', min(l))
print('max time =', max(l))
print('mean time =', sum(l)/len(l))
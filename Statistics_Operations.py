N = int(input())
list1 = list(map(int,input().rstrip().split()))
mean = 0
median = 0
mode = 0
s = 0
length = len(list1)
#mean
for i in range(length):
    s = s + list1[i]
    mean = round(s/length,1)
list1.sort()
#median
if length % 2 != 0:
    middle = length // 2
    median  = list1[middle]
else :
    m1 = length // 2
    m2 = length // 2 - 1
    median = round((list1[m1] + list1[m2]) / 2 , 1)
#mode
c_dict = {}
list1.sort()  
for i in range(length):
    count = 0
    for j in range(1,length):
        if list1[i] == list1[j]:
            count = count + 1
            c_dict[list1[i]] = count       
maximum = max(c_dict, key = c_dict.get)  # Just use 'min' instead of 'max' for minimum.
print(mean)
print(median)
print(maximum)


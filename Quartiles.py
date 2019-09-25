'''
Q1 = left array from the median index
Q2 = median
Q3 = rigth array from the median index
'''
n = int(input())
array = list(map(int, input().strip().split()))
def med(arr):
    median = 0
    length = len(arr)
    if length % 2 != 0:
        middle = length // 2
        median  = arr[middle]
    else :
        m1 = length // 2
        m2 = length // 2 - 1
        median = (arr[m1] + arr[m2]) // 2 
    return median
array.sort()
Q2 = med(array)
Q1 = med(array[:n//2])
Q3 = med(array[(n+1)//2:])
print(Q1)
print(Q2)
print(Q3)

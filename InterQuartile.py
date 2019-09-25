import statistics as st
N = int(input())
X = list(map(int,input().strip().split()))
F = list(map(int,input().strip().split()))
S = []
for i in range(N):
    S += [X[i]] * F[i]
S.sort()
n = sum(F)
'''
if N % 2 != 0:
    q1 = st.median(S[:n//2])
    q3 = st.median(S[n//2 + 1:])
else:
    q1 = st.median(S[:n//2])
    q3 = st.median(S[n//2:])
'''
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
q1 = med(S[:n//2])
q3 = med(S[n//2 + 1:])
print(round(float(q3 - q1),1))

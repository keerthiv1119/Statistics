import math
N = int(input())
X = list(map(int,input().strip().split()))
mean = 0
s = []
length = len(X)
Sum = sum(X)
mean = Sum//length
for i in range(N):
    dif = (X[i] - mean) ** 2
    s.append(dif)
Sum2 = sum(s)
standard_deviation = math.sqrt(round(Sum2/length,1))
print(round(standard_deviation,1))

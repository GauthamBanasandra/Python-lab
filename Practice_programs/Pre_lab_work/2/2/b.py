import math

__author__ = 'gauth_000'
u, l=eval(input())
perfect_squares=[]
digit_sum={}

for i in range(u, l):
    if math.sqrt(i)==math.floor(math.sqrt(i)):
        perfect_squares.append(i)
    sum_=i
    while sum_>=10:
        sum_=sum(list(map(int, list(str(sum_)))))
    digit_sum[i]=sum_

print('perfect squares :', ', '.join(list(map(str, perfect_squares))))
print('digit sum :', digit_sum)
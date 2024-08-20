from math import gcd
def solution(a, b):
    answer = 0
    b //= gcd(a,b)
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    answer = 1 if b==1 else 2
    return answer
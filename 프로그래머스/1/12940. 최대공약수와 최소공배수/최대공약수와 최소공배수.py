import math

def lcm(n, m):
    return int(n * m / math.gcd(n, m))

def solution(n, m):
    answer = 0
    gcd = math.gcd(n, m)
    answer = [gcd, lcm(n,m)]
    return answer
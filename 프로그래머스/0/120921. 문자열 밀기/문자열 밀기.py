def solution(A, B):
    answer = 0
    while A != B:
        A = A[-1] + A[:-1]
        answer += 1
        if len(A) == len(B) and answer > len(A):
            return -1
    return answer

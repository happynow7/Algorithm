# from itertools import combinations
# def solution(numbers):
#     answer = set()
#     for i in list(combinations(numbers,2)):
#         answer.add(sum(i))
#     answer = sorted(answer)
#     return answer
def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.add(numbers[i] + numbers[j])
    answer = list(answer)
    answer.sort()
    return answer
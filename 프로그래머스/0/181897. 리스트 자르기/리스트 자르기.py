def solution(n, slicer, num_list):
    answer = []
    
    if (n == 1):
        # answer.append(num_list[0:slicer[1]+1]) <= 배열 속의 배열로 담겨서 X
        answer += num_list[0:slicer[1]+1]
    elif (n == 2):
        # answer.append(num_list[slicer[0]:])
        answer += num_list[slicer[0]:]
    elif (n == 3):
        # answer.append(num_list[slicer[0]:slicer[1]+1])
        answer += num_list[slicer[0]:slicer[1]+1]
    elif (n == 4):
        # answer.append(num_list[slicer[0]:slicer[1]+1:slicer[2]])
        answer +=num_list[slicer[0]:slicer[1]+1:slicer[2]]
    return answer
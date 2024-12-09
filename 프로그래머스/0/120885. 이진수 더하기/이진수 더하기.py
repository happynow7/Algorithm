def solution(bin1, bin2):
    return bin(int(bin1, 2) + int(bin2, 2))[2:]

# def solution(bin1, bin2):
#     return f'{int(bin1, 2) + int(bin2, 2):b}'
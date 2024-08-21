def solution(order):
    answer = 0
    pay = 0
    
    for i in order:
        if 'cafelatte' in i:
            pay += 5000
        elif 'americano' in i:
            pay += 4500
        elif 'anything' in i:
            pay += 4500
        answer = pay
    return answer

# def solution(order):
#     answer = 0
#     latte = sum([1 for latte in order if "latte" in latte])
#     america = sum([1 for america in order if "americano" in america])
#     anything = sum([1 for anything in order if "anything" in anything])
#     answer = (latte * 5000) + (america * 4500) + (anything * 4500)
#     return answer
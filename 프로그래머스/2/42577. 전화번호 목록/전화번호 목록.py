def solution(phone_book):
    answer = True
    phone_search = {}
    
    for address in phone_book:
        phone_search[address] = 1
    
    for address in phone_book:
        temp = ""
        if not answer:
            break
        for number in address:
            temp += number
            if temp in phone_search and temp != address:
                answer = False
                break
    
    return answer
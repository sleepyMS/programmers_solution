def solution(phone_book):
    headers = set([number for number in phone_book])
    
    for phone in phone_book:
        tmp = ""
        for p in phone:
            tmp += p
            if tmp in headers and tmp != phone:
                return False
    return True
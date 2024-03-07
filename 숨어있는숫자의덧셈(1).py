import re

def solution(my_string):
    a = re.findall('[0-9]', my_string)
    b = []
    for i in a:
        b.append(int(i))
    answer = sum(b)
    return answer
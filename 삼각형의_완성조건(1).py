def solution(sides):
    a = max(sides)
    sides.remove(a)
    b = sum(sides)
    if a < b:
        answer = 1
    else:
        answer = 2
    return answer
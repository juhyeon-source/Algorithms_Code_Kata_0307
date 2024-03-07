def solution(array):
    array = sorted(array)
    a = len(array) // 2 + 1
    answer = array[a-1]
    return answer
def solution(num):
    pdt, summ = (1, 0)
    for i in str(num):
        pdt *= int(i)
        summ += int(i)
    return pdt-summ
print(solution(4421))
# date : 2024-02-19
# file : ds23_rcSum.py
# desc : 재귀호출 합산함수

def addNumber(num):
    if num <= 1:
        return 1
    
    return num + addNumber(num-1) # [5 + addNumber(4)] [4 + addNumber(3)] [3 + addNuber(2)] [2 + addNuber(1)]
                                  #         15                  10                 6              3     
sum = addNumber(5) # 15
print(sum)

# 요렇게 해도 된다
# sum = 0
# for i in range(1, 6):
# sum += i
# date : 2024-02-14
# file : ds11_stack.py
# desc : 스택 전체 구현

# StackFull 확인함수
def isStackFull():
    global Size, stack, top
    if top == (Size - 1):
        return True # 스택이 꽉 찼음
    else:
        return False

# 스택에 데이터 삽입함수
def push(data):
    global Size, stack, top
    if isStackFull() == True:
        print('스택이 꽉 찼습니다')
        return
    else:
        top += 1
        stack[top] = data

# 스택 엠티 확인함수
def isStackEmpty():
    global Size, stack, top
    if top <= -1:
        return True # 스택이 비었음
    else:
        return False
    
# 스택 데이터 추출함수
def pop():
    global Size, stack, top
    if isStackEmpty() == True:
        print('스택이 비었습니다')
        return None
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return data
    
# 스택 최종데이터 추출함수
def peek():
    global stack, top
    if isStackEmpty() == True:
        print('스택이 비어있습니다')
        return None
    else:
        return stack[top]
    
# 전역변수 선언
Size = 5
stack = [None for _ in range(Size)]
top = -1

## 메인코드
if __name__ == '__main__':
     while True:
        select = input('PUSH(p), POP(o), PEEK(e), Exit(x) > ')

        if select.lower() == 'p':
            data = input('입력데이터 >> ')
            push(data)
            print(f'스택상태 : {stack}')
        elif select.lower() == 'o':
            data = pop()
            print(f'추출 데이터 : {data}')
            print(f'스택상태 : {stack}')
        elif select.lower() == 'e':
            data = peek()
            print(f'확인 데이터 : {data}')
            print(f'스택상태 : {stack}')
        elif select.lower() == 'x':
            exit(0)
        else:
            continue
# date : 2024-02-14
# file : ds11_stack.py
# desc : 스택 전체 구현
import webbrowser
import time

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
Size = 10
stack = [None for _ in range(Size)]
top = -1

## 메인코드
if __name__ == '__main__':
    urls = ['naver.com', 'daum.net', 'nate.com', 'bing.com', 'github.com']

    for url in urls:
        push(url)
        webbrowser.open(f'https://www.{url}')
        print(url, end=' --> ')
        time.sleep(1) # 1초동안 멈춤

    print('방문 종료')
    print(stack)
    time.sleep(5) # 5초동안 아무것도 하지 않고 대기함

    while True:
        url = pop() # 위의 url과 다름 이건 지역변수임
        if url == None: break

        webbrowser.open(f'https//www.{url}')
        print(url, end=' --> ')
        time.sleep(1)

    print('방문종료')
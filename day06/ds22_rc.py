# date : 2024-02-19
# file : ds22_rc.py
# desc : 재귀호출
# 무한 루프처럼 보이지만 무한 루프가 아니다

import time

def open_box():
    global count
    print(f'{count}번째 상자를 엽니다')
    count -= 1
    if count == 0:
        print('반지를 넣고 반환합니다')
        return # 이걸 빼면 무한루프
    time.sleep(0.1) # 0.5초동안 딜레이
    open_box()
    print('상자를 닫습니다')

# 전역변수
count = 10

if __name__ == '__main__':
    open_box()   # 함수는 뒤에 괄호를 해야한다 제발 기억하자!!!
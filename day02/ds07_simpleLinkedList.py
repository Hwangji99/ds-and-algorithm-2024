# date : 2024-02-13
# file : ds07_simpleLinkedList.ipynb
# desc : 단순 연결리스트 일반 구현

memory = [] # 실제 컴퓨터 메모리를 유사하게 구성한 것
# head, curr, prev 일반 변수
# head = node 
head, curr, prev = None, None, None

class Node():
    # data, link 두 개의 멤버변수 존재
    # 생성자 추가
    def __init__(self, name) -> None:
        self.data = name
        self.link = None

# 클래스 끝
# 밑에 코딩이 클래스 안에 들어가려면 printNodes(self, start)가 되어야한다
def printNodes(start): # 클래스의 멤버함수 X
    curr = start
    if curr == None: return # 다음 값이 없으니 함수를 빠져나감
    print(curr.data, end=' -> ')
    while curr.link != None:
        curr = curr.link # 노드의 다음의 노드가 current가 됨
        print(curr.data, end=' -> ') # end -> 로 해서 enter가 없음
    print() # enter 추가

dataArray = ['찬규', '지환', '경민', '소민', '은수']

# 메인 시작
if __name__ == '__main__':
    node = Node(dataArray[0]) # '찬규' 데이터를 담은 노드 생성
    head = node # 첫번째 값을 head가 가리킴
    memory.append(node) # 가짜 메모리에 집어넣음

    for data in dataArray[1:]: # 두번째 노드부터 끝까지
        prev = node
        node = Node(data) # 지환
        prev.link = node
        memory.append(node)

    printNodes(head)
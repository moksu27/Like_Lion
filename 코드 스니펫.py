# 1.zip 함수
list(zip('abcde', '12345', '원투쓰포파'))
list(zip('abcde', '12345', ['one','two','three','four','five']))
list(zip('abcde',range(1000)))

# 2.key의 함수 기준으로 정렬
def 함수(value):
    return value[1]
def 함수2(value):
    return abs(value[1] - value[0])
def 함수3(value):
    return len(value[2])
# 2차원 matrix 형태의 리스트가 주어졌을 때 함수 실행
sorted([(10, 2), (3, 5), (7, 11), (5, 6)]) # 기본은 0번째 기준
sorted([(10, 2), (3, 5), (7, 11), (5, 6)], key = 함수) # 1번째 기준
sorted([(10, 2), (3, 5), (7, 11), (5, 6)], key = 함수2) # 두 수의 차 기준으로
sorted([(10, 2, 'aa'), (3, 5, 'aaaa'), (7, 11, 'aaa'), (5, 6, 'a')], key = 함수3) #문자의 길이 기준

# 3.최솟값 구하기
s = [1,3,4,8,13,17,20]
m = float('inf')

for i in s:
    if i < m:
        m = i
print(m)

# 4.최대값 구하기
s = [1,3,4,8,13,17,20]
m = s[0]

for i in s:
    if i > m:
        m = i
print(m)


'''
스택과 큐
* 스택은 LIFO(Last-In-First-Out, 후입선출)
* 큐는 FIFO(First-In_First-Out, 선입선출)
'''
# 5.스택, 100반환
s = [10,20,30,40,50]
s.append(100) # push
s.pop() #pop

# 스택 기반 클래스
class Stack:
    def __init__(self):
        self.배열 =[]
    def push(self, data):
        self.배열.append(data)
    def pop(self):
        self.배열.pop()
    def bottom(self):
        self.배열[0]
    def top(self):
        self.배열[-1]
    def empty(self, data):
        self.배열 = []
        
s = Stack() # 인스터스 할당하여 실행
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.push(60)
s.push(70)
s.pop()
s.배열

[10, 20, 30, 40, 50, 60] # 출력


# 6.큐, 10반환
s = [10,20,30,40,50]
s.append(100) # push
s.pop(0) # pop


# 7.클래스와 인스턴스
class Car:          # 클래스 정의
    maxSpeed = 100
    maxPeople = 6
    def start(self):
        print('출발하였습니다.')
        return
    def stop(self):
        print('출발하였습니다.')
        return
    def append(self, s):
        print(f'{s}을 추가한답니다!')

k3 = Car() # 인스턴스 정의
k5 = Car()
k7 = Car()

k3.start() # 함수 실행
k3.append('경고등')


# 8.연결 리스트
class Node:
    def __init__(self, data):
        print(f'{data}가 입력되었습니다.')
        self.data = data
        self.next = None

node1 = Node(90)
node2 = Node(2)
node3 = Node(37)
node4 = Node(35)
node5 = Node(21)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node1.next.next.next.data
# 출력
'''
90가 입력되었습니다.
2가 입력되었습니다.
37가 입력되었습니다.
35가 입력되었습니다.
21가 입력되었습니다.
35
'''


# 9.링크드 리스트
class Node:                    # 노드 정의
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):        # 첫번째 노드 정의
        init = Node('init')
        self.head = init
        self.tail = init
        self.currentNode = None
        self.counter = 0
        
    def __iter__(self):
        currentNode = self.head
        currentNode = currentNode.next
        while currentNode:
            yield currentNode.data
            currentNode = currentNode.next
    
    def __len__(self):
        return self.counter
    
    def __str__(self):
        currentNode = self.head
        currentNode = currentNode.next
        result = ''
        for i in range(self.counter):
            result += f'{currentNode.data} '
            currentNode = currentNode.next
        return f'<{result[:-1]}>'
    
    def append(self, data):
        newNode = Node(data)
        self.tail.next = newNode
        # newNode.pre = self.tail 더블링크드에서 추가
        self.tail = newNode
        self.counter += 1
    
    def insert(self, inputIndex, inputData):
        currentNode = self.head
        for i in range(inputIndex):
            currentNode = currentNode.next
        newNode = Node(inputData)
        newNode.next = currentNode.next
        currentNode.next = newNode
        
        self.counter += 1

    
    def pop(self):
        lastNodeData = self.tail.data
        currentNode = self.head
        for i in range(self.counter):
            if currentNode.next == self.tail:
                self.tail = currentNode
                currentNode.next = None
                break
            currentNode = currentNode.next
        self.counter -=1
        return lastNodeData
    
    def find(self, data):
        index = -1
        currentNode = self.head
        for i in range(self.counter+1):
            if currentNode.data == data:
                return index
            index +=1
            currentNode = currentNode.next
        return -1
    
    
# 10.yield 함수: 값을 그떄 그때 반환
def g():
    counter1 = 0
    counter2 = 0
    홀짝 = '짝'
    while True:
        yield [counter1, counter2, 홀짝]
        counter1 +=1
        counter2 +=2
        if counter1 % 2 == 0:
            홀짝 = "짝"
        else:
            홀짝 = '홀'
count = 0
for i, j, k in g():
    if count == 10:
        break
    print(i,j,k)
    count += 1


# 11.더블 링크드 리스트의 기본 형태
init = {
    'head': None
}
node1 = {'data':12,'prev' : None,'next' : None}
node2 = {'data':99,'prev' : None,'next' : None}
node3 = {'data':37,'prev' : None,'next' : None}
node4 = {'data':2,'prev' : None,'next' : None}

init['head'] = node1

node1['prev'] = init
node1['next'] = node2

node2['prev'] = node1
node2['next'] = node3

node3['prev'] = node2
node3['next'] = node4

node4['prev'] = node3
node4['next'] = None

init['head']['data']
init['head']['next']['data']
init['head']['next']['next']['data']
init['head']['next']['next']['prev']['prev']['data']


# 12.양방향 트리구현
root = {
    'value': 55,
    'left': None,
    'right': None
}

node1 = {'value':99, 'left':None, 'right':None}
node2 = {'value':53, 'left':None, 'right':None}
node3 = {'value':37, 'left':None, 'right':None}
node4 = {'value':54,  'left':None, 'right':None}
root['right'] = node1
root['left'] = node2
node2['left'] = node3
node2['right'] = node4


# 13.트리 만들기(값 입력)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class Tree:
    def __init__(self, data):
        init = Node(data)
        self.root = init
        self.counter = 0
        
    def __len__(self):
        return self.counter
    
    def insert(self, data):
        newNode = Node(data)
        currentNode = self.root
        while(currentNode):
            if (data == currentNode.data):
                return
            if (data < currentNode. data):
            # 왼쪽으로 데이터 삽입
            # 해당 데이터 부분이 비어있으면 데이터를 넣고, 아니면 
                if (not currentNode.left):
                    currentNode.left = newNode
                    self.counter +=1
                    return
                currentNode = currentNode.left
            
            if (data > currentNode. data):
            # 오른쪽으로 데이터 삽입
            # 해당 데이터 부분이 비어있으면 데이터를 넣고, 아니면 
                if (not currentNode.right):
                    currentNode.right = newNode
                    self.counter +=1
                    return
                currentNode = currentNode.right
   # 깊스너큐(깊이우선 탐색은 스택, 너비우선 탐색은 큐)
    def DFS(self):
        # 깊이우선탐색, DFS(Depth First Search)
        # Stack 이용!
        result = []
        stack = [self.root]

        while(len(stack) != 0):
            current = stack.pop()
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
            result.append(current.data)
        return result

    def BFS(self):
        # 너비우선탐색, BFS(Breadth First Search)
        # Queue 이용!
        result = []
        stack = [self.root]

        while(len(stack) != 0):
            current = stack.pop()
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
            result.append(current.data)
        return result

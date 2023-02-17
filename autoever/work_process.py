import sys
from collections import deque

class Node:
    def __init__(self) -> None:
        self.left = None
        self.right = None
        self.left_work = deque()
        self.right_work = deque()

class BinaryTree:
    def __init__(self) -> None:
        self.chief = None
        self.rtn_val = 0
    
    def add(self, current, new_node=Node()):
        if self.chief == None:
            self.chief = new_node
        else:
            if current.left == None:
                current.left = new_node
            elif current.right == None:
                current.right = new_node
            else:
                self.add(current.left)
    
    def job_done(self,current, day) -> int:
        # 날짜가 홀수인지 확인
        if day%2 != 0:
            if current == self.chief:
                if current.right.right_work == None and current.right.left_work == None and  current.left.right_work == None and current.left.left_work == None:
                    pass
                else:
                    self.rtn_val += current.left_work.popleft()
            elif current.right == None and current.left == None:
                current.right_work.append(current.right.left_work.popleft())
                current.left_work.append(current.left.left_work.popleft())
            elif current.right.right_work == None and current.right.left_work == None and  current.left.right_work == None and current.left.left_work == None:
                self.job_done(current=current.left,day=day)
            else:
                current.left_work.append(current.left.left_work.popleft())
        else:
            if current == self.chief:
                self.rtn_val += current.right_work.popleft()
            elif current.right == None and current.left == None:
                current.right_work.append(current.right.left_work.popleft())
                current.left_work.append(current.left.left_work.popleft())
            elif current.right.right_work == None and current.right.left_work == None and  current.left.right_work == None and current.left.left_work == None:
                self.job_done(current=current.right,day=day)
            else:
                current.right_work.append(current.right.left_work.popleft())
        




h, k, r = map(int, sys.stdin.readline().split(' '))
works = []
for i in range(2**h):
    work_str = sys.stdin.readline().replace('\n','')
    works.append(deque(work_str.split(' ')))

bt = BinaryTree()
for i in range(2**h-1):
    bt.add(current=bt.chief)

for w in works:
    new_node = Node()
    new_node.left_work = w
    bt.add(bt.chief,new_node)

for i in range(r):
    bt.job_done(current=bt.chief,day=i+1)

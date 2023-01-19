class Node:
    def __init__(self, url:str = '', foward=None, back=None) -> None:
        self.url = url
        self.foward = foward
        self.back = back

class BrowserHistory:
    def __init__(self, url:str) -> None:
        new_node = Node(url=url)
        self.head = new_node
        self.current = new_node

    def visit(self, url:str) -> None:
        new_node = Node(url=url)
        head = self.head
        head.foward = new_node
        new_node.back = head
        self.head = new_node
        self.current = new_node

    def back(self, num:int) -> str:
        for _ in range(num):
            prev = self.current.back
            if prev == None:
                return self.current.url
            else:
                self.current = prev
        return prev.url
    
    def foward(self, num) -> str:
        for _ in range(num):
            post = self.current.foward
            if post == None:
                return self.current.url
            else:
                self.current = post
        return post.url

browserHistory = BrowserHistory('leetcode.com')
browserHistory.visit(url='google.com')
browserHistory.visit(url='facebook.com')
browserHistory.visit(url='youtube.com')
print(browserHistory.back(1))
print(browserHistory.back(1))
print(browserHistory.foward(1))
browserHistory.visit(url='linkedin.com')
print(browserHistory.foward(2))
print(browserHistory.back(7))
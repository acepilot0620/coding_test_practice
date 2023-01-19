class Node:
    def __init__(self, url:str = '', forward=None, back=None) -> None:
        self.url = url
        self.forward = forward
        self.back = back

class BrowserHistory:
    def __init__(self, url:str) -> None:
        new_node = Node(url=url)
        self.current = new_node

    def visit(self, url:str) -> None:
        new_node = Node(url=url)
        self.current.forward = new_node
        new_node.back = self.current
        self.current = new_node

    def back(self, num:int) -> str:
        for _ in range(num):
            prev = self.current.back
            if prev == None:
                return self.current.url
            else:
                self.current = prev
        return prev.url
    
    def forward(self, num) -> str:
        for _ in range(num):
            post = self.current.forward
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
print(browserHistory.forward(1))
browserHistory.visit(url='linkedin.com')
print(browserHistory.forward(2))
print(browserHistory.back(2))
print(browserHistory.back(7))
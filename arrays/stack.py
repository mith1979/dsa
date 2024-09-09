# Implementing a stack is trivial using a dynamic array
# (which we implemented earlier).
class Stack:
    def __init__(self):
        self.stack = []
    # O(1) operation
    def push(self, n):
        self.stack.append(n)
    # O(1) operation (LIFO)
    def pop(self):
        return self.stack.pop()
    # simply returns, the top element without removing it. This is also an efficient 
    # O(1)operation.
    def peek(self):
        return self.stack[-1]
    def printStack(self):
        for ele in self.stack:
            print(ele)

my_arr = [1,2,3]
st = Stack()
for ele in my_arr:
    st.push(ele)

st.printStack
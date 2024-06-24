class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []
    
    def is_empty(self):
        return len(self.__stack) == 0
    
    def is_full(self):
        return len(self.__stack) == self.__capacity

    def push(self, value):
        if self.is_full():
            raise Exception('overflow')
        self.__stack.append(value)

    def pop_stack(self):
        if self.is_empty():
            raise Exception("underflow")
        self.__stack.pop(-1)
    def top(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.__stack[-1]

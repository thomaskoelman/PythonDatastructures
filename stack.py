class Stack:
    def __init__(self):
        self.__lst = []

    def push(self, arg):
        self.__lst = [arg] + self.__lst

    def pop(self):
        res = self.__lst[0]
        self.__lst = self.__lst[1:]
        return res

    def top(self):
        return self.__lst[0]

    def is_empty(self):
        return not bool(self.__lst)


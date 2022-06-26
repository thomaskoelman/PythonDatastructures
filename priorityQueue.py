class PQueue:

    def __init__(self):
        self.__queue = []

    def is_empty(self):
        return not self.__queue

    def enqueue(self, value, priority):
        self.__queue.append((value, priority))

    def serve(self):
        self.__queue.sort(key=lambda x: x[1])
        res = self.__queue[0]
        self.__queue = self.__queue[1:]
        return res

    def peek(self):
        self.__queue.sort(key=lambda x: x[1])
        return self.__queue[0]


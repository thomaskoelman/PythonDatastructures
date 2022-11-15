class PQueue:

    def __init__(self):
        self.__queue = []

    def is_empty(self):
        return not self.__queue

    def enqueue(self, value, priority):
        self.__queue.append((value, priority))
        self.__queue.sort(reverse=True, key=lambda x: x[1])

    def serve(self):
        pair = self.__queue[0]
        self.__queue = self.__queue[1:]
        return pair[0]

    def peek(self):
        pair = self.__queue[0]
        return pair[0]


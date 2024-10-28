import threading
from datetime import datetime


class Stack:
    '''
        RPN stack class Model to manage values
    '''

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self.is_empty():
            return self._items.pop()
        raise IndexError("pop from empty stack")

    def size(self):
        return len(self._items)

    def is_empty(self):
        return self.size() == 0

    def get_items(self):
        return self._items

class StackManager:
    '''
    Manager class to handle CRD operations  of stacks in a thread safe mode
    '''

    _stacks = dict()

    #FIXME using a single lock for all stacks
    _lock = threading.Lock()

    @classmethod
    def create_stack(cls):
        with cls._lock:
            stack_id = datetime.now().strftime("%Y%m%d-%H%M%S")
            cls._stacks[stack_id] = Stack()
            return stack_id


    @classmethod
    def get_stack(cls, name):
        with cls._lock:
            return cls._stacks.get(name)


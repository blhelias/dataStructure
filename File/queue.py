from typing import List


class Queue:
    """We implement a queue with 2 stacks the 'head' is
    used to extract elements and the 'queue' to insert elements.
    this class provide the following operations:
        * test if the queue is empty
        * push an element
        * pop an element
    """
    def __init__(self) -> None:
        self.in_stack: List = [] # queue (stack)
        self.out_stack: List = [] # head (statck)

    def __len__(self) -> int:
        """get the length of the queue
        """
        return len(self.in_stack) + len(self.out_stack)

    def push(self, obj):
        """Add an element in the queue
        """
        self.in_stack.append(obj)

    def pop(self):
        """remove an element and return it
        """
        if not self.out_stack:
            self.out_stack = self.in_stack[::-1]
            self.in_stack = []
        return self.out_stack.pop()

    def is_empty(self):
        """Check if the queue is empty
        """
        return len(self) == 0


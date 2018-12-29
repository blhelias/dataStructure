from ..Heap import Heap
from copy import copy

#TODO: build some tests !!!

#############
# DEBUT  TEST
#############

items = [1, 2, 3, 4]

def test_push():
    heap = Heap(items)
    assert heap.heap == [4, 3, 2, 1]
    heap.push(5)
    assert heap.heap == [5, 4, 2, 1, 3]

def test_pop():
    heap = Heap(items)
    element = heap.pop()
    print(element)

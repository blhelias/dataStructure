from ..File import Queue
from copy import copy

file = Queue()
test_list = [1, 2, 3]
for element in test_list:
    file.push(element)

def test_len():
    file_temp = copy(file)
    assert len(file_temp) == 3
    for _ in range(3):
        file_temp.pop()
    assert len(file_temp) == 0

def test_is_empty():
    file_temp = copy(file)
    assert file.is_empty() == False
    for _ in range(3):
        file_temp.pop()
    assert file_temp.is_empty() == True



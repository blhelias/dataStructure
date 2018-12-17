from ..File import Queue

file = Queue()
test_list = [1, 2, 3]
for element in test_list:
    file.push(element)

def test_push():


def test_len():
    assert len(file) == 3



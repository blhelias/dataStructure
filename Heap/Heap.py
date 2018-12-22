from typing import List

class Heap:
    """ Tas
    """
    def __init__(self, items) -> None:
        self.n = 0
        self.heap = [None]   # index 0 will be ignored
                             # len(self.heap) = 1
        self.rank = {}
        for x in items:
            self.push(x)

    def __len__(self):
        """get length of the heap
        """
        return len(self.heap) - 1

    def push(self, x):
        """push a new element in the heap
        """
        assert x not in self.rank
        i = len(self.heap)
        self.heap.append(x) # ajout d'une nouvelle feuille
        self.rank[x] = i
        self.up(i)          # maintenir l'ordre du tas

    def pop(self):
        """Remmove an element from the heap
        """
        root = self.heap[1]
        del self.rank[root]
        x = self.heap.pop()  # Enlever la derniere feuille
        if self:             # si le tas n'est pas vide
            self.heap[1] = x # et la mettre à la racine
            self.rank[x] = 1
            self.down(1)     # maintenir l'ordre du tas

        return root

    def up(self, i):
        #TODO
        raise NotImplementedError()

    def down(self, i):
        #TODO
        raise NotImplementedError()

    def update(self, old, new):
        raise NotImplementedError()
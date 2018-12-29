import math

class Heap:
    """ Tas
    Complexite moyennne d'une opération: O(log(n))
    complexité dans le pire cas: O(n) -> a cause
    du dictionnaire.
    """
    def __init__(self, items) -> None:
        self.n = 0
        self.heap = []   # index 0 will be ignored
                             # len(self.heap) = 1
        self.rank = {}
        for x in items:
            self.push(x)

    def __len__(self):
        """get length of the heap
        """
        return len(self.heap)

    def push(self, x):
        """push a new element in the heap
        """
        assert x not in self.rank
        i = len(self)
        self.heap.append(x) # ajout d'une nouvelle feuille
        # self.rank[x] = i
        self.sift_up()          # maintenir l'ordre du tas
        # print(self)

    def pop(self):
        """Remmove an element from the heap
        """
        root = self.heap[0]
        # del self.rank[root]
        x = self.heap.pop()  # Enlever la derniere feuille
        if self:             # si le tas n'est pas vide
            self.heap[0] = x # et la mettre à la racine
            # self.rank[x] = 1
            self.sift_down()     # maintenir l'ordre du tas
        print(self)
        return root

    def sift_up(self):
        k = len(self) - 1
        while k > 0:
            p = math.floor((k - 1) / 2)
            item = self.heap[k]
            parent = self.heap[p]
            if item > parent:
                # swap
                self.heap[p], self.heap[k] = self.heap[k], self.heap[p]
                k = p
            else:
                break

    def sift_down(self):
        #TODO
        # lorsqu'un element est retire:
        # faire descendre le premier element tant quil est plus
        # grand que l'un des 2 enfants
        p = 1
        k = 0
        item = self.heap[k]
        left_child = self.heap[p]
        right_child = self.heap[p+1]

        if item < left_child or item < right_child:
            if left_child > right_child:
                # swap with left
                self.heap[p], self.heap[k] = self.heap[k], self.heap[p]
                k = p
            else:
                # swap to the right
                self.heap[p+1], self.heap[k] = self.heap[k], self.heap[p+1]
                k = p + 1
        else:
            return

        while k < len(self) - 1:
            item = self.heap[k - 1]
            p = (k * 2) - 1
            left_child = self.heap[p]
            right_child = self.heap[p+1]
            if item < left_child or item < right_child:
                if left_child > right_child:
                    # swap with left
                    self.heap[p], self.heap[k] = self.heap[k], self.heap[p]
                    k = p
                else:
                    # swap with right
                    self.heap[p+1], self.heap[k] = self.heap[k], self.heap[p+1]
                    k = p + 1
            else:
                break

    def update(self, old, new):
        raise NotImplementedError()

    def __repr__(self):
        heap_print = ""
        for elements in self.heap:
            heap_print += str(elements) + ", "
        return "[ {}]".format(heap_print)

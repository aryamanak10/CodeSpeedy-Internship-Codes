import ctypes


class DynamicArray(object):
    def __init__(self):
        self.n = 0
        self.size = 1
        self.A = self.make_array(self.size)
    
    def __len__(self): 
        return self.n 

    def add(self, ele):
        if self.n == self.size:
            self._reshape(2 * self.size)
        self.A[self.n] = ele
        self.n += 1

    def remove(self):
        if self.n == 0:
            print("Array is empty, Please add an element first.")
            return
        self.A[self.n-1] = 0
        self.n -= 1

    def appendAt(self, item, ind):
        if ind < 0 or ind > self.n:
            print("Please enter with the range of the index !")
            return
        if self.n == self.size:
            self._reshape(2*self.size)
        for i in range(self.n-1, ind-1, -1):
            self.A[i+1] = self.A[i]
        self.A[ind] = item
        self.n += 1

    def deleteAt(self, ind):
        if self.n == 0:
            print("Array is empty, Please add an element first !!")
            return
        if ind < 0 or ind >= self.n:
            return indError("The index is not within the range, Deletion is not possible.")
        if ind == self.n-1:
            self.A[ind] = 0
            self.n -= 1
            return
        for i in range(ind, self.n-1):
            self.A[i] = self.A[i+1]
        self.A[self.n-1] = 0
        self.n -= 1

    def __getiele__(self, k):
        if not 0 <= k < self.n:
            return ('k is out of bounds !')

        return self.A[k]

    def _reshape(self, new_size):
        B = self.make_array(new_size)
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.size = new_size

    def make_array(self, new_size):
        return (new_size * ctypes.py_object)()


arr = DynamicArray()
arr.add(1)
arr.add(23)
arr.appendAt(25,2)
arr.add(12)
arr.add(34)

print(arr.__len__())
print(arr.__getiele__(1))

arr.remove()
print(arr.__getiele__(3))
print(arr.__len__())

arr.add(10)
arr.add(70)
print(arr.__len__())

arr.deleteAt(1)
print(arr.__getiele__(2))
print(arr.__len__())
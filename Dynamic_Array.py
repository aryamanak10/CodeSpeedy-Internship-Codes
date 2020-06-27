import ctypes 

class DynamicArray(object): 
	def __init__(self): 
		self.n = 0 
		self.size = 1 
		self.A = self.make_array(self.size) 
    
	def add(self, ele): 
		if self.n == self.size: 
			self._reshape(2 * self.size) 
		self.A[self.n] = ele
		self.n += 1

	def remove(self): 
		if self.n==0: 
			print("Array is empty deletion not Possible") 
			return	
		self.A[self.n-1]=0
		self.n-=1

	def appendAt(self,item,ind): 
		if ind<0 or ind>self.n: 
			print("please enter appropriate ind..") 
			return
		if self.n==self.size: 
			self._reshape(2*self.size) 		
		for i in range(self.n-1,ind-1,-1): 
			self.A[i+1]=self.A[i] 	
		self.A[ind]=item 
		self.n+=1

	def deleteAt(self,ind): 
		if self.n==0: 
			print("Array is empty deletion not Possible") 
			return
		if ind<0 or ind>=self.n: 
			return indError("ind out of bound....deletion not possible")		 
		if ind==self.n-1: 
			self.A[ind]=0
			self.n-=1
			return		
		for i in range(ind,self.n-1): 
			self.A[i]=self.A[i+1]			 
		self.A[self.n-1]=0
		self.n-=1

	def __getiele__(self, k): 
		if not 0 <= k <self.n:  
			return indError('K is out of bounds !') 
		
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
print(len(arr))
arr.add(23)
print(len(arr))
class circle:
	# """docstring for ClassName"""	
	def __init__(self,r):
		 self.r= r



	def area(r):
		 PI=3.14159
		 A=PI*r*r
		 return A

	def circumference(r):
		PI=3.14159
		C=2*PI*r
		return C


class square:
	"""docstring for ClassName"""
	def __init__(self, a):

		self.a = a
		
	def area(a):
		A=a*a
		return A

	def perimeter(a):
		P=4*a
		return P

class rectangle:
	"""docstring for ClassName"""
	def __init__(self,w,l):
		
		self.w = w
		self.l=l

	def area(w,l):
		A=self.w*self.l
		return A

	def perimeter(w,l):
		P=2*(self.l+self.w)
		return P

class sphere:
	"""docstring for ClassName"""
	def __init__(self, r):
		self.r = r

	def area(r):
		PI=3.14159
		A=4*PI*self.r
		return A

	def volume(r):
		PI=3.14159
		V=4/3 *PI*self.r*self.r*self.r
		return V


		


		


       
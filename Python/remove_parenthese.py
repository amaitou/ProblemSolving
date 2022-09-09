
class stack :

	def __init__(self) :

		self.arr = []

	def _empty(self) :

		return True if len(self.arr) == 0 else False
	
	def _push(self , v) :

		self.arr.append(v)

	def _pop(self) :

		if self._empty() :
			return
		else :
			self.arr.pop()

	def _peek(self) :

		return self.arr[-1]


	def _traversal(self) :

		if self._empty() :
			return
		else :
			while not self._empty() :
				print(self._peek())
				self._pop()

def parenthese(a , b) :

	return True if a == "(" and b == ")" else False

def remove_parentheses(s) :


	x = stack()
	r = ""

	for i in s :

		if i == "(" :

			x._push(i)

		else :

			if x._empty() :

				r += i

			elif x._peek() == "(" and not parenthese(x._peek() , i) :
				pass
			else :
				x._pop()
				if i != ")" :
					r += i

	return r

# Link: https://www.codewars.com/kata/5f7c38eb54307c002a2b8cc8

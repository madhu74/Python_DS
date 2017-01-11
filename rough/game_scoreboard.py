class PlayerScore(object):
	
	def __init__(self,name,score):
		self._name = name
		self._score = score

	def getName(self):
		return self._name

	def getScore(self):
		return self._score

	def __str__(self):
		return '({0},{1})'.format(self._name,self._score)

class ScoreBoard(object):
	
	def __init__(self,capacity = 10):
		self._board = [None]*capacity
		self._n = 0

	def __getitem__(self,k):
		return self._board[k]

	def __str__(self):
		return '\n'.join(str(self._board[i]) for i in xrange(self._n))



	def add(self,newvalue):
		good = self._n < len(self._board) or newvalue.getScore() > self._board[-1].getScore()

		if good:
			if self._n <len(self._board):
				self._n += 1

			j = self._n - 1 #indexing adjustment since list starts from 0
			while j >0 and self._board[j-1].getScore() < newvalue.getScore():
				self._board[j] = self._board[j-1]
				j = j-1
			self._board[j] = newvalue


if __name__ =='__main__':
	a = ScoreBoard()
	
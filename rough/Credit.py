from __future__ import division

class Credit(object):

	def __init__(self,name,balance,limit,accno):
		self._name = name
		self._balance = balance
		self._limit = limit
		self._accno = accno

	def getbalance(self):
		return self._balance

	def getlimit(self):
		return self._limit

	def getcustomer(self):
		return self._name

	def getaccount(self):
		return self._accno


	def charge(self,amount):
		if self._balance + amount < self._limit:
			self._balance += amount
			return True
		else:
		    return False 
	
	def make_payment(self,amount):
		self._balance -= amount

class PredatoryCredit(Credit):

	def __init__(self,name,balance,limit,accno,apr):
		super(PredatoryCredit,self).__init__(name,balance,limit,accno)
		self._apr = apr

	def charge(self,amount):
		success = super(PredatoryCredit,self).charge(amount)
		if not success:
			self._balance +=5

	def monthly(self):
		if self._balance>0:
			monthly_factor = pow(1+self._apr,1/12)
			self._balance = monthly_factor*self._balance

if __name__ == '__main__':
	my_account= PredatoryCredit('madhusudan',40,50,1234567789,8.5)
	my_account.charge(80)
	print my_account.getbalance()
	my_account.charge(2.5)
	print my_account.getbalance()
	print my_account.__dict__

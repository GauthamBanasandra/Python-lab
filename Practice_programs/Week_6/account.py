class Account:
	acc_no=0
	
	def __init__(self, name, address):
		self.name=name
		self.address=address
		Account.acc_no+=1
		self.account_no=Account.acc_no
	
	def display(self):
		print('account no. :', self.account_no)
		print('name :', self.name)
		print('address :', self.address)

class FD_Account(Account):
	def __init__(self, name, address, amt, period, rate):
		super().__init__(name, address)
		self.amt=amt
		self.period=period
		self.rate=rate
		self.trans=0
		
	def deposit(self, amt):
		self.amt+=amt
		self.trans+=1
		print(int(amt), 'added to', self.name)
	
	def withdraw(self, amt):
		if self.amt>=amt:
			self.amt-=amt
			self.trans+=1
			print(int(amt), 'withdrawn from', self.name)
		else:
			print('insufficient balance in', self.name)
	
	def total_balance(self):
		return self.amt+self.amt*self.period*self.rate
	
	def display(self):
		super().display()
		print('balance :', self.amt)
		print('period :', self.period)
		print('rate of interest :', self.rate)
		print('no. of transactions :', self.trans, '\n')

import random as r
a=FD_Account('A', 'Earth', r.random()*1000+1, r.random()*10+1, r.random()+1)
b=FD_Account('B', 'Moon', r.random()*1000+1, r.random()*10+1, r.random()+1)
c=FD_Account('C', 'Mars', r.random()*1000+1, r.random()*10+1, r.random()+1)
d=FD_Account('D', 'Jupiter', r.random()*1000+1, r.random()*10+1, r.random()+1)
accounts=[a, b, c, d]

for i in range(100):
	idx=int(r.random()*10)%len(accounts)
	accounts[idx].deposit(r.random()*1000) if r.random()*10>5 else accounts[idx].withdraw(r.random()*1000)

accounts=sorted(accounts, key=lambda x : x.trans, reverse=True)

for acc in accounts:
	acc.display()

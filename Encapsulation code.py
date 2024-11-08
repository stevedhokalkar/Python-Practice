class Bank_Account:
	def __init__(self):
		self.balance=2000
		user_account_no=int(input("Enter Account Number: "))

	def deposit(self):
		amount=float(input("Enter amount to be Deposited: "))
		self.balance += amount
		print("\n Amount Deposited:",amount)

	def withdraw(self):
		amount = float(input("Enter amount to be Withdrawn: "))
		if self.balance>=amount:
			self.balance-=amount
			print("\n You Withdraw:", amount)
		else:
			print("\n Insufficient balance ")

	def display(self):
		print("\n Net Available Balance=",self.balance)

obj = Bank_Account()

obj.deposit()
obj.withdraw()
obj.display()

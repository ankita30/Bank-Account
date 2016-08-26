#Main class 
class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
    
  def __repr__(self):
   	return "Account belongs to " + self.name + " having balance of %.2f" %self.balance
   
  def show_balance(self):
    print "Account balance is %.2f" %self.balance
  
  def deposit(self, amount):
    if amount <=0:
      print "Invalid amount entered!"
    else:
      print "%.2f amount is being deposited" % amount
      self.balance += amount
      self.show_balance()
   
  def withdraw(self, amount):
    if amount > self.balance:
      print "Entered amount is higher than balance!"
    else:
      print "%.2f amount is withdrawn" % amount
      self.balance -= amount
      self.show_balance()

#Create Ankita names Bank Account      
my_account = BankAccount("Ankita")
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account

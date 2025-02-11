class CreditCard:
    def __init__(self,customer,bank,account,limit):
        self._customer = customer
        self._balance = 0
        self._bank = bank
        self._account = account
        self._limit = limit

    def get_customer(self):
        "Return the name of customer"
        return self._customer

    def get_bank(self):
        "Returns the bank name of customer"
        return self._bank

    def get_account(self):
        "return the account number of customer"
        return self._account

    def get_balance(self):
        "Returns the Balance of customer which is default zero (0)"
        return self._balance

    def get_limit(self):
        "Returns the Limit of customer"
        return self._limit
    

    def charge(self,price):
        "Penalty True/False if he makes a payment more than his limits"
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self,amount):
        "The customer makes mayment"
        self._balance -= amount



# if __name__ == "__main__":
#     my_card=CreditCard("ashish","ABC bank","123456789",1000)
#     print(my_card.get_balance())
#     print(my_card.make_payment(200))
    
#     print(my_card.charge(25))
#     print(my_card.get_balance())


if __name__ == '__main__' :
    wallet = [ ]
    wallet.append(CreditCard( 'John Bowman' , 'California Savings' ,'5391 0375 9387 5309' , 2500) )
    wallet.append(CreditCard('John Bowman' , 'California Federal' ,'3485 0399 3395 1954' , 3500) )
    wallet.append(CreditCard( 'John Bowman' , 'California Finance' ,'5391 0375 9387 5309' , 5000) )
    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)
    for c in range(3):
        print( 'Customer =' , wallet[c].get_customer( ))
        print( 'Bank =' , wallet[c].get_bank( ))
        print( 'Account =' , wallet[c].get_account( ))
        print( 'Limit =' , wallet[c].get_limit( ))
        print( 'Balance =' , wallet[c].get_balance( ))
    while wallet[c].get_balance( ) > 100:
        wallet[c].make_payment(100)
        print( 'New balance =' , wallet[c].get_balance( ))
    print()
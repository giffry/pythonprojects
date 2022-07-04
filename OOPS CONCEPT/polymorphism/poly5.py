class Bank:
    bank_name="SBI"
    def acct_creatn(self,name,acct_no):
        self.name=name
        self.acct_no=acct_no
        self.min_bal=2000
        self.bal=self.min_bal

    # def withdraw(self,amount):
    #     self.amount=amount
    #     self.bal=self.bal-self.amount
    #     if(self.amount<=self.bal):
    #       print(self.amount,"money debited from your accnt",self.bal)
    #     else:
    #         print("insuffient balance")

    def deposit(self,amount1):
        self.amount1=amount1
        self.bal=self.bal+self.amount1
        print(self.amount1,"money credited to your acct ","balance amount is rs",self.bal)

    def withdraw(self,amount):
        self.amount=amount
        self.bal=self.bal-self.amount
        if(self.amount<=self.bal):
          print(self.amount,"money debited from your accnt",self.bal)
        else:
            print("insuffient balance")


ob=Bank()
ob.acct_creatn("arjun",123456789)
ob.deposit(1000)
ob.withdraw(3500)


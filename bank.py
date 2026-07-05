class Bankaccount:
    
    def newAccount(self,name,number,balance,password):
        self.name = name
        self.number = number
        self.balance = balance
        self.password = password
        
        filename = f"{self.number}.txt"
        
        with open(filename, "a") as f:
              f.write(f"NAME : {self.name} , ACCOUNT NUMBER : {self.number} , BALANCE : {self.balance}\n")

    def secure(self):
         
         print("ENTER ACCOUNT NUMBER")
        
         num = int(input())
        
         print("ENTER A PASSWORD\n")
        
         passe = int(input())
         
         if passe == self.password and num== self.number:
              self.choose()
         
         else:
              print("PASSWORD OR NUMBER IS INVALID")

    def deposit(self,add):

        filename = f"{self.number}.txt"       

        self.balance +=add
        
        print(f"CREDITED : {add} TOTAL BALANCE : {self.balance}")
        
        with open(filename , "a") as f:
              f.write(f"CREDITED : {add} TOTAL BALANCE : {self.balance}\n")
    
    def withdraw(self,amount):
        
        filename = f"{self.number}.txt"
        
        if(amount>self.balance):
                    print("INSUFFICIENT BALANCE")
        
        else:
           
            self.balance-=amount
           
            print(f"DEBITED : {amount} TOTAL BALANCE : {self.balance}")
            
            with open(filename, "a") as f:
                f.write(f"DEBITED : {amount} TOTAL BALANCE : {self.balance}\n")

    def enquiry(self):
        
         print(f"YOUR BALANCE {self.balance}")
    
    def history(self):
         
         filename = f"{self.number}.txt"
        
         with open(filename , "r") as f:
              for i in f:
                   print(i.strip())
    
    def choose(self):
         
         print("CHOOSE\n WITHDRAW,DEPOSIT,ENQUIRY,HISTORY OR EXIT") 
         
         inp = input("ENTER\n")
         
         if inp == "WITHDRAW":
              
              amo = int(input("ENTER AMOUNT TO WITHDRAW\n"))
              self.withdraw(amo)
        
         elif inp == "DEPOSIT":
             
              dep = int(input("ENTER AMOUNT TO DEPOSIT\n"))
              self.deposit(dep)
         
         elif inp == "ENQUIRY":
              self.enquiry()
         
         elif inp == "HISTORY":
              self.history()
        
         elif inp == "EXIT":
              return
         
         else:
              print("INVALID")

acc1 = Bankaccount()
acc1.newAccount("DISHANT" , 101 , 50000,556)
acc1.secure()
acc1.choose()
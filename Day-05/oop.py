#Smart budget and expense management system
class account():
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email
        self.lt=[]

    def create_account(self):
        self.lt[count]=[email,age
        
print('======= Smart budget and expense management system =======')
print('Enter 1 for Creating Account')
print('Enter 2 to Add Budget')
print('Enter 2 to Set Monthly Budget')
print('Enter 3 to Check Remaining Budget')
print('Enter 4 to Check Expense Summary')
print('Enter 5 to check Highest Expense')
print('Enter 6 to Exit')
choice=int(input('Enter a choice: '))
while(1):
    if choice == 1:
        name=input('Enter a Name: ')
        age=int(input('Enter a Age: '))
        email=print('Enter a Phone number: ')
        a=account()
        b=a.create_account(name,age,email)
print()
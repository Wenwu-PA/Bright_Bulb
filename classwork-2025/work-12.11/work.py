# Базовый

class Student:
    def __init__(self,name: str,grade: int,student_id: int):
        self.name = name
        self.grade = grade
        self.student_id = student_id
    def upgrade_grade(self):
        if self.grade + 1 <= 12:
            self.grade += 1
        else:
            print("Max grade")
    def print_info(self):
        print(self.name,self.grade,self.student_id)
    
# stud = Student("gosha",1,2)
# stud.print_info()

# Средний

class BankAccount:
    def __init__(self,owner: str,account_number: int,balance: int):
        self.owner = owner
        self.account = account_number
        self._balance = balance
    def deposit(self,amount):
        self_balance += amount
    def withdraw(self,amount):
        if self._balance - amount >=0:
            self._balance -= amount
        else:
            return "Error"
    def get_balance(self):
        return self._balance

account = BankAccount("art",12,232)
print(account.get_balance())


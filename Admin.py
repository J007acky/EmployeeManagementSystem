import json

from User import user
from database import viewUsers


def ViewAll():
   viewUsers()

def Delete():
    pass

def Update():
    pass


operations = {
    "View":ViewAll,
    "Delete":2,
    "Update":3,
    "Quit":4
}

class Admin(user):
    def __init__(self,email,password,):
        super().__init__(email,password)

    def load_database(self):
        with open("admin_data.json","r") as json_file:
            self.db = json.load(json_file)[0]

    def login(self):
        self.load_database()
        if self.db['email'] == self.email and self.db['password'] == self.password:
            print("Login Successfull!!!")
        else:
            print("Login Failed!!!")
        self.menu()
    def menu(self):
        while True:
            print("Enter Operations : \n")
            user_input = input("View : view all Employees\n"
                  "Delete : Delete particular employee\n"
                  "Update : Update Employee Details\n"
                    "Quit : Exit")
            if user_input == 'Quit':
                return
            operation = operations[user_input]
            operation()
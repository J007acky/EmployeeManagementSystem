from Admin import Admin
import database

if __name__=="__main__":
    user_input = input("1 - Login as User\n"
                       "2 - Login as Admin\n"
                       "3 - Signup new User")
    if user_input == '2':
        email = input('Email : ')
        password = input('Password : ')
        admin = Admin(email,password)
        admin.login()
    if user_input == '3':
        database.signup()
import json

with open('user_data.json', 'r+') as json_file:
    db = json.load(json_file)


class database:
    @staticmethod
    def dbReload():
        with open('user_data.json', 'r+') as json_file:
            json_file.seek(0)
            json.dump(db, json_file)

    @staticmethod
    def seekUser(email,password):
        admin_json = db[0]['admin_details']
        emp_json = db[0]['user_details']
        for user in admin_json:
            if user['email'] == email and user ['password'] == password:
                return 'admin'
        for user in emp_json:
            if user['email'] == email and user ['password'] == password:
                return 'employee'
        return 'No'

    @staticmethod
    def signup(user):
        db[0]['user_details'].append(user)
        database.dbReload()


    @staticmethod
    def viewUsers():
        for user in db[0]['user_details']:
            print(user)


    @staticmethod
    def deleteUser():
        emp_json = db[0]['user_details']

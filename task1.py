import bcrypt
database=[]
def register():
    username=input("Type in the Username you want to register with: ")
    password=input("Type in the password you want to register with: ")
    salt=bcrypt.gensalt()
    hashed_pw=bcrypt.hashpw(password.encode('utf-8'),salt)
    database.append({'username': username, 'password': hashed_pw})
    print("Registration successful")
def login():
    u=input("Type in the Username you want to login with: ")
    p=input("Type in the Password you want to login with: ")
    user=next((user for user in database if user['username']==u),None)
    if user and bcrypt.checkpw(p.encode('utf-8'),user['password']):
        print("Login Successful!")
    else:
        print("Login Unsuccessful!")
register()
login()
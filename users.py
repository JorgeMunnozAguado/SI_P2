import os
import sys
import json

FOLDER_PATH = "users/"

class Users:

    def __init__(self, name, password, ccard, balance, email):

        self.name = name
        self.password = password
        self.ccard = ccard
        self.balance = balance
        self.email = email

    @staticmethod
    def createNewUser(name, password, ccard, balance, email):
        
            if not os.path.exists(FOLDER_PATH + name):
            
                os.makedirs(FOLDER_PATH + name)
                f = open(FOLDER_PATH + name + "/info.json", "w")
                f.write('{"name":"' + name + '","password":"' + password + '","ccard":"' + ccard + '","balance":"' + balance + '","email":"' + email + '"}')
                
                return Users(name, password, ccard, balance, email)
                
            else: return None
            
    @staticmethod
    def getUserFromDB(name):

        if not os.path.exists(FOLDER_PATH + name):
            return None            
        
        file = open(FOLDER_PATH + name + "/info.json", "r")
        
        parse = json.loads(file.read())
        
        return Users(parse['name'], parse['password'], parse['ccard'], parse['balance'], parse['email'])
        
    @staticmethod
    def checkUser(name, password):

        user = Users.getUserFromDB(name)
        
        if not (user is None):
            
            if user.password == password:
                return True
            
        return False

    def __getitem__ (self, name):
    
        if name == 'name':
            return name
            
        if name == 'password':
			return password
            
        if name == 'ccard':
			return ccard
            
        if name == 'balance':
			return balance

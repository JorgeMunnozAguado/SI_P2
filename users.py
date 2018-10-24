import os
import sys
import json
import time

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
                
                file = open(FOLDER_PATH + userName + "/films.json", "w")
                file.write('{"films":[]}')
                
                file = open(FOLDER_PATH + name + "/info.json", "w")
                file.write('{"name":"' + name + '","password":"' + password + '","ccard":"' + ccard + '","balance":"' + balance + '","email":"' + email + '"}')
                
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
        
    @staticmethod
    def buyFilm(userName, filmName, price):

        user = Users.getUserFromDB(userName)
        
        if user is None:
            return False
            
        file = open(FOLDER_PATH + userName + "/films.json", "r")
        
        parse = json.loads(file.read())
        
        if not ({'name':filmName} in parse['films']): # MEJORAR--------------------------------------------------- NO SE SI FUNCIONAA

            parse['films'].append({'name':filmName, 'date':time.strftime("%x"), 'price':price})
        
        file = open(FOLDER_PATH + userName + "/films.json", "w")
        
        file.write(json.dumps(parse))
            
        return True
        
    @staticmethod
    def listUserFilms(userName):

        user = Users.getUserFromDB(userName)
        
        if user is None:
            return None
            
        file = open(FOLDER_PATH + userName + "/films.json", "r")
        
        parse = json.loads(file.read())
        
        return parse['films']
        

    def __getitem__ (self, name):
    
        if name == 'name':
            return name
            
        if name == 'password':
			return password
            
        if name == 'ccard':
			return ccard
            
        if name == 'balance':
			return balance

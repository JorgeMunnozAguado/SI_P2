import os
import sys
import json
import time
import datetime
from utilficheros import jsonAPelicula, resultadoPeliculas, searchFilms

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
                
                file = open(FOLDER_PATH + name + "/films.json", "w")
                file.write('{"films":[]}')
                
                file = open(FOLDER_PATH + name + "/info.json", "w")
                file.write('{"name":"' + name + '","password":"' + password + '","ccard":"' + ccard + '","balance":"' + balance + '","email":"' + email + '"}')
                
                return Users(name, password, ccard, balance, email)
                
            else: return None
            
    @staticmethod
    def updateUser(user):
        
            if os.path.exists(FOLDER_PATH + user.name):
                
                file = open(FOLDER_PATH + user.name + "/info.json", "w")
                file.write('{"name":"' + user.name + '","password":"' + user.password + '","ccard":"' + user.ccard + '","balance":"' + user.balance + '","email":"' + user.email + '"}')
                
                return user
                
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
    def buyFilm(user, basket):
        
        if user is None:
            return False
            
        file = open(FOLDER_PATH + user.name + "/films.json", "r")
        
        parse = json.loads(file.read())
        
        obj = json.loads(basket)
        buscar = obj["films"]
        
        films = searchFilms(buscar)
        f = []
        
        if films[1] > user.balance:
            return False
        
        user.balance = str(float(user.balance) - float(films[1])) 
        
        Users.updateUser(user)
        
        for film in films[0]:
        
            #if Users.isFilmBuy(user, film) == False:
            #    aux = True
            #    f.append({"name":film.titulo, "precio":film.precio})
            f.append({"name":film.titulo, "price":film.precio})

        #if aux == False:
        #    return False

        purchase = {"purchase":str(datetime.datetime.now()), "date":time.strftime("%d/%m/%y"), "price":films[1], "films":f}
        
        parse['films'].append(purchase)
        #print >>sys.stderr, parse
        file = open(FOLDER_PATH + user.name + "/films.json", "w")
        
        file.write(json.dumps(parse))
            
        return True
        
    
    @staticmethod
    def isFilmBuy(user, film):
        
        file = open(FOLDER_PATH + user.name + "/films.json", "r")
        
        parse = json.loads(file.read())
        
        for purchase in parse["films"]:
        
            for peli in purchase["films"]:
            
                if peli['name'] == film.titulo:
                    return True
        
        return False
        
    
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

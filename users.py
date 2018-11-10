import os
import sys
import json
import time
import datetime
import md5
from utilficheros import jsonAPelicula, resultadoPeliculas, searchFilms


class Users:

    def __init__(self, name, password, ccard, balance, email):

        self.name = name
        self.password = password
        self.ccard = ccard
        self.balance = balance
        self.email = email

    @staticmethod
    def createNewUser(name, password, ccard, balance, email,rootpath):
        
            if not os.path.exists(os.path.join(rootpath,name)):
            
                os.makedirs(os.path.join(rootpath,name))
                
                file = open(os.path.join(rootpath,name+"/history.json"), "w")
                file.write('{"films":[]}')
                
                m = md5.new()
                m.update(str(password))
                
                file = open(os.path.join(rootpath,name+"/info.json"), "w")
                file.write('{"name":"' + str(name) + '","password":"' + m.hexdigest() + '","ccard":"' + str(ccard) + '","balance":"' + str(balance) + '","email":"' + str(email) + '"}')
                
                return Users(name, password, ccard, balance, email)
                
            else: return None
            
    @staticmethod
    def updateUser(user,rootpath):
        
            if os.path.exists(os.path.join(rootpath,user.name)):
                
                file = open(os.path.join(rootpath,user.name+"/info.json"), "w")
                file.write('{"name":"' + user.name + '","password":"' + user.password + '","ccard":"' + user.ccard + '","balance":"' + user.balance + '","email":"' + user.email + '"}')
                
                return user
                
            else: return None
            
    @staticmethod
    def getUserFromDB(name,rootpath):

        if not os.path.exists(os.path.join(rootpath,name)):
            return None            
        
        file = open(os.path.join(rootpath,name + "/info.json"), "r")
        
        parse = json.loads(file.read())
        
        return Users(parse['name'], parse['password'], parse['ccard'], parse['balance'], parse['email'])
        
    @staticmethod
    def checkUser(name, password,rootpath):

        user = Users.getUserFromDB(name,rootpath)
        
        if not (user is None):
            
            if user.password == password:
                return True
            
        return False
        
        
    @staticmethod
    def buyFilm(user, basket,rootpath,site_root):
        
        if user is None:
            return False
            
        file = open(os.path.join(rootpath,user.name + "/history.json"), "r")
        
        parse = json.loads(file.read())
        
        obj = json.loads(basket)
        buscar = obj["films"]
        
        films = searchFilms(buscar,site_root)
        f = []
        
        if films[1] > user.balance:
            return False
        
        if (float(user.balance) - float(films[1])) < 0:
            return False
        
        user.balance = str(float(user.balance) - float(films[1])) 
        
        Users.updateUser(user,rootpath)
        
        for film in films[0]:
        
            #if Users.isFilmBuy(user, film) == False:
            #    aux = True
            #    f.append({"name":film.titulo, "precio":film.precio})
            f.append({"name":film["titulo"], "price":film["precio"], "number":film["number"]})

        #if aux == False:
        #    return False

        purchase = {"purchase":str(datetime.datetime.now()), "date":time.strftime("%d/%m/%y"), "price":films[1], "films":f}
        
        parse['films'].append(purchase)
        #print >>sys.stderr, parse
        file = open(os.path.join(rootpath,user.name + "/history.json"), "w")
        
        file.write(json.dumps(parse))
            
        return True
        
    
    @staticmethod
    def isFilmBuy(user, film,rootpath):
        
        file = open(os.path.join(rootpath,user.name + "/history.json"), "r")
        
        parse = json.loads(file.read())
        
        for purchase in parse["films"]:
        
            for peli in purchase["films"]:
            
                if peli['name'] == film.titulo:
                    return True
        
        return False
        
    
    @staticmethod
    def listUserFilms(userName,rootpath):

        user = Users.getUserFromDB(userName,rootpath)
        
        if user is None:
            return None
            
        file = open(os.path.join(rootpath,userName + "/history.json"), "r")
        
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


import os

FOLDER_PATH = "/users/"

class Users:

	def __init__(name, password, ccard, balance):
    
		self.name = name
        self.password = password
        self.ccard = ccard
        self.balance = balance


    def createNewUser(name, password, ccard, balance):
    
        if not os.path.exists(FOLDER_PATH + name):
        
            os.makedirs(FOLDER_PATH + name)
            return Users(name, password, ccard, balance)
            
        else: return None
        

    def getUserFromDB(name):
    
        if not os.path.exists(FOLDER_PATH + name):
            return None            
        
        file = open(FOLDER_PATH + name + "/info.json", "r")
        
        parse = json.loads(file.read())
        
        return User(parse['name'], parse['password'], parse['ccard'], parse['balance'])
        
        
	def __getitem__ (self, type):
    
		if type == 'name':
			return name
		
        elif type == 'password':
			return password
            
        elif type == 'ccard':
			return ccard
            
        elif type == 'balance':
			return balance
            
        

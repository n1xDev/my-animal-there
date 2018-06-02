import json
### ------------------------------------- ###
users = []
with open('db/users.json') as data_file:
	users = json.loads(data_file.read())
parks = []
with open('db/parks.json') as data_file:
	parks = json.loads(data_file.read())
animals = []
with open('db/animals.json') as data_file:
	animals = json.loads(data_file.read())
### ------------------------------------- ###

class Users(object):
	@classmethod
	def regMe(self, login, password, email, phone):
		if users != []:
			i = 0
			while i < len(users['users']):
				if users['users'][i][1] == login:
					return "user_err"
				i += 1
			new_user = [login, password, email, phone]
			users['users'].append(new_user)
			file = open("db/users.json","w")
			json.dump(users ,file, indent=4)
			return "ok"
		else:
			return "db_err"

class Parks(object):
	def getAll(self):
		res = []
		i = 0
		while i < len(parks['parks']['usa']):
			res.append(parks['parks']['usa'][i])
			i += 1
		if res == []:
			return "nothing"
		return res

class Animals(object):
	def getAll(self):
		res = []
		i = 0
		while i < len(animals['animals']):
			res.append(animals['animals'][i])
			i += 1
		if res == []:
			return "nothing"
		return res
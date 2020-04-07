from time import sleep

class Users():
	
	def __init__(self, name_of_network='TestNetWork'):
		self.name_of_network = name_of_network
		self.u_d_f = "users_data_2.txt"
		self.users_data_dict = {}
		
	def start_page(self):
		print("Hello, new User, welcome to " + "'" + self.name_of_network + "'.")
		account = input("Do you have an account?(enter 'y' or 'n') ")
		account = account.lower()
		if account == 'y':
			self.log_in()
		elif account == 'n':
			register = input("Do you want to register in our network?(enter 'y' or 'n') ")
			register = register.lower()
			if register == 'y':
				self.register_new_user()
			elif register == 'n':
				print("Ok. If you change your mind, come to us again!")
	
	def register_new_user(self):
			print("Ok let is starts registration!")
			self.name = input("Enter your first AND second name(You can write nickname as well): ")
			self.age = input("Enter your age: ")
			self.email = input("Enter your Email: ")
			self.phone = input("Enter your number phone: ")
			sleep(1)
			self.identical_data_verification()
			
	def identical_data_verification(self):
		with open(self.u_d_f) as users_data_file:
			readfile = users_data_file.read()
			if self.email in readfile or self.phone in readfile:
				print("Email: " + "'" + self.email + "'" + " or " + "Number phone: " + "'" + self.phone + "'" + " already registered!")
			else:
				self.database_entry()
				
	def database_entry(self):
		with open(self.u_d_f, 'a') as users_data_file:
			self.users_data_dict = {'Name':self.name.title(), 'Age':self.age, 'Email':self.email, 'Number phone':self.phone}
			users_data_file.write(str(self.users_data_dict) + "\n")
			print("\n" + "You was successfully registered on site!")
		
	def log_in(self):
		attempts = 3
		start = True
		while start:
			self.phone_log = input("Enter your phone: ")
			self.email_log = input("Enter your Email: ")
			with open(self.u_d_f) as users_data_file:
				read = users_data_file.read()
				if self.phone_log in read and self.email_log in read:
					sleep(1)
					print("\n" + "Welcome on site!" + "\n")
					self.show_data()
					break
				else:
					if attempts != 0:
						sleep(1)
						try_again = input("\n" + "ERROR! Invalid data was entered! Try again!(enter 'y' or 'n') ")
						try_again = try_again.lower()
						if try_again == 'y':
							print("You have a " + str(attempts) + " attempts for log in!")
							attempts -= 1
							continue
						elif try_again == 'n':
							break
					elif attempts == 0:
						start = False
						print("You used all three attempts for log in. Try again in 30 minutes!")
					
	def show_data(self):
		with open(self.u_d_f) as users_data_file:
			readlinesdata = users_data_file.readlines()
			for l in readlinesdata:
				if self.phone_log in l and self.email_log in l:
					print(l)
				else:
					None
			
users = Users()
users.start_page()


class Admins(Users):
	
	def __init__(self, name_of_network='TestNetWork'):
		super().__init__(name_of_network)
		self.admins_data = {}
		self.a_d_f = "admins_data_2.txt"

	def admins_start_page(self):
		print("Hello, new Admin, welcome to " + "'" + self.name_of_network + "'.")
		account = input("Do you have an account?(enter 'y' or 'n') ")
		account = account.lower()
		if account == 'y':
			self.log_in()
		elif account == 'n':
			register = input("Do you want to register in our network?(enter 'y' or 'n') ")
			register = register.lower()
			if register == 'y':
				self.register_new_user()
			elif register == 'n':
				print("Ok. If you change your mind, come to us again!")
	
	def register_new_user(self):
		print("Ok let is starts registration!")
		self.name = input("Enter your first AND second name(You can write nickname as well): ")
		self.age = input("Enter your age: ")
		self.email = input("Enter your Email: ")
		self.phone = input("Enter your number phone: ")
		sleep(1)
		self.identical_data_verification()
			
	def identical_data_verification(self):
		with open(self.a_d_f) as admins_data_file:
			readfile = admins_data_file.read()
			if self.email in readfile or self.phone in readfile:
				print("Email: " + "'" + self.email + "'" + " or " + "Number phone: " + "'" + self.phone + "'" + " already registered!")
			else:
				self.database_entry()
	
	def database_entry(self):
		with open(self.a_d_f, 'a') as admins_data_file:
			self.admins_data = {'Name':self.name.title(), 'Age':self.age, 'Email':self.email, 'Number phone':self.phone}
			admins_data_file.write(str(self.admins_data) + "\n")
			print("\n" + "You was successfully registered on site!")
		
	def log_in(self):
		attempts = 3
		start = True
		while start:
			self.phone_log = input("Enter your phone: ")
			self.email_log = input("Enter your Email: ")
			with open(self.a_d_f) as admins_data_file:
				read = admins_data_file.read()
				if self.phone_log in read and self.email_log in read:
					sleep(1)
					print("\n" + "Welcome on site!" + "\n")
					self.show_data()
					self.actions_of_admins()
					start = False
				else:
					if attempts != 0:
						sleep(1)
						try_again_admin = input("\n" + "ERROR! Invalid data was entered! Try again!(enter 'y' or 'n') ")
						try_again_admin = try_again_admin.lower()
						if try_again_admin == 'y':
							print("You have a " + str(attempts) + " for log in!")
							attempts -= 1
							continue
						elif try_again_admin == 'n':
							break
					elif attempts == 0:
						start = False
						print("You used all three attempts for log in!Try again in 30 minutes")
				
	def actions_of_admins(self):
		start = True
		while start:
			statistic = input("What actions about users do you want to do ? (enter 's' for 'search user'/'w' to 'watch statistic data'/'x' for 'exit': ")
			statistic = statistic.lower()
			if statistic == 'w':
				sleep(1)
				self.watch_statistic_of_users()
			elif statistic == 's':
				what_user = input("How do you want search user ? (enter 'n' for 'number search'/'t' for 'telephone search'/'e' for 'email search': ")
				what_user = what_user.lower()
				if what_user == 'n':
					self.search_number_user()
				elif what_user == 't':
					self.search_number_phone_user()
				elif what_user == 'e':
					self.email_search()
			elif statistic == 'x':
				start = False
				
	def watch_statistic_of_users(self):
		with open(self.u_d_f) as users_data_file:
			read = users_data_file.readlines()
			print(str(len(read)) + " users registered at the moment" + "\n")
			for l in read:
				print(l)
			self.actions_of_admins()
				
	def search_number_user(self):
		start = True
		while start:
			try:
				number_user = int(input("Enter a number user:(enter '-1' for exit) "))
			except ValueError:
				print("You can enter only a number user(not string)!")
				continue
			else:
				with open(self.u_d_f) as users_data_file:
					read_lines = users_data_file.readlines()
					for n, l in enumerate(read_lines):
						if number_user == n:
							sleep(1)
							print(l)
							continue
						elif number_user == -1:
							start = False
							self.actions_of_admins()
						elif number_user > len(read_lines):
							print("We have only " + str(len(read_lines)) + " users!")
							break
					
	def search_number_phone_user(self):
		start = True
		while start:
			self.tel_user = input("Enter a telephone number of user(enter '-1' for exit): ")
			with open(self.u_d_f) as users_data_file:
				read_data_file = users_data_file.read()
				if str(self.tel_user) in read_data_file:
					self.data_information_by_tel_number()
				elif str(self.tel_user) == '-1':
					start = False
					self.actions_of_admins()
				else:
					self.not_registered_number_phone()
					continue
				
	def data_information_by_tel_number(self):
		with open(self.u_d_f) as users_data_file:
			read_data_lines = users_data_file.readlines()
			for line in read_data_lines:
				if str(self.tel_user) in line:
					print(line)
				else:
					None
				
	def not_registered_number_phone(self):
		with open(self.u_d_f) as users_data_file:
			read_data = users_data_file.read()
			if str(self.tel_user) not in read_data:
				print("Number telephone: " + "'" + str(self.tel_user) + "'" + " not registered!")
			else:
				None
				
	def email_search(self):
		start = True
		while start:
			self.enter_email = input("Enter an email of user(enter '-1' for exit): ")
			with open(self.u_d_f) as users_data_file:
				read_file = users_data_file.read()
				if self.enter_email in read_file:
					self.data_information_by_email()
					continue
				elif self.enter_email == '-1':
					start = False
					self.actions_of_admins()
				else:
					print("Email " + "'" + str(self.enter_email) + "'" + " not registered!")
					continue
					
	def data_information_by_email(self):
		with open(self.u_d_f) as users_data_file:
			read_file_lines = users_data_file.readlines()
			for line in read_file_lines:
				if self.enter_email in line:
					print(line)
				else:
					None
		
	def show_data(self):
		with open(self.a_d_f) as admins_data_file:
			readlinesdata = admins_data_file.readlines()
			for l in readlinesdata:
				if self.phone_log in l and self.email_log in l:
					print(l)
				else:
					None
			
admins = Admins()
admins.admins_start_page()
		
			

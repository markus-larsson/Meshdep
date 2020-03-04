import mysql.connector

class Database:
	def __init__(self, ip, port, user, password, database):
		self.IP = ip
		self.PORT = port
		self.DB = database
		self.USER = user
		self.PASS = password

		try:
			self.CONN = mysql.connector.connect(
				user=self.USER, 
				password=self.PASS,
				host=self.IP,
				port = self.PORT,
				database=self.DB)
		except:
			kill(self)
			print("[DB] Connection failed.")

	def __repr__(self):
		return """IP: %s PORT: %s DB: %s""" % (self.IP, self.PORT, self.DB)

	def __del__(self):
		try:
			CONN.close()
		except:
			pass

	def queryFileAddition(self):
		# this function should query the database
		# to add relevant information about
		# the file that is being added to a node
		# should only be called after the node successfully
		# retrieved data.
		pass

	def queryFileDeletion(self):
		# this function should query the database
		# to delete the relevant file.
		pass

	def queryFileMove(self):
		# this function should query the database to
		# alter the path of a file.
		pass

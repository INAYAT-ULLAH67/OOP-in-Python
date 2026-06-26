class Database:
    def connect(self):
        raise NotImplementedError("Subclasses must implement this method!")

class MySQLDatabase(Database):
    def connect(self):
        return "Connecting to MySQL database on port 3306... "

class OracleDatabase(Database):
    def connect(self):
        return "Initializing Oracle Row-by-Row streaming connection... "
    
mySalObj=MySQLDatabase()
OracleObj=OracleDatabase()
print(mySalObj.connect())
print(OracleObj.connect())
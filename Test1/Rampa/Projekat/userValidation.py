import sqlite3
import hashlib

def validation(username, password):
    connection = sqlite3.connect('baza.db')
    cursor = connection.cursor()

    command = "SELECT EXISTS(SELECT 1 FROM korisnici WHERE username = '%s' LIMIT 1);" % (username)
    test = cursor.execute(command)
    testValue = test.fetchone()

    if (testValue[0] == 1):
        command = "SELECT password FROM korisnici WHERE username = '%s' LIMIT 1" % (username)
        test = cursor.execute(command)
        testValue = test.fetchone()
        passwordHash = hashlib.sha256(password.encode('utf8')).hexdigest()
 
        if (passwordHash == testValue[0]):
            connection.close()
            return '1'
        else:
            connection.close()
            return 'Greska'
        
    else:
        connection.close()
        return '0'

if __name__ == "__main__":
    print(validation("bogDAN","abcde"))

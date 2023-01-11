import sqlite3
import hashlib

def showPhoneNumbers(username):
    connection = sqlite3.connect('baza.db')
    cursor = connection.cursor()

    command = "SELECT broj FROM telefoni WHERE username = '%s';" % (username)
    value = cursor.execute(command)
    x = value.fetchall()
    print(x)
    return x

def insertPhone(username, phoneNumber):
    connection = sqlite3.connect('baza.db')
    cursor = connection.cursor()
    
    message = "1"
    command = "SELECT EXISTS(SELECT 1 FROM telefoni WHERE broj='%s' LIMIT 1);" % (phoneNumber)
    test = cursor.execute(command)
    testValue = test.fetchone()
    
    if (testValue[0] == 0):
        try:
            command = "INSERT INTO telefoni VALUES ('%s','%s');" % (phoneNumber, username)
            cursor.execute(command)
            connection.commit()
        except:
            message = "0"
        finally:
            connection.close()
            return message
    else:
        connection.close()
        return "-1"
    
def removePhone(username, phoneNumber):
    connection = sqlite3.connect('baza.db')
    cursor = connection.cursor()
    
    message = "Uspesno obrisan broj telefona %s za korisnika %s" % (phoneNumber, username)
    command = "SELECT EXISTS(SELECT * FROM telefoni WHERE broj='%s');" % (phoneNumber)
    test = cursor.execute(command)
    testValue = test.fetchone()
    
    if (testValue[0] == 1):
        try:
            command = "DELETE FROM telefoni WHERE broj='%s';" % (phoneNumber)
            cursor.execute(command)
            connection.commit()
        except:
            message = "Greska"
        finally:
            connection.close()
            return message
    else:
        connection.close()
        return "Broj ne postoji u bazi"
               
def changeUsername(username, newUsername):
    connection = sqlite3.connect('baza.db')
    cursor = connection.cursor()

    message = "1"

    try:
        command = "UPDATE korisnici SET username = '%s' WHERE username = '%s';" % (newUsername, username)
        cursor.execute(command)
        command = "UPDATE telefoni SET username = '%s' WHERE username = '%s';" % (newUsername, username)
        cursor.execute(command)
        connection.commit()
    except:
        message = "0"
    finally:
        connection.close()
        return message

def changePassword(username, newPassword):
    connection = sqlite3.connect('baza.db')
    cursor = connection.cursor()
    message = "1"

    try:
        newPassword = hashlib.sha256(newPassword.encode('utf8')).hexdigest()
        command = "UPDATE korisnici SET password = '%s' WHERE username = '%s';" % (newPassword, username)
        cursor.execute(command)
        connection.commit()
    except:
        message = "0"
    finally:
        connection.close()
        return message

if __name__ == "__main__":
    changeUsername("bogdan","bogDAN")
    changePassword("bogDAN","abcd")
    print(showPhoneNumbers("bogDAN"))

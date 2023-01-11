import sqlite3
import hashlib

def changeUsername(username, newUsername):
    connection = sqlite3.connect('baza.db')
    cursor = connection.cursor()

    message = "Uspesno promenjen username sa %s na %s" % (username, newUsername)

    try:
        command = "UPDATE admini SET username = '%s' WHERE username = '%s';" % (newUsername, username)
        cursor.execute(command)
        connection.commit()
    except:
        message = "Greska"
    finally:
        connection.close()
        return message

def changePassword(username, newPassword):
    connection = sqlite3.connect('baza.db')
    cursor = connection.cursor()
    message = "Uspesna promena lozinke"

    try:
        newPass = hashlib.sha256(newPassword.encode('utf8')).hexdigest()
        print(newPassword)
        print(newPass)
        command = "UPDATE admini SET password = '%s' WHERE username = '%s';" % (newPass,username)
        cursor.execute(command)
        connection.commit()
    except:
        message = "Greska"
    finally:
        connection.close()
        return message

if __name__ == "__main__":
    changePassword("bogdan","abcde")

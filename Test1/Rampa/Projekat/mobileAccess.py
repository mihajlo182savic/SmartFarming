import sqlite3
import datetime

def access(phoneNumber):
    connection = sqlite3.connect('baza.db')
    cursor = connection.cursor()

    command = "SELECT EXISTS(SELECT 1 FROM telefoni WHERE broj = '%s' LIMIT 1);" % (phoneNumber)
    test = cursor.execute(command)
    testValue = test.fetchone()
    connection.close()
    
    if (testValue[0] == 1):
        try:
            connection = sqlite3.connect('archive/%s.db' % (str(datetime.date.today())))
            cursor = connection.cursor()
            timestamp = str(datetime.datetime.now().time().strftime('%H:%M'))

            command = "INSERT INTO telefon (time,number) VALUES ('%s','%s');" % (timestamp,phoneNumber)
            cursor.execute(command)

            connection.commit()
            connection.close()
            return '1'
        except:
            connection.close()
            return 'Greska'
    else:
        return '0'
    
if __name__ == "__main__":
    print(access("+381645350634"))
    

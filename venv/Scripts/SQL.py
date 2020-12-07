import mysql-connector

mydb = mysql.connector.connect(host='localhost', user='root', passwd='mysql1234')

mycu = mydb.cursor()
mycu.execute('show databases')



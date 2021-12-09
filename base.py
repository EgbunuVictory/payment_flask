import mysql.connector

mybase = mysql.connector.connect(
    host = 'localhost',
    database = 'payment',
    user = 'root',
    password = ''
)

mycursor = mybase.cursor(dictionary=True)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS students(
        ID INT NOT NULL AUTO_INCREMENT,
        stu_name VARCHAR(255),
        stu_id VARCHAR(255),
        stu_gender VARCHAR(255),
        dept VARCHAR(255),
        PRIMARY KEY(ID)
    )"""
)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS pay(
        name VARCHAR(255) NOT NULL,
        bank_name VARCHAR(255) NOT NULL,
        account_number INT NOT NULL,
        amount INT NOT NULL,
        purpose VARCHAR(255) NOT NULL,
        pay_id INT references students(ID)
    )"""
)
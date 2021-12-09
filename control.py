from flask import Flask, render_template, request, redirect
from base import mybase, mycursor


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('ppp.html')

@app.route('/adminLogin', methods=['GET','POST'])
def adminLogin():
    message = ''
    username = 'victory'
    password = 'egbunu'
    if request.method == 'GET':
        return render_template('adminLogin.html')
    if request.method == 'POST':
        username == request.form['username']
        password == request.form['password']
        if username == username and password == password:
            message = 'Correct'
            return render_template("admin.html")
        else:
            message = 'Wrong username or password Try Again'
            return render_template('index.html', message = message)

@app.route('/studentLogin', methods=['GET', 'POST'])
def studentLogin():
    message = ''
    if request.method == 'GET':
        return render_template('studentLogin.html')
    if request.method == 'POST':
        _username = request.form['username']
        _password = request.form['password']
        mycursor.execute(f'SELECT * FROM students WHERE stu_name = "{_username}" and stu_id = "{_password}" ')
        verify = mycursor.fetchone()
        # if verify:
        #     mycursor.execute(f"SELECT * FROM students WHERE ID={verify['ID']}")
        #     student = mycursor.fetchone()
        return render_template('profile.html')
    else:
        message = 'Wrong student name or password Try again'
        return render_template('index.html', message = message)

@app.route('/list')
def List():
    mycursor.execute("SELECT * FROM students")
    students = mycursor.fetchall()
    return render_template('list.html', students = students)

@app.route('/register', methods=['GET', 'POST'])
def Register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        _stu_name = request.form['stu_name']
        _stu_id = request.form['stu_id']
        _stu_gender = request.form['stu_gender']
        _dept = request.form['dept']
        sql = f'INSERT INTO students (stu_name, stu_id, stu_gender, dept) VALUES (%s, %s, %s, %s)'
        val = (_stu_name, _stu_id, _stu_gender, _dept)
        mycursor.execute(sql, val)
        mybase.commit()
        return redirect('/list')

@app.route('/list', methods=['GET', 'POST'])
def view():
    if request.method == 'GET':
        return render_template('list.html')

# @app.route('/payment')
# def Show():
#     mycursor.execute("SELECT * FROM pay")
#     payments = mycursor.fetchall()
#     return render_template("pay_list.html", payments = payments)

@app.route('/payment', methods=['GET', 'POST'])
def Payment():
    if request.method == 'GET':
        return render_template('payment.html')
    if request.method == 'POST':
        _name = request.form['name']
        _bank_name = request.form['bank_name']
        _account_number = request.form['account_number']
        _amount = request.form['amount']
        _purpose = request.form['purpose']
        sql = 'INSERT INTO pay (name, bank_name, account_number, amount, purpose) VALUES (%s, %s, %s, %s, %s)'
        val = (_name, _bank_name, _account_number, _amount, _purpose)
        mycursor.execute(sql, val)
        mybase.commit()
        mycursor.execute("SELECT * FROM pay")
        payments = mycursor.fetchall()
        return render_template('pay_list.html', payments = payments)

@app.route('/payments')
def Payments():
    mycursor.execute("SELECT * FROM pay")
    payments = mycursor.fetchall()
    return render_template('pay_list.html', payments = payments)


if __name__ == '__main__':
    app.run(debug = True)
from flask import Flask, render_template, request, url_for, redirect, flash, session
import mysql.connector
from time import sleep
from date_calc import *

app = Flask(__name__, template_folder="f_templates")
app.secret_key = "77d48e2e153c7796b4bdd39598f9935b6165f26ff8e1eb3b"

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="pfa_orange"
)

cursor = db.cursor()

# Login check decorator
def login_required(f):
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash("Please log in to access this page.", "warning")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

@app.route("/")
def index():
    return render_template('homepage.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        global username
        username = request.form['username']
        password = request.form['password']
        cursor = db.cursor()
        cursor.execute('SELECT User_ID, Pwd, User_name FROM user_details WHERE User_ID = %s', (username,))
        global user
        user = cursor.fetchone()
        print("Retrieved user data:", user)
        if user and user[1] == password:  
            session['username'] = user[2]  
            flash("Login successful!", "success")
            return redirect('/')
        else:
            flash("Invalid username or password.", "danger")
            return redirect(url_for('login'))

@app.route("/logout")
def logout():
    session.pop('username', None)  # Remove username from session
    flash("You have been logged out.", "success")
    return redirect('/')     

@app.route("/schemes")
def schemes():
    return redirect("http://127.0.0.1:3000/schemes")

@app.route("/forgot_pwd", methods=['GET', 'POST'])
def forgot_pwd():
    if request.method == 'GET':
        return render_template('forgot_pwd.html')
    elif request.method == 'POST':
        username = request.form['username']
        new_password = request.form['new_password']
        # Update password in database
        cursor.execute('UPDATE user_details SET pwd = %s WHERE user_id = %s', (new_password, username))
        db.commit()
        return redirect(url_for('login'))
    
@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        # Retrieve form data
        user_id = request.form['user_id']
        name = request.form['name']
        mobile = request.form['mobile']
        email = request.form['email']
        dob = request.form['dob']
        password = request.form['password']
        conf_pwd = request.form['confirm_password']
        acc_number = request.form['acc_number']
        ifsc = request.form['ifsc']
        pan = request.form['pan']
        status = request.form['status']
        acc_type = request.form['acc_type']
        created_on = request.form['created_on']
        if password == conf_pwd:
            # Insert data into the database
            cursor = db.cursor()
            cursor.execute('''INSERT INTO user_details (user_id, user_name, mob, email_id, dob, pwd) VALUES (%s, %s, %s, %s, %s, %s)''', (user_id, name, mobile, email, dob, password))
            cursor.execute('''INSERT INTO account_details (acc_no, ifsc, pan, acc_status, acc_type, acc_create, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s)''', (acc_number, ifsc, pan, status, acc_type, created_on, user_id))
            db.commit()
        else:
            return redirect(url_for('signup'))
        # Redirect to the index page or a success page
        return redirect(url_for('login'))

@app.route("/savings", methods=['GET', 'POST'])
@login_required
def savings():
    if request.method == 'GET':
        return render_template('savings.html')
    if request.method == 'POST':
        trans_id = request.form['trans_id']
        user_id = request.form['user_id']
        scheme_id = request.form['scheme_id']
        amount = request.form['amount']

        print(trans_id)
        cursor = db.cursor()
        query = f"SELECT user_details.Mob, account_details.acc_no, account_details.pan FROM user_details JOIN account_details ON user_details.User_ID = account_details.user_id WHERE user_details.User_ID = {user_id}"
        cursor.execute(query)
        result = cursor.fetchone()
        print(result)
        if result:
            cursor.execute('''SELECT calc_int_amt(%s, %s)''', (amount, scheme_id))
            mat_amt = cursor.fetchone()[0]
            mat_date = maturity_date(int(scheme_id))
            print(mat_date)
            # inv_date=mat_date[0]
            cursor.execute('''INSERT INTO savings_details (user_id_savings, account_number, mobile_number, Scheme_ID, amount, pan, Maturity_Amount, invested_date, Maturity_Date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) ''', (user_id, result[1], result[0], scheme_id, amount, result[2], mat_amt, mat_date[0], mat_date[1]))
            db.commit()
            # cursor = db.cursor()
            # cursor.execute('''INSERT INTO transactions(Transaction_ID, User_ID, Debit_Amount, Debit_Date) VALUES (%s, %s, %s, %s)''', (trans_id, user_id, amount, inv_date))
            # db.commit()
            return redirect(url_for('schemes'))
        else:
            return redirect(url_for("savings"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

# signup ,savings, homepage - Mahika
# schemes, transactions(of specific user), login - Khushi
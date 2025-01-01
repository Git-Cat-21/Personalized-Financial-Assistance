from flask import Flask, render_template, request, url_for, redirect, session, flash
import mysql.connector
from time import sleep
from date_calc import *
import datetime
import matplotlib.pyplot as plt

app = Flask(__name__, template_folder="f_templates")
app.secret_key = "77d48e2e153c7796b4bdd39598f9935b6165f26ff8e1eb3b"

@app.before_request
def initialize_session():
    if 'username' not in session:
        session['username'] = None
    if 'userid' not in session:
        session['userid'] = None

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="pfa_orange"
)

cursor = db.cursor()

def login_required(f):
    def decorated_function(*args, **kwargs):
        if session.get('username') is None or session.get('userid') is None:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

@app.route("/")
def index():
    userid = session.get('userid')
    cursor.execute('SELECT * FROM user_details WHERE User_ID = %s', (userid,))
    query = cursor.fetchall()
    return render_template('homepage.html', query=query)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = db.cursor()
        cursor.execute('SELECT User_ID, Pwd, User_name FROM user_details WHERE User_ID = %s', (username,))
        user = cursor.fetchone()
        if user and user[1] == password:  
            session['username'] = user[2]  
            session['userid'] = user[0]
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))

@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('userid', None)
    return redirect(url_for('index'))

@app.route("/schemes")
def schemes():
    return redirect("http://127.0.0.1:3000/schemes")

@app.route("/graphs",methods=['GET','POST'])
def graphs():
    scheme_id = request.form.get('Scheme_ID')
    amount = request.form.get('Amount')
    duration=int(request.form.get("duration_hide"))
    rate=float(request.form.get("rate_hide"))
    curr_year=int(datetime.datetime.now().year)

    years=[curr_year+x for x in range(duration + 1)]
    curr_amt=int(amount)
    amount_lst=[curr_amt]

    for i in range(1,len(years)):
        curr_amount=((curr_amt*i*rate)/100)+curr_amt
        amount_lst.append(curr_amount)

    plt.plot(years, amount_lst, marker='o', linestyle='-', color='b', label='Investment Value')

    for year, amount in zip(years, amount_lst):
        plt.annotate(f'{year}: {amount:.2f}', xy=(year, amount), xytext=(year, amount + 100))
    plt.title("Investment Growth Over Time")
    plt.xlabel("Years")
    plt.ylabel("Amount (in rupees)")
    plt.grid(True)
    plt.legend()

    plt.show()

    return redirect("http://127.0.0.1:3000/schemes")

@app.route("/forgot_pwd", methods=['GET', 'POST'])
def forgot_pwd():
    if request.method == 'GET':
        return render_template('forgot_pwd.html')
    elif request.method == 'POST':
        username = request.form['username']
        new_password = request.form['password']  # Changed to match form field 'password'
        
        # Update the user's password in the database
        cursor.execute('UPDATE user_details SET Pwd = %s WHERE User_Id = %s', (new_password, username))
        db.commit()
        
        return redirect(url_for('login'))

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    if request.method == "GET":
        return render_template("admin.html")
    elif request.method == "POST":
        admin_name = request.form['admin_name']
        password = request.form['pass_wd']
        user_id = request.form['user_id']
        cursor = db.cursor()
        cursor.execute("SELECT password FROM admin WHERE admin_name = %s", (admin_name,))
        values = cursor.fetchone()

        if values and values[0] == password:
            cursor = db.cursor()
            cursor.execute("DELETE FROM SAVINGS_DETAILS WHERE User_ID_savings = %s", (user_id,))
            db.commit()
            cursor = db.cursor()
            cursor.execute("DELETE FROM user_details WHERE User_ID = %s", (user_id,))
            db.commit()
            return render_template("admin.html")
        else:
            return render_template("homepage.html")
        
@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
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
            cursor = db.cursor()
            cursor.execute('''INSERT INTO user_details (user_id, user_name, mob, email_id, dob, pwd) VALUES (%s, %s, %s, %s, %s, %s)''', (user_id, name, mobile, email, dob, password))
            cursor.execute('''INSERT INTO account_details (acc_no, ifsc, pan, acc_status, acc_type, acc_create, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s)''', (acc_number, ifsc, pan, status, acc_type, created_on, user_id))
            db.commit()
        else:
            return redirect(url_for('signup'))
        return redirect(url_for('login'))
    
@app.route("/savings", methods=['GET', 'POST'])
@login_required
def savings():
    if request.method == 'GET':
        return render_template('savings.html')
    elif request.method == 'POST':
        trans_id = request.form['trans_id']
        user_id = request.form['user_id']
        scheme_id = request.form['scheme_id']
        amount = request.form['amount']

        cursor.execute(f'''
            SELECT user_details.Mob, account_details.acc_no, account_details.pan 
            FROM user_details 
            JOIN account_details 
            ON user_details.User_ID = account_details.user_id 
            WHERE user_details.User_ID = %s
        ''', (user_id,))
        result = cursor.fetchone()
        
        if result:
            cursor.execute('SELECT calc_int_amt(%s, %s)', (amount, scheme_id))
            mat_amt = cursor.fetchone()[0]
            mat_date = maturity_date(int(scheme_id))
            
            cursor.execute('''
                INSERT INTO savings_details 
                (user_id_savings, account_number, mobile_number, Scheme_ID, amount, pan, Maturity_Amount, invested_date, Maturity_Date) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (user_id, result[1], result[0], scheme_id, amount, result[2], mat_amt, mat_date[0], mat_date[1]))
            
            db.commit()
            
            cursor.execute('''
                INSERT INTO transactions
                (Transaction_ID, User_ID, Debit_Amount, Debit_Date, Credit_Amount, Credit_Date) 
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (trans_id, user_id, amount, mat_date[0], mat_amt, mat_date[1]))
            
            db.commit()
            return redirect(url_for('schemes'))
        else:
            return redirect(url_for("savings"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
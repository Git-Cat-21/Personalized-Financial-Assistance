from flask import Flask,render_template,request,url_for,redirect, flash, session
import mysql.connector

#what is secret key used for check??
app=Flask(__name__,template_folder="f_templates")
app.secret_key = "77d48e2e153c7796b4bdd39598f9935b6165f26ff8e1eb3b"

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="pfa_orange"
)

cursor = db.cursor()

@app.route("/")
def index():
    return render_template('homepage.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = db.cursor()
        cursor.execute('SELECT User_ID, Pwd, User_name FROM user_details WHERE User_ID = %s', (username,))
        user = cursor.fetchone()
        print("Retrieved user data:", user)
        if user and user[1] == password:  
            session['username'] = user[2]  
            flash("Login successful!", "success")
            return redirect(url_for('index'))
        else:
            flash("Invalid username or password.", "danger")
            return redirect(url_for('login'))

@app.route("/logout")
def logout():
    session.pop('username', None)  # Remove username from session
    flash("You have been logged out.", "success")
    return redirect(url_for('index'))     
    
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
        acc_number = request.form['acc_number']
        ifsc = request.form['ifsc']
        status = request.form['status']
        acc_type = request.form['acc_type']
        created_on = request.form['created_on']
        
        # Insert data into the database
        cursor = db.cursor()
        cursor.execute('''INSERT INTO user_details (user_id, user_name, mob, email_id, dob, pwd) VALUES (%s, %s, %s, %s, %s, %s)''', (user_id, name, mobile, email, dob, password))
        cursor.execute('''INSERT INTO account_details (acc_no, ifsc, acc_status, acc_type, acc_create, user_id) VALUES (%s, %s, %s, %s, %s, %s)''', (acc_number,ifsc,status,acc_type,created_on,user_id))
        db.commit()
        
        # Redirect to the index page or a success page
        return redirect(url_for('login'))

@app.route("/savings",methods=['GET','POST'])
def savings():
    if request.method=='GET':
        return render_template('savings.html')
    if request.method=='POST':
        user_id = request.form['user_id']
        acc_no = request.form['acc_no']
        mobile = request.form['mobile']
        scheme_id = request.form['scheme_id']
        amount = request.form['amount']
        pan = request.form['pan']
        inv_date = request.form['inv_date']
        cursor=db.cursor()
        cursor.execute('''INSERT INTO savings_details (user_id_savings,account_number,mobile_number,Scheme_ID,amount,pan,invested_date) VALUES (%s, %s, %s, %s, %s, %s, %s) ''',(user_id, acc_no,mobile,scheme_id,amount,pan,inv_date))
        db.commit()

        # flash ("Correct go in")
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

#signup ,savings, homepage - Mahika
# schemes, transactions(of specific user), login - Khushi
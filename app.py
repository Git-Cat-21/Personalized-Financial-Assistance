from flask import Flask,render_template,request,url_for,redirect
import mysql.connector

#what is secret key used for check??

app=Flask(__name__,template_folder="f_templates")

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

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        #print(username,password)
        # cursor=db.cursor()
        # cursor.execute('INSERT INTO user_details (username, password) VALUES (%s, %s)',(username,password))
        # db.commit()

        # flash ("Correct go in")
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
        return redirect(url_for('index'))

@app.route("/savings",methods=['GET','POST'])
def savings():
    if request.method=='GET':
        return render_template('savings.html')
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']

        cursor=db.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)',(username,password))
        db.commit()

        # flash ("Correct go in")
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

#signup ,savings, homepage - Mahika
# schemes, transactions(of specific user), login - Khushi
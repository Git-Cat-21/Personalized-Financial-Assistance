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

@app.route("/signup",methods=['GET','POST'])
def signup():
    if request.method=='GET':
        return render_template('signup.html')
    if request.method=='POST':
        data=request.get_json()
        user_id = data.get("userId")
        name=request.form['name']
        mob=request.form['mobile']
        email=request.form['email']
        dob=request.form['dob']
        password=request.form['password']
        cursor=db.cursor()
        cursor.execute('INSERT INTO user_details VALUES (%s, %s, %s, %s, %s, %s)',(user_id, name, mob, email, dob, password))
        db.commit()

        # flash ("Correct go in")
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
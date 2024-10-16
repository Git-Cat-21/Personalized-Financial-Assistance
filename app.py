from flask import Flask,render_template,request

app=Flask(__name__,template_folder="f_templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return "Hii"
    elif request.method == 'POST':
        pass

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
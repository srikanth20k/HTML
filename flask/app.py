from flask import Flask,render_template,request,redirect,url_for,session
from datetime import timedelta

app = Flask(__name__)
users= [{"srikanth":"srikanth@012"},{"sudheer":"srikanth@0123"},{"sai":"srikanth@0124"}  ]
app.secret_key="your secrete key"
app.permanent_session_lifetime=timedelta(minutes=5)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method=="POST":
        username =request.form['username']
        password =request.form['password']
        user_exists=False
        for user in users:
            if username in user:
                user_exists=True
                if user[username]==password:
                    session.permanent=True
                    session["user"]=username
                    return redirect(url_for('index'))
                else:
                    return "invalid details try again with correct details"
        if not user_exists:
            return "user does not exist"
    elif"user" in session:
        return redirect(url_for('index'))
    return render_template("login.html")
# app.add_url_rule("/login","login",login)

    
@app.route('/logout',methods=['POST'])
def logout():
    session.pop("user",None)
    return redirect(url_for('login'))
    
    
    
if __name__=='__main__':
    app.run(debug=True)
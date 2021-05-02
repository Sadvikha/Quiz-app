from flask import Flask, render_template, redirect, url_for, session, request,flash
from flask_mysqldb import MySQL
import MySQLdb
import mysql.connector


app = Flask(__name__)
app.secret_key = "1234353234"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Revanth_22"
app.config["MYSQL_DB"] = "quiz"

db = MySQL(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if 'Email' in request.form and 'password' in request.form:
            Email = request.form['Email']
            password = request.form['password']
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("SELECT * FROM logininfo WHERE Email=%s AND Password= %s", (Email,password))
            info = cursor.fetchone()
            if info is not None:
                if info['Email'] == Email and info['Password'] == password:
                    session['loginsuccess'] = True
                    return redirect(url_for('home'))

            else:
                return redirect(url_for('login'))
                #return redirect(url_for('index'))


    return render_template("login.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        if "one" in request.form and "two" in request.form and "three" in request.form:
            username = request.form['one']
            email = request.form['two']
            password = request.form['three']
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("INSERT INTO quiz.logininfo(Name, Password, Email)VALUES(%s,%s,%s)",(username,password,email))
            db.connection.commit()
            flash('You were successfully Signed Up')
            return redirect(url_for('login'))



    return render_template("signup.html")



@app.route('/')
def index():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/easy')
def easy():
    return render_template("easy.html")

@app.route('/medium')
def medium():
    return render_template("medium.html")

@app.route('/hard')
def hard():
    return render_template("hard.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/baselogout')
def baselogout():
    return render_template("baselogout.html")

@app.route('/politics')
def politics():
    return render_template("politics.html")

@app.route('/sports')
def sports():
    return render_template("sports.html")

@app.route('/heritage')
def heritage():
    return render_template("heritage.html")


'''
@app.route('/easyquiz')
def easyquiz():
    return render_template("easyquiz.html")
    
'''

@app.route('/easyquiz1')
def easyquiz1():
    return render_template("easyquiz1.html")




@app.route('/easyquiz2')
def easyquiz2():
    return render_template("easyquiz2.html")


@app.route('/easyquiz3')
def easyquiz3():
    return render_template("easyquiz3.html")



@app.route('/easyquiz4')
def easyquiz4():
    return render_template("easyquiz4.html")


@app.route('/easyquiz5')
def easyquiz5():
    return render_template("easyquiz5.html")







@app.route('/easyresult')
def easyr():
    return render_template("easyresult.html")



@app.route('/mediumquiz')
def mediumquiz():
    return render_template("mediumquiz.html")


@app.route('/mediumresult')
def mediumr():
    return render_template("mediumresult.html")

@app.route('/hardquiz')
def hardquiz():
    return render_template("hardquiz.html")

@app.route('/hardresult')
def hardr():
    return render_template("hardresult.html")

@app.route('/politicsquiz')
def politicsquiz():
    return render_template("politicsquiz.html")

@app.route('/politicsresult')
def politicsr():
    return render_template("politicsresult.html")


@app.route('/sportsquiz')
def sportsquiz():
    return render_template("sportsquiz.html")

@app.route('/sportsresult')
def sportsr():
    return render_template("sportsresult.html")

@app.route('/heritagequiz')
def heritagequiz():
    return render_template("heritagequiz.html")

@app.route('/heritageresult')
def heritager():
    return render_template("heritageresult.html")





'''
@app.route('/logout')
def logout():
    session.pop('loginsuccess', None)
    return render_template("login.html")


@app.route('/homeloggedin')
def homelin():
    if session['loginsuccess'] == True:
        return render_template('homeloggedin.html')


@app.route('/aboutloggedin')
def aboutlin():
    if session['loginsuccess'] == True:
        return render_template('aboutloggedin.html')

@app.route('/contactloggedin')
def contactlin():
    if session['loginsuccess'] == True:
        return render_template('contactloggedin.html')
'''

if __name__ == '__main__':
    app.run(debug=True)
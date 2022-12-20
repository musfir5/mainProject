from flask import *
from src.dbconnection import *
#from datetime import datetime
app = Flask(__name__)
app.secret_key="anshid"



@app.route("/", methods=['get', 'post'])  # for loading login page
def main():
    return render_template("aboutus.html")


@app.route("/log",methods=['post','get'])
def log():
    return render_template("index.html")


@app.route("/sign",methods=['post','get'])
def sign():
    return render_template("index.reg.html")


@app.route("/cont",methods=['post','get'])
def cont():
    return render_template("contact.html")


@app.route("/uhome",methods=['post','get'])
def uhome():
    return render_template("userPage.html")


@app.route("/ureg",methods=['post','get'])
def reg():
    return render_template("index.reg.html")


@app.route("/adminProfile",methods=['post','get'])
def adminProfile():
    return render_template("viewUsers.html")


@app.route("/adhome",methods=['post','get'])
def adminPage():
    return render_template("adminPage.html")



@app.route("/login",methods=['post','get'])
def login():
    username=request.form['textfield']
    password=request.form['textfield2']
    qry="SELECT * FROM `login` WHERE `username`=%s AND `password`=%s"
    val=(username,password)
    res=selectone(qry,val)

    if res is None:
        return ''' <script> alert('invalid user name or password');window.location="/log"</script>'''
    elif res['type']=="admin":
        session['lId'] = res['lid']
        return '''<script>alert("welcome admin");window.location="/viewAdmins"</script>'''
    else :
        session['lId'] = res['lid']
        return'''<script>alert("welcome user");window.location="/uhome"</script>'''





@app.route("/urejistration",methods=['post','get'])
def rejistration():
    name = request.form['Name']
    phone = request.form['Ph']
    email = request.form['Email']
    username = request.form['Uname']
    password = request.form['Password']
    confirm_password = request.form['Password1']
    if password==confirm_password:
        qry="INSERT INTO login VALUES(NULL,%s,%s,'user')"
        val=(username,password)
        res=iud(qry,val)
        qry1="INSERT INTO user_reg VALUES(NULL,%s,%s,%s,%s)"
        vall=(str(res),name,phone,email)
        res1=iud(qry1,vall)
        return '''<script>alert("rejistration successfully");window.location="/log"</script>'''
    else:
        return '''<script>alert("password does not match!");window.location="/sign"</script>'''


@app.route("/contact",methods=['post','get'])
def contact():
    name1 = request.form['name1']
    email = request.form['email']
    sub = request.form['sub']
    mess = request.form['mess']
    qry="INSERT INTO contact VALUES(NULL,%s,%s,%s,%s,%s)"
    val=(session['lId'],name1,email,sub,mess)
    res=iud(qry,val)

    return'''<script>alert("Message sended successfully");window.location="/uhome"</script>'''
       
      

@app.route("/adProfile",methods=['post','get'])
def adProfile():
    uname=request.form['uname']
    password = request.form['pass']
    cpassword= request.form['cpass']
    if password == cpassword:
        qry = "INSERT INTO login VALUES(NULL,%s,%s,'admin')"
        val = (uname, password)
        res = iud(qry, val)
        return '''<script>alert("Admin Rejistration successfully");window.location="/viewAdmins"</script>'''
    else:
        return '''<script>alert("password does not match");window.location="/viewAdmins"</script>'''


@app.route("/viewAdmins",methods=['post','get'])
def viewAdmins():
    qry = "SELECT `lid`,`username`,`password` FROM `login` WHERE `type`='admin' AND `lid`='%s'"
    res = selectall2(qry,session['lId'])
    return render_template("adminPage.html",val=res)





















app.run(debug=True)












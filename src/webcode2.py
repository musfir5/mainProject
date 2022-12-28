import smtplib
from flask import *
import os
from src.dbconnection import *
from datetime import datetime
app = Flask(__name__)
app.secret_key="anshid"
import json
from flask_mail import Mail,Message


app.config["MAIL_SERVER"]="smtp.gmail.com"
app.config["MAIL_PORT"]=587


app.config["MAIL_USERNAME"]="elitemot7@gmail.com"
app.config["MAIL_PASSWORD"]="iprddrhiytjekrzv"
app.config["MAIL_USE_TLS"]= True
app.config["MAIL_DEFAULT_SENDER"]="elitemot7@gmail.com"



mail=Mail(app)




@app.route("/", methods=['get', 'post'])  #show 'aboutus' page 
def main():
    return render_template("aboutus.html")



@app.route("/log",methods=['post','get'])   #show 'login' page
def log():
    return render_template("index.html")


@app.route("/sign",methods=['post','get'])  #show 'registration' page
def sign():
    return render_template("index.reg.html")


@app.route("/cont",methods=['post','get'])   #show 'contact' page
def cont():
    return render_template("contact.html")





@app.route("/ureg",methods=['post','get'])
def reg():
    return render_template("index.reg.html")


@app.route("/adminProfile",methods=['post','get'])
def adminProfile():
    return render_template("viewUsers.html")


@app.route("/adhome",methods=['post','get'])
def adminPage():
    return render_template("adminPage.html")

@app.route("/service",methods=['post','get'])  #show service page on user page
def service():
    return render_template("service.html")





@app.route("/login",methods=['post','get'])  # login action
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





@app.route("/urejistration",methods=['post','get'])  # registration action
def rejistration():
    name = request.form['Name']
    phone = request.form['Ph']
    email = request.form['Email']
    username = request.form['Uname']
    password = request.form['Password']
    confirm_password = request.form['Password1']

    #msg=Message("Successfully registered, Name:"+name,recipients=[email])
    #print(msg)
    #mail.send(msg)
    message= Message("Welcome "+name+" To our Elite Yamaha Family",recipients=[email])
    print(message)
    mail.send(message)


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


@app.route("/contact",methods=['post','get'])   # contact page action
def contact():
    name1 = request.form['name1']
    email = request.form['email']
    sub = request.form['sub']
    mess = request.form['mess']
    qry="INSERT INTO contact VALUES(NULL,%s,%s,%s,%s,%s)"
    val=(session['lId'],name1,email,sub,mess)
    res=iud(qry,val)

    return'''<script>alert("Message sended successfully");window.location="/uhome"</script>'''
       
      

@app.route("/adProfile",methods=['post','get']) # add new admin in admin panel
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


@app.route("/viewAdmins",methods=['post','get']) # view admin details on admin page
def viewAdmins():
    qry = "SELECT `lid`,`username`,`password` FROM `login` WHERE `type`='admin' AND `lid`='%s'"
    res = selectall2(qry,session['lId'])
    
    return render_template("adminPage.html",val=res)




@app.route("/viewUsers",methods=['post','get']) # view user details in admin panel
def viewUsers():
    qry="SELECT * FROM `user_reg`"
    res=selectall(qry)
    return render_template("viewUsers.html",val=res)


@app.route("/deleUser",methods=['post','get']) # delete user action in admin panel
def deleUser():
    id=request.args.get('ID')
    qry="DELETE FROM `login` WHERE `lid`=%s"
    val=(id)
    res=iud(qry,val)
    qry="DELETE FROM `user_reg` WHERE `lid`=%s"
    val=(id)
    res=iud(qry,val)
    print(res)
    return '''<script>alert("Deleted successfully.");window.location="/viewUsers"</script>'''


@app.route("/addnewBike",methods=['post','get'])  # add new bike in admin panel
def addnewBike():
    mile=request.form['mile']
    model=request.form['model']
    loc=request.form['loc']
    name=request.form['name']
    price=request.form['price']
    desc=request.form['desc']
    img=request.files['img']
    

    fn=datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    img.save("static/bikesImage/"+fn)

    

    qry="INSERT INTO `addbike` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s)"
    val=(mile,model,loc,name,price,desc,fn)
    res=iud(qry,val)
    return '''<script> alert('Successfully Added');window.location="/addBike"</script>'''


@app.route("/addBike",methods=['post','get']) # show added bikes in admin panel
def addBike():
    qry="SELECT * FROM `addbike`"
    res=selectall(qry)
    return render_template("addBikes.html",val=res)


@app.route("/deleBike",methods=['post','get']) # delete bikes action in admin panel
def deleBike():
    id=request.args.get('ID')
    qry="DELETE FROM `addbike` WHERE `vid`=%s"
    val=(id)
    res=iud(qry,val)    
    return '''<script>alert("Deleted successfully.");window.location="/addBike"</script>'''


@app.route("/editBike",methods=['post','get']) # edit button action in admin panel
def aditBike():
    id=request.args.get('ID')
    session['vid']=id
    qry = "SELECT * FROM `addbike` WHERE vid=%s"
    val=(id)
    res=selectone(qry,val)
    return render_template("/updateBike.html",val=res)


@app.route("/updateBike",methods=['post','get'])  # update bike details action from admin panel
def updateBike():
    mile=request.form['mile']
    model=request.form['model']
    loc=request.form['loc']
    name=request.form['name']
    price=request.form['price']
    desc=request.form['desc']
    img=request.files['img']
   

    fn=datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    img.save("static/bikesImage/"+fn)

    

    qry="UPDATE `addbike` SET `mile`=%s,`model`=%s ,`loc`=%s, `name`=%s ,`price`= %s ,`desc`=%s,`img`=%s where vid=%s"
    val=(mile,model,loc,name,price,desc,fn,session['vid'])
    res=iud(qry, val)
    return '''<script> alert('data Updated');window.location="/addBike"</script>'''



@app.route("/uhome",methods=['post','get'])  # view added bikes in user page
def uhome():
    qry="SELECT * FROM `addbike`"
    res=selectall(qry)
    print(res)
    qry1="SELECT * FROM `offer`"             # view offer bikes in user page
    res1=selectall(qry1)
    qry2="SELECT * FROM `trending`"          # view trending bikes in user page
    res2=selectall(qry2) 
    return render_template("userPage.html",val=res,val1=res1,val2=res2)



@app.route("/addoffBike",methods=['post','get'])  # add offer bikes action in admin panel
def addoffBike():
    
    offname=request.form['offname']
    img=request.files['img']
    name=request.form['name']
    price=request.form['price']
    mile=request.form['mile']
    year=request.form['year']
    torq=request.form['torq']
    cc=request.form['cc']
    

    fn=datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    img.save("static/bikesImage/"+fn)

    

    qry="INSERT INTO `offer` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(offname,fn,name,price,mile,year,torq,cc)
    res=iud(qry,val)
    return '''<script> alert('Successfully Added');window.location="/offBike"</script>'''





@app.route("/viewoffBike",methods=['post','get'])  # view offer bikes in admin Panel
def viewoffBike():
    qry="SELECT * FROM `offer`"
    res=selectall(qry)
    return render_template("offerBike.html",val=res)


@app.route("/deleoffBike",methods=['post','get']) # delete offer bike action from admin panel
def deleoffBike():
    id=request.args.get('ID')
    qry="DELETE FROM `offer` WHERE `offid`=%s"
    val=(id)
    res=iud(qry,val)    
    return '''<script>alert("Deleted successfully.");window.location="/viewoffBike"</script>'''


@app.route("/viewtrenBike",methods=['post','get'])
def viewtrenBike():
    qry="SELECT * FROM `trending`"
    res=selectall(qry)
    return render_template("trendBike.html",val=res)


@app.route("/addtrendBike",methods=['post','get'])  # add trend bikes action in admin panel
def addtrendBike():
    
    trname=request.form['trname']
    trimg=request.files['trimg']
   
    

    fn=datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    trimg.save("static/bikesImage/"+fn)

    

    qry="INSERT INTO `trending` VALUES(NULL,%s,%s)"
    val=(trname,fn)
    res=iud(qry,val)
    return '''<script> alert('Successfully Added');window.location="/viewtrenBike"</script>'''



@app.route("/deletrendBike",methods=['post','get']) # delete trending bike action from admin panel
def deletrendBike():
    id=request.args.get('ID')
    qry="DELETE FROM `trending` WHERE `trid`=%s"
    val=(id)
    res=iud(qry,val)    
    return '''<script>alert("Deleted successfully.");window.location="/viewtrenBike"</script>'''


@app.route("/addService",methods=['post','get'])  # add new  service in admin panel
def addService():
    modelname=request.form['model']
    regno=request.form['regno']
    type=request.form['type']
    date=request.form['date']
    time=request.form['time']
    
    qry="SELECT `email` FROM `user_reg` WHERE `lid` = %s"
    res=selectone(qry,session['lId'])
    print(res['email'])
    message= Message("You are successfully booked service on :"+date+"-- Time "+time+" -- Vehicle Reg NO: "+regno,recipients=[res['email']])
    print(message)
    mail.send(message)
    

    qry="INSERT INTO `select_service` VALUES(NULL,%s,%s,%s,%s,%s,%s)"
    val=(session['lId'],modelname,regno,type,date,time)
    res=iud(qry,val)

    

    return '''<script> alert('Successfully Added');window.location="/service"</script>'''


@app.route("/viewService",methods=['get','post'])  # view service details in admin panel
def viewService():
    qry="SELECT * FROM `user_reg`,`select_service` WHERE select_service.lid = user_reg.lid"
    res=selectall(qry)

    return render_template("viewService.html",val=res)

app.run(debug=True)












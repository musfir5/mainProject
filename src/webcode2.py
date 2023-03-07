import smtplib
from flask import *
import os
from src.dbconnection import *
from datetime import datetime
app = Flask(__name__)
app.secret_key="mus"
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

@app.route("/service",methods=['post','get'])  # show 'service' page in user home
def service():

    qry="SELECT * FROM `addbike`"
    res=selectall(qry)
    qry1="SELECT * FROM `slots`"
    res1=selectall(qry1)

    return render_template("service.html",val=res,val1=res1)


@app.route("/emi",methods=['post','get'])      # show 'emi' page in user home 
def emi():

    qry="SELECT * FROM `emi`"
    res= selectall(qry)

    return render_template("emi.html",val=res)





@app.route("/viewUpload",methods=['get','post'])  # show 'upload' page in user Booking
def viewUpload():

    return render_template("upload.html")


@app.route("/payment",methods=['get','post'])    # show `payment` section in booking page 
def payment():

    return render_template("payment.html")






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

    message= Message("Mr/Ms"+name1+"  Your message recived successfully : Thankyou for contacting us.",recipients=[email])
    print(message)
    mail.send(message)

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
    qry1="SELECT * FROM `emi`"
    res1= selectall(qry1)
    
    return render_template("adminPage.html",val=res,val1=res1)




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


@app.route("/addnewBike",methods=['post','get'])  # add new bike into database
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
    qry1="SELECT * FROM `bike_model`"
    res1=selectall(qry1)
    return render_template("addBikes.html",val=res,val1=res1)


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



@app.route("/uhome",methods=['post','get'])  # view added bikes in user page  ---Main user page
def uhome():
    qry="SELECT * FROM `addbike`"
    res=selectall(qry)
    print(res)
    qry1="SELECT * FROM `offer`"             # view offer bikes in user page
    res1=selectall(qry1)
    qry2="SELECT * FROM `trending`"          # view trending bikes in user page
    res2=selectall(qry2) 
    return render_template("userPage.html",val=res,val1=res1,val2=res2)



@app.route("/addoffBike",methods=['post','get'])  # add offer bikes into database
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


@app.route("/addtrendBike",methods=['post','get'])  # add trend bikes into database
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


@app.route("/addService",methods=['post','get'])  # add new  service into database  # slote setting
def addService():
    email=request.form['email']
    modelname=request.form['model']
    regno=request.form['regno']
    type1=request.form['type']
    date=request.form['dates']
    time=request.form['time']
    
  
    date_select= "select sl_date,slots from `slots` where slots=%s"
    res1=selectone(date_select,date)

    if res1['slots'] <= 0:

        return '''<script> alert('Slot is full for this date');window.location="/service"</script>'''
    
    else:

        qry="INSERT INTO `select_service` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s)"
        val=(session['lId'],email,modelname,regno,type1,res1['sl_date'],time)
        res=iud(qry,val)

        sub=res1['slots']-1
        
        qry3="UPDATE `slots` SET `slots`=%s where `sl_date` = %s"
        val=(sub,res1['sl_date'])
        res3=iud(qry3, val)

   
    
        return '''<script> alert('Successfully Added');window.location="/service"</script>'''


@app.route("/viewService",methods=['get','post'])  # view service details in admin panel
def viewService():
    qry="SELECT * FROM `user_reg`,`select_service` WHERE select_service.lid = user_reg.lid"
    res=selectall(qry)
    qry1="SELECT * FROM `slots`"
    res1=selectall(qry1)

    return render_template("viewService.html",val=res,val1=res1)


@app.route("/deleService",methods=['post','get']) # delete service details action from admin panel
def deleService():
    id=request.args.get('ID')
    qry="DELETE FROM `select_service` WHERE `ssid`=%s"
    val=(id)
    res=iud(qry,val)    
    return '''<script>alert("Deleted successfully.");window.location="/viewService"</script>'''



@app.route("/addTestdrive",methods=['post','get'])  # add test drive into database
def addTestdrive():
    
    tdname=request.form['tdname']
    tdtime=request.form['tdtime']
    tddate=request.form['tddate']

    
    qry="SELECT `email` FROM `user_reg` WHERE `lid` = %s"
    res=selectone(qry,session['lId'])
    print(res['email'])
    message= Message("You are successfully booked Test drive on :"+tddate+"-- Time "+tdtime+" -- Vehicle Model: "+tdname,recipients=[res['email']])
    print(message)
    mail.send(message)


    qry="INSERT INTO `testDrive` VALUES(NULL,%s,%s,%s,%s)"
    val=(session['lId'],tdname,tdtime,tddate)
    res=iud(qry,val)
    return '''<script> alert('Successfully Added');window.location="/uhome"</script>'''


@app.route("/viewTestdrive",methods=['get','post'])    #view test drive details in admin panel
def viewTestdrive():

    qry="SELECT * FROM `user_reg`,`testDrive` WHERE testDrive.lid = user_reg.lid"
    res=selectall(qry)


    return render_template("viewTestdrive.html",val=res)





@app.route("/booking",methods=['get','post']) # show 'booking' page in user page
def booking():

    
    qry="SELECT * FROM `bike_model`"
    res=selectall(qry)


    return render_template("booking.html",val=res)



@app.route("/deleTestdrive",methods=['post','get']) # delete service details action from admin panel
def deleTestdrive():
    id=request.args.get('ID')
    qry="DELETE FROM `testDrive` WHERE `tdid`=%s"
    val=(id)
    res=iud(qry,val)    
    return '''<script>alert("Deleted successfully.");window.location="/viewTestdrive"</script>'''




@app.route("/addContact",methods=['post','get']) # show contact us messages in admin panel
def addContact():
    qry="SELECT * FROM `contact`"
    res=selectall(qry)
    return render_template("viewContact.html",val=res)



@app.route("/replayMess",methods=['get','post'])   # replay to the user from admin panel
def replayMess():
    id=request.args.get('ID')
    replay=request.form['replay']
    qry="SELECT `name`,`email`,`sub` FROM `contact` WHERE `cid` = %s"
    val=(id)
    res=selectone(qry,val)
    print(res['name'])
    print(res['email'])
    print(res)

    message= Message("Mr/Ms: "+res['name']+" This is the replay for your subject on: "+res['sub']+" REPLYA :- "+replay,recipients=[res['email']])
    print(message)
    mail.send(message)

    return '''<script>alert("replay sended successfully.");window.location="/addContact"</script>'''



@app.route("/addbooking",methods=['post','get'])   #booking action in user page
def addbooking():
    name=request.form['name1']
    phone=request.form['phone']
    email=request.form['email']
    addre=request.form['addre']
    model=request.form['model']

    message= Message(name+" You are successfully booked your bike model :"+model+" you need to update your document by clicking upload option in the site also you can make payment online",recipients=[email])
    print(message)
    mail.send(message)

    qry="INSERT INTO `booking` VALUES(NULL,%s,%s,%s,%s,%s,%s)"
    val=(session['lId'],name,phone,email,addre,model)
    res=iud(qry,val)

    session['bbId']= res['bbid']

    return '''<script> alert('Successfully booked');window.location="/booking"</script>'''
    


    
@app.route("/approveService",methods=['get','post'])   # approve service request by admin panel
def approveService():

    id=request.args.get('SID')

    qry1="SELECT `date`,`time`,`regno`,`s_email` FROM `select_service` WHERE `ssid` = %s"
    val1=(id)
    res1=selectone(qry1,val1)
    print(res1['regno'],res1['date'])
    message= Message("You are successfully booked service on  today "+res1['time']+" Vehicle Reg NO: "+res1['regno'],recipients=[res1['s_email']])
    print(message)
    mail.send(message)
    
    return '''<script> alert('Successfully approved service');window.location="/viewService"</script>'''


@app.route("/addUpload",methods=['get','post'])  # upload form action in user page
def addUpload():

    name2=request.form['name2']
    phone=request.form['ph']
    email=request.form['email']
    address=request.form['address']
    photo=request.files['phot']
    aadar=request.files['aadar']

    pho=datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    photo.save("static/upload/photo/"+pho)

    aad=datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    aadar.save("static/upload/aadar/"+aad)

    qry1="SELECT * FROM booking WHERE lid = %s"
    val1=(session['lId'])
    res1=selectone(qry1,val1)
   
    print(res1['bbil'])
    
    qry="INSERT INTO `upload` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s)"
    val=(res1['bbil'],name2,phone,email,address,pho,aad)
    res=iud(qry,val)
    return '''<script> alert('Successfully uploaded');window.location="/booking"</script>'''



@app.route("/viewBooking",methods=['post','get'])   # show `booking` booking details in admin panel 
def viewBooking():

    qry="SELECT * FROM `booking`,`upload` WHERE booking.bbil = upload.bbil"
    res=selectall(qry)
    
    return render_template("viewBooking.html",val=res)



@app.route("/deleBooking",methods=['get','post'])  # delete booking details from admin panel
def deleBooking():

    id=request.args.get('ID')
    qry="DELETE FROM `booking` WHERE `bbil`=%s"
    val=(id)
    res=iud(qry,val)    
    return '''<script>alert("Deleted successfully.");window.location="/viewBooking"</script>'''






@app.route("/deleMessage",methods=['get','post'])  # delete messages details from admin panel
def deleMessage():

    id=request.args.get('ID')
    qry="DELETE FROM `contact` WHERE `lid`=%s"
    val=(id)
    res=iud(qry,val)    
    return '''<script>alert("Deleted successfully.");window.location="/addContact"</script>'''





@app.route("/addmodelBike",methods=['post','get'])  # add new model bike into database
def addmodelBike():
    model=request.form['model']
    price=request.form['price']
   
 
    qry="INSERT INTO `bike_model` VALUES(NULL,%s,%s)"
    val=(model,price)
    res=iud(qry,val)
    return '''<script> alert('Successfully Added');window.location="/addBike"</script>'''





@app.route("/deleBike_model",methods=['get','post'])  # delete messages details from admin panel
def deleBike_model():

    id=request.args.get('ID')
    qry="DELETE FROM `bike_model` WHERE `bmid`=%s"
    val=(id)
    res=iud(qry,val)    
    return '''<script>alert("Deleted successfully.");window.location="/addBike"</script>'''


@app.route("/adEmi",methods=['post','get']) # `add EMI %` in admin panel
def adEmi():
    emi1=request.form['emi']
  
    qry = "INSERT INTO emi VALUES(NULL,%s)"
    val = (emi1)
    res = iud(qry, val)
    
    return '''<script>alert("EMI added successfully");window.location="/viewAdmins"</script>'''


@app.route("/deleEmi",methods=['post','get']) # delete emi % action in admin panel
def deleEmi():
    id=request.args.get('ID')
    qry="DELETE FROM `emi` WHERE `emid`=%s"
    val=(id)
    res=iud(qry,val)    
    return '''<script>alert("Deleted successfully.");window.location="/viewAdmins"</script>'''
    


@app.route("/adSlots",methods=['post','get']) # `add slots` in admin panel
def adSlots():
    date=request.form['slotDate']
    slot=request.form['slots']
  
    qry = "INSERT INTO slots VALUES(NULL,%s,%s)"
    val = (date,slot)
    res = iud(qry, val)
    
    return '''<script>alert("slots added successfully");window.location="/viewService"</script>'''


@app.route("/deleSlots",methods=['post','get']) # delete slos action in admin panel
def deleSlots():
    id=request.args.get('ID')
    qry="DELETE FROM `slots` WHERE `slid`=%s"
    val=(id)
    res=iud(qry,val)    
    return '''<script>alert("Deleted Slot successfully.");window.location="/viewService"</script>'''



@app.route("/setslot",methods=['get','post']) #-----------------------sample---------------
def setslot():

    qry="SELECT * FROM `slots`"
    res=selectall(qry)

    return render_template("slot.html",val=res)



app.run(debug=True)






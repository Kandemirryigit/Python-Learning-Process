from flask import Flask,render_template,request
import smtplib
from email.mime.text import MIMEText

app=Flask(__name__)

FROM_EMAIL="kyigit293@gmail.com"
PASSWORD="wogqjekloxwwiuqg"
TO_EMAIL="kandemirryigit@gmail.com"


@app.route("/")
def get_all_posts():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post1")
def post1():
    return render_template("post1.html")

@app.route("/post2")
def post2():
    return render_template("post2.html")

@app.route("/post3")
def post3():
    return render_template("post3.html")


@app.route("/form-entry",methods=["POST"])
def received_data():
    data=request.form
    name=data["name"]
    email=data["email"]
    phone=data["phone"]
    message=data["message"]

    full_message=f"From: {name}\nMail: {email}\nNumber: {phone}\nMessage: {message}"
    msg=MIMEText(full_message,_charset="UTF-8")
    msg["Subject"]="New Message From Website"
    msg["From"]=FROM_EMAIL

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(FROM_EMAIL,PASSWORD)
        connection.sendmail(FROM_EMAIL,TO_EMAIL,msg.as_string())
    return render_template("succesful.html")


    




if __name__=="__main__":
    app.run(debug=True)
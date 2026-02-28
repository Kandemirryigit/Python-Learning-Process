from flask import Flask,render_template
import random
import datetime as dt
import requests

app=Flask(__name__)

@app.route("/")
def home():
    random_number=random.randint(1,10)
    year=dt.datetime.now().year
    month=dt.datetime.now().month
    day=dt.datetime.now().day
    return render_template("index.html",num=random_number,year=year,month=month,day=day)

@app.route("/guess/<username>")
def guess(username):
    gender=requests.get(f"https://api.genderize.io?name={username}").json()["gender"]
    age=requests.get(f"https://api.agify.io?name={username}").json()["age"]
    
    return render_template("index2.html",name=username,gender=gender,age=age)


@app.route("/blog")
def get_blog():
    blog=requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html",blog=blog)
   

if __name__=="__main__":
    app.run(debug=True)
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog=requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html",blog=blog)

@app.route("/read/<int:number>")
def read(number):
    blog=requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    context=[]
    for post in blog:
        title=post["title"]
        subtitle=post["subtitle"]
        body=post["body"]
        context.append(title)
        context.append(subtitle)
        context.append(body)
    return render_template("post.html",blog=blog,number=number,context=context)


if __name__ == "__main__":
    app.run(debug=True)

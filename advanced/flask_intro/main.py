from flask import Flask, render_template
from random import randint
from datetime import datetime
from requests import get
app = Flask( __name__ )

@app.route('/')
def home():
    return "Hello World!"

@app.route("/guest/<username>")
def guest( username ):
    randiom_num = randint(1,100)
    cur_year = datetime.now().year
    params : dict = {
        "name" : "Abhay"
    }
    response = get("https://api.genderize.io", params=params)
    res = get("https://api.agify.io", params=params)
    sex = response.json()['gender']
    age = res.json()['age']
    return render_template('index.html', year=cur_year, age = age, sex=sex, name=username)


@app.route("/blogs")
def blogs():
    response = get("https://api.npoint.io/c790b4d5cab58020d391")
    posts = response.json()
    return render_template('blog-listing.html', blogs=posts)


@app.route("/blogs/<int:index>")
def showPost(index):
    response = get("https://api.npoint.io/c790b4d5cab58020d391")
    blogs = response.json()
    post = [i for i in blogs if i["id"]==index]
    return render_template("blog.html", index=index, blogs=post)

if __name__ == "__main__":
    app.run(debug=True)

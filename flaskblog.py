from flask import Flask, render_template,url_for
app = Flask(__name__)

posts=[
    {
        'author':'Pushpa Iyer',
        'title':'Blog post1',
        'content':'post1',
        'date_posted':'April 21, 2018'
    },
    {
        'author':'Aditi Chandrashekar',
        'title':'Blog post2',
        'content':'post2',
        'date_posted':'April 22, 2018'
    }
]

@app.route("/")
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True)
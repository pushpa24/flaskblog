from flask import Flask, render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY']='620393bcb6a7e844abad8ea480635232'

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
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='register',form=form)

@app.route("/login")
def login():
    form=LoginForm()
    return render_template('login.html',title='login',form=form)

if __name__=="__main__":
    app.run(debug=True)
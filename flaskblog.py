from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '31da0ee3646ae04f456db0a344bab17d'

posts = [
    {
        'author': 'author1',
        'title': 'post1',
        'content': 'content1',
        'date_posted': 'april 20, 2019'
    },
    {
        'author': 'author2',
        'title': 'post2',
        'content': 'content2',
        'date_posted': 'april 22, 2019'
    },
    {
        'author': 'author3',
        'title': 'post3',
        'content': 'content2',
        'date_posted': 'april 22, 2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='about')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.email.data == 'admin@blog.com' and form.password.data == 'password':
        flash('you have been logged in', 'success')
        return redirect(url_for('home'))
    else:
        flash('login unsuccessful', 'danger')
    return render_template('login.html', title='login', form=form)


if __name__ == '__main__':
    app.run(debug=True)

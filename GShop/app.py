from flask import Flask, render_template

app = Flask(__name__)  # creating the flask class object


@app.route("/")
def main():
    return "My First Flask Web Application"


@app.route("/demo")
def demo1():
    return "Demo Page"


@app.route("/admin")
def demo2():
    return "Admin Page"


@app.route("/user")
def demo3():
    return "User Page"


@app.route("/user/<name>")
def demo4(name):
    return "Hello %s" %name

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/stockmanager")
def stockmanager():
    return render_template("sm_login.html")

@app.route("/shopowner")
def shopowner():
    return render_template("so_login.html")

@app.route("/customer")
def customer():
    return render_template("customer_login.html")

if __name__ == '__main__':
    app.run(debug=True)
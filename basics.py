from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def main():
    return "Hello World"

@app.route("/hello2/") # Both /hello2 and /hello2/ work
def hello_world2():
    return "hello world/"

@app.route("/hello")  # /hello/ doesn't work
def hello_world():
    return 'hello world'
# app.add_url_rule("/","hello",hello_world) also binds the route to the method like @app.route() does

@app.route("/greeting/<name>")  # <name> allows parameters
def greet(name):
    if name=='admin':
        return redirect(url_for('hello_admin', adname=name)) # url_for calls a function and then it's parameters
    return "Hello " + name

@app.route('/admin/<adname>')
def hello_admin(adname):
    return "Hello admin " + adname

@app.route("/age/<int:a>") # <int:> makes the variable have to be an integer
def age(a):
    return "your age " + str(a)

if __name__=='__main__':
    # Default port is 5000
    app.debug = True # This lets the website refresh with code changes
    app.run()
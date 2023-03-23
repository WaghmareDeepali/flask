from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello ,world </h1>"

@app.route("/hello_world1")
def hello_world1():
    return "<h1>Hello ,world ........Deepali</h1>"

@app.route("/hello_world2")
def hello_world2():
    return "<h1>Hello ,world.....Waghmare </h1>"

@app.route("/test")
def test():
    a=5+6
    return "<h1>this is my test function testing the flask and working flask.........</h2>{}".format(a)

# @app.route("/test2")
# def test2():


if __name__=="__main__":
    app.run(host="0.0.0.0")
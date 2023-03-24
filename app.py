from flask import Flask,render_template,request,jsonify

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home_page():
    return render_template("index.html")


@app.route("/")
def hello_world():
    return "<h1>Hello ,world </h1>"


#creating method for performing operation like add,sub,div
@app.route('/math',methods=['POST'])
def math_operation():
    if(request.method=='POST'):
        ops=request.form['operation'] 
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
    if(ops=='subtract'):
            r=num1-num2
            result='The subtract of '+'\t'+str(num1)+'\t'+'and'+'\t'+str(num2)+'is'+str(r)
    if(ops=='multiply'):
            r=num1*num2
            result='The multiplyof '+'\t'+str(num1)+'\t'+'and'+'\t'+str(num2)+'is'+str(r)
    if(ops=='divide'):
            r=num1/num2
            result='The divide of '+'\t'+str(num1)+'\t'+'and'+'\t'+str(num2)+'is'+str(r)

    return render_template('result.html',result=result)  




if __name__=="__main__":
    app.run(host="0.0.0.0")
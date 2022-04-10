from flask import Flask, request, render_template, redirect, url_for, make_response
import json

app = Flask(__name__)

@app.route('/data', methods = ['GET'])
def index():
    num = request.args.get('number')
    
    if num.isnumeric():
        sum = 0
        for i in range(1, int(num) + 1):
        
            sum += i

        return str(sum)
    else:
        return "Wrong Parameter"

@app.route('/sum.html')
def sum():
    return render_template("sum.html")


@app.route('/myName')
def get_cookie():
    cookie = request.cookies.get('mycookie')
    if cookie == None:
        return render_template("setcookie.html")
    else:
        return cookie
        
@app.route('/trackName' , methods = ['GET'])   
def set_cookie():
    name = request.args.get('name')
    resp = make_response('Setting cookie!')
    resp.set_cookie(key='mycookie', value=name)
    return resp
  
app.run(debug=True, port=3000, host='0.0.0.0')
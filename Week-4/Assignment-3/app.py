from flask import Flask, request, Response, jsonify, json, session, url_for, redirect, render_template
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_cors import CORS, cross_origin
from setting import DB_CONFIG, SESSION_SECRET_KEY
import pymysql
import jwt

def insert(params):
    db = pymysql.connect(host=DB_CONFIG['host'],
                        user=DB_CONFIG['user'],
                        password=DB_CONFIG['password'],
                        database=DB_CONFIG['database'])

    cursor = db.cursor()
    query = """INSERT INTO user (email, password) VALUEs (%s, %s)"""
    try:
        cursor.execute(query, params)
        db.commit()
        db.close()
        return True
        
    except:
        db.rollback()
        db.close()
        return False

def get(params):
    db = pymysql.connect(host=DB_CONFIG['host'],
                        user=DB_CONFIG['user'],
                        password=DB_CONFIG['password'],
                        database=DB_CONFIG['database'])

    cursor = db.cursor(pymysql.cursors.DictCursor)
    query = """SELECT * FROM user WHERE email = %s"""
    cursor.execute(query, params)
    entries = cursor.fetchall()

    return entries[0]

def check(params):
    db = pymysql.connect(host=DB_CONFIG['host'],
                        user=DB_CONFIG['user'],
                        password=DB_CONFIG['password'],
                        database=DB_CONFIG['database'])

    cursor = db.cursor()
    query = """SELECT EXISTS(SELECT * FROM user WHERE email= %s)"""
    cursor.execute(query, params)

    if cursor.fetchall()[0][0]:
        return True
    else:
        return False
    

app = Flask(__name__)
cors = CORS(app)
#app.config['CORS_HEADERS'] = 'Content-Type'

app.config['SECRET_KEY'] = SESSION_SECRET_KEY['SECRET_KEY']
#app.config['SESSION_USE_SIGNER'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = 120

@app.route('/')
def home():
    if 'username' in session:
        user_id = session['username']
        return render_template('index.html')
        #return jsonify({'message' : 'You are already logged in', 'user_id' : user_id})
    else:
        return render_template('login.html')
        #return jsonify({'message' : 'Unauthorized'})

@app.route('/login', methods =['POST'])
def login():
    login_info = json.loads(request.data)
    email = login_info['email']
    password = login_info['password']
    
    if check(email):
        try:
            user_info = get(email)
            if check_password_hash(user_info['password'], password):
                session['username'] = user_info['id']
                return render_template('index.html')
                #return jsonify({'message' : 'You are logged in successfully'})
            else:
                return jsonify({'message' : 'The password is incorrect, Please try again'})
        except:
            return Response(status=401)
    else:
        return jsonify({'message' : "Couldn't find your account"}), 401
    

@app.route('/logout',  methods=['GET'])
def logout():
    if 'username' in session:
        session.pop('username', None)
    return render_template('login.html')
    #return jsonify({'message' : 'You successfully logged out'})

@app.route('/register', methods=['POST'])
def register():
    user_info = json.loads(request.data)
    email = user_info['email']
    password = user_info['password']
    comfirm_password = user_info['confirm_password']

    if check(email):
        return jsonify({'message' : 'The email is taken. Please try another.'}), 409 # The email is taken.
    
    else:
        if password == comfirm_password:
            password_hash = generate_password_hash(password)

            if insert((email, password_hash)):
                return render_template('login.html')
                #return jsonify({'message' : 'Registration Successful'}), 201 # Registration Successful
            else:
                return jsonify({'message' : 'Registration Failed'}), 409 # Registration Failed

        else:
            return jsonify({'message' : 'Your new and confirm password are different. Please enter your passwords again.'}), 409 # Registration Failed

@app.route('/register_form')
def redirect():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0')
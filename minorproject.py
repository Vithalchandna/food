from flask import *
import datetime
from mongodb3 import MongoDBHelper
import hashlib
from bson.objectid import ObjectId

web_app = Flask("PeitPooja")

@web_app.route("/")
def index():
    return render_template('index.html')

@web_app.route("/register")
def register():
    return render_template('register.html')

@web_app.route("/register-customer", methods=['POST'])
def register_customer():

    customer_data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'password': hashlib.sha256(request.form['pwd'].encode('utf-8')).hexdigest(),
        'phone_number': request.form['phone_number'],
        'createdOn': datetime.datetime.today()
    }

    print(customer_data)
    db = MongoDBHelper(collection="customerfood")

    # Update MongoDB Helper insert function, to return result here
    result = db.insert(customer_data)

    # Test the same
    customer_id = result.inserted_id
    session['customer_id'] = str(customer_id)
    session['customer_email'] = customer_data['email']

    return render_template('home.html', email=session['customer_email'])

@web_app.route("/login-customer", methods=['POST'])
def login_customer():

    customer_data = {
        'email': request.form['email'],
        'password': hashlib.sha256(request.form['pswd'].encode('utf-8')).hexdigest(),
    }

    print(customer_data)
    db = MongoDBHelper(collection="customerfood")
    documents = db.fetch(customer_data)
    print(documents, type(documents))
    if len(documents) == 1:
        session['customer_email'] = documents[0]['email']
        print(vars(session))
        return render_template('home.html', email=session['customer_email'], )
    else:
        return render_template('error.html')



def main():
    web_app.secret_key = 'PeitPooja-key-1'
    web_app.run(port=5001)

if __name__ == "__main__":
    main()

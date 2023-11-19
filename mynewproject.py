from flask import *
import datetime
from mongodb3 import MongoDBHelper
import hashlib
from bson.objectid import ObjectId


web_app = Flask("Foodie Express")

@web_app.route("/")
def index():
    return render_template('index.html')


@web_app.route("/register")
def register():
    return render_template('register1.html')


@web_app.route("/home")
def home():
    return render_template('home.html')


@web_app.route("/raja")
def menu_raja():
    return render_template('home2.html')


@web_app.route("/register-customer", methods=['POST'])
def register_customer():

    customer_data = {
        'email': request.form['email'],
        'password': hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest(),
        'city': request.form['city'],
        'createdOn': datetime.datetime.today()
    }

    print(customer_data)
    db = MongoDBHelper(collection="xyz")

    # Update MongoDB Helper insert function, to return result here
    result = db.insert(customer_data)

    # Test the samet.inserted_id
    #     session['custom
    session['customer_email'] = customer_data['email']

    return render_template('home.html', email=session['customer_email'])


@web_app.route("/login", methods=['POST'])
def login_customer():
    customer_data = {
        'email': request.form['email'],
        'password': hashlib.sha256(request.form['pswd'].encode('utf-8')).hexdigest(),
    }

    print("Received login request with customer data:", customer_data)

    try:
        db = MongoDBHelper(collection="xyz")
        print("Connected to MongoDB successfully.")
    except Exception as e:
        print("Error connecting to MongoDB:", str(e))
        return "Database connection error."

    documents = db.fetch(customer_data)
    print("Fetched documents:", documents, type(documents))

    if len(documents) == 1:
        session['customer_id'] = str(documents[0]['_id'])
        session['customer_email'] = documents[0]['email']
        session['customer_name'] = documents[0]['name']
        print("User logged in. Session Variables:", vars(session))
        return render_template('home.html')
    else:
        print("Login failed. No matching user found.")
        return "Login failed. Invalid credentials."




@web_app.route("/logout")
def logout():
    session['customer_id'] = ""
    session['customer_email'] = ""
    return redirect("/")


if __name__ == "__main__":
    web_app.run(port="5005")

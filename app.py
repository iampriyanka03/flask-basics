from flask import Flask,request,url_for,redirect
from flask.json import jsonify


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/contact')
def contact_page():
    return 'your number is 9347027986'

@app.route('/user/<name>')
def user(name):
    return '<h1>hello {}</h1>'.format(name)

@app.route('/project/<int:urid>')
def displayid(urid):
    return '<h1>Your roll number is {}</h1>'.format(urid)

#showing json output in the web app(dictionary)
@app.route('/json')
def showjsonpage():
    return jsonify({"name":"pandu","location":"hyderabad"})

# GET,POST
@app.route('/form',methods = ['POST','GET'])
def showform():
    return '<h1> this page is from POST and GET methods </h1>'

@app.route('/application',methods = ['POST'])
def showapplication():
    return '<h1>this page is from POST methods </h1>'

#student page
@app.route('/studentpage',methods=['POST','GET'],defaults ={"studentname" : "priya"})
@app.route('/studentpage/<string:studentname>',methods=['POST','GET'])
def showstudentpage(studentname):
    return '<h1>hello {}</h1>'.format(studentname)

# taking multiple inputs from the user , through the url application using ? and & symbol
@app.route('/query')
def showquerypage():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1>hello {} from {}</h1>'.format(name, location)

#displaying login page
@app.route('/loginpage')
def showloginpge():
    return"""
        <form action = "/processloginform" method ="POST">
                <h1>enter your details to continue.</h1>
                <input type = "text" name = "username" placeholder = "enter your user name" /></br></br>
                <input type = "password" name = "password" placeholder = "enter your password" /></br></br>

                <input type = "submit" value = "login">
        </form>
        """

#to fetch or request from the form
@app.route('/processloginform', methods=['POST'])
def processloginform():
    username = request.form['username']
    password = request.form['password']
    return '<h1> hello your name is {} and password is {} </h1>'.format(username, password)


# Using POST and GET methods for auto navigation of the user as if-else condition.
@app.route('/welcomepage', methods=['POST', 'GET'], defaults={"name": "pandu", "location": "hyderabad"})
@app.route('/welcomepage/<string:name>', methods=['POST', 'GET'])
def showwelcomepage(name, location=None):
    return '<h1>hello {}, welcome to the home</h1>'.format(name)

@app.route("/theform", methods=['POST', 'GET'])
def showtheform():
    if request.method == 'GET':
        return """
        <form action="/theform" method="POST">
            <h1>enter your details to continue.</h1>
            <input type="text" name="name" placeholder="enter your name" /><br /><br />
            <input type="text" name="location" placeholder="enter your location" /><br /><br />
            <input type="submit">
        </form>
        """
    else:
        name = request.form['name']
        location = request.form['location']
        return redirect(url_for('showwelcomepage', name=name, location=location))
    

if __name__ == '__main__':
    app.run(debug=True)


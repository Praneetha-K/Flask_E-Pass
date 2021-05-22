# This is a sample Python script.
'''
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



from flask import Flask, render_template, request, redirect, url_for

#from werkzeug.utils import redirect

app = Flask(__name__)


@app.route('/')
@app.route("/", methods=["GET", "POST"])
def data():
    print("ghm")
    if request.method == "POST":
        print("abh")
        req = request.form

        firstname = req.get("fname")
        lastname = req.get("lname")
        email = req.get("email")
        phn=req.get("phn")
        SState=req.get("ss")
        SCity=req.get("sc")
        DState=req.get("ds")
        DCity=req.get("dc")
        Aadhno=req.get("aan")
        print(firstname)
        return redirect(request.url)

    return render_template("data.html")



if __name__ == '__main__':
    app.run()


from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def student():
   return render_template('data.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      print(result)
      return render_template("result.html",result = result)


if __name__ == '__main__':
   app.run(debug = True)'''

import requests
from flask import Flask, render_template, request
from twilio.rest import Client

account_sid = 'AC6b8eea9ea7c855ff768347ef6f16bac5'
auth_token = '874965f2b9e415ab48cb2209c546484a'
client = Client(account_sid, auth_token)
app = Flask(__name__)


@app.route('/')
def data():
    return render_template('data.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if (request.method == "POST"):
        firstname = request.form['first_name']
        lastname = request.form['last_name']
        emailid = request.form['email']
        source_st = request.form['Source_state']
        source_dt = request.form['Source_city']
        destination_st = request.form['Destination_state']
        destination_dt = request.form['Destination_city']
        phnnumber = request.form['Phone_number']
        idc = request.form['id_proof']
        date=request.form['date']
        fullname = firstname + "." + lastname
        result = request.form
        r = requests.get('https://api.covid19india.org/v4/data.json')
        json_data = r.json()
        cnt = json_data[destination_st]['districts'][destination_dt]['total']['confirmed']
        pop = json_data[destination_st]['districts'][destination_dt]['meta']['population']
        travel_pass = ((cnt / pop) * 100)
        if (travel_pass < 30) and request.method == 'POST':
            status = 'confirmed'
            client.messages.create(to="whatsapp:+917013479436",
                                   from_="whatsapp:+14155238886",
                                   body="HELLO" + " " + fullname + " " + "your travel from" + " " + source_dt + " " + "to" + " " + destination_dt + " is " + status)
            result = request.form
            return render_template('result.html', result=result, var=status)
        else:
            status = 'not confirmed'
            client.messages.create(to="whatsapp:+917013479436",
                                   from_="whatsapp:+14155238886",
                                   body="HELLO" + " " + fullname + " " + "your travel from" + " " + source_dt + " " + "to" + " " + destination_dt + " is " + status)
            result = request.form
            return render_template('result.html', result=result, var=status)
    else:
        print("Not found")
        # return render_template('result.html', result=result, var=status)


if __name__ == '__main__':
    app.run(debug=True)

# This is a sample Python script.
 

import requests
from flask import Flask, render_template, request
from twilio.rest import Client

account_sid = ''
auth_token = ''
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

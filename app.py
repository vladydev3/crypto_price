from flask import Flask, request, render_template
import requests 

app = Flask(__name__)

access_key = '8e10bac3ef2b3d8beb2376742f681cd5';

@app.route('/', methods=['GET', 'POST'])
def get_crypto():
    response = requests.get(f'http://api.coinlayer.com/live?access_key={access_key}')

    if request.method == 'POST':
        if (request.form['crypto'] == ''):
            return "<html><body><h1>Invalid Input</h1></body></html>"
        else:
            crypto = request.form['crypto']
            price = response.json()['rates'][crypto]
            return render_template('./return_price.html', price=price, crypto=crypto)
        
    if request.method == 'GET':
        return render_template('./index.html')

if __name__ == '__main__':
    app.run(debug=True)
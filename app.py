from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>مرحباً بكم في موقعي!</h1>
    <p>هذا أول موقع أبنيه بـ Python</p>
    '''

if __
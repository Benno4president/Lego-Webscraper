import flask
from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

# Index
@app.route('/', methods=['GET', 'POST'])
def index():
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

@app.route('/')
def index():
 return '<h1>Hello World!</h1>'
 
if __name__ == '__main__':
    app.run(debug=True)

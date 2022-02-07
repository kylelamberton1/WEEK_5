from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'This is the home page'

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/square/<num>')
def square(num):
    num = int(num)
    answer = num*num
    return str(answer)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, welcome to the deployed project on Vercel!"

@app.route('/math')
def math():
    num1 = 5
    num2 = 10
    result = num1 + num2
    return f"The result of adding {num1} and {num2} is {result}"

if __name__ == "__main__":
    app.run()

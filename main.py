from flask import Flask

app = Flask(__name__)

print("Hello, welcome to the deployed project on Vercel!")

if __name__ == "__main__":
    app.run()

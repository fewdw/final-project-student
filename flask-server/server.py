from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"


if __name__ == '__main__':
    app.run(debug=True)

#activate venv
#mac: source venv/bin/activate
#windows: .\venv\Scripts\activate

# run
# python3 server.py
# or python server.py

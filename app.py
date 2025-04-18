from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def greet():
    return jsonify({'message':"Hello Vempada Siva Kumar Reddy"})

if __name__ == '__main__':
    app.run()

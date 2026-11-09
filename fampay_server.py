from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/')
def home():
    return "CODEFORGE PRO Server Running"
@app.route('/verify')
def verify():
    return jsonify({"status":"success","message":"Payment verified"})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

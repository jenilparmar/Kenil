from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/api/health')
def health():
    return jsonify({'status': 'ok'})

@app.route('/api/info')
def info():
    return jsonify({
        'name': 'Simple Flask Server',
        'version': '1.0.0'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health')
def health():
    return render_template('health.html', status="OK", message="Server is healthy")

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        name = request.form.get('name', 'Anonymous')
        return render_template('data.html', received=name, message="Data received successfully!")
    return render_template('data.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

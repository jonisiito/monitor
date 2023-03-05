from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route('/')
def index():
    result = os.popen('docker stats --no-stream').readlines()[1:]
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)


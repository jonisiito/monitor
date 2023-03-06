from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route('/')
def index():
    result = os.popen('docker stats --no-stream').readlines()[1:]
    
    ram = os.popen('free -m | awk \'NR==2{printf("%.2f%%", $3/$2*100)}\'').read().strip()
    return render_template('index.html', result=result, ram=ram)

@app.route('/cpu_usage')
def cpu_usage():
    result = os.popen('mpstat 1 1 | awk \'$12 ~ /[0-9.]+/ { printf("%.2f%%\\n", 100 - $12); }\'').read().strip()
    return result

@app.route('/ram_usage')
def ram_usage():
    result = os.popen('free -m | awk \'NR==2{printf("%.2f%%", $3/$2*100)}\'').read().strip()
    return result

@app.route('/createcookie', methods=['POST'])
def cookie():
  sesion = flask.request.form['sesion']
  print(sesion)
  resp = flask.make_response(flask.redirect("http://3.237.171.101"))
  print('a')
  resp.set_cookie('sesion', sesion)
  print('b')
  return resp

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)


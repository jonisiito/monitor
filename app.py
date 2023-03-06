
import flask
import os
import urllib.request
app = flask.Flask(__name__)

external_ip = urllib.request.urlopen('https://ident.me/').read().decode('utf8')

@app.route('/')
def index():
    try:
        if(len(flask.request.cookies.get('sesion'))>5):
            result = os.popen('docker stats --no-stream').readlines()[1:]
            ram = os.popen('free -m | awk \'NR==2{printf("%.2f%%", $3/$2*100)}\'').read().strip()
            return flask.render_template('index.html', result=result, ram=ram, external_ip1='http://'+external_ip+'/cpu_usage', external_ip2='http://'+external_ip+'/ram_usage')

    except:
        return '<h2 style="font-family: Arial, sans-serif; font-weight: bold;  text-align:center;">¡Error! Necesitas iniciar sesion</h2>'
        
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
  resp = flask.make_response(flask.redirect("http://"+external_ip))
  print('a')
  resp.set_cookie('sesion', sesion)
  print('b')
  return resp

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
    
    


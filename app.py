from flask import Flask, request, session, render_template

from modules.tools import SysInfo

app = Flask(__name__)
app.secret_key = 't_session'

device = ''

@app.route('/')
def indexpage():
    sys = SysInfo(device=device)
    sys.getInfo()
    return render_template('index.html',sys=sys)

if __name__ == '__main__':
    device = 'Android Device'
    app.run('0.0.0.0', port=5000, debug=True)

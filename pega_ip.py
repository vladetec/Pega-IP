import ipapi
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def Index():
    search = request.form.get('search')
    data = ipapi.location(ip=search, output='json')
    return render_template('index.html', data=data)

@app.route("/pega_ip", methods=["GET"])
def pega_ip():
    #return jsonify({'ip': request.remote_addr}), 200
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return jsonify({'ip': request.environ['REMOTE_ADDR']}), 200
    else:
        return jsonify({'ip': request.environ['HTTP_X_FORWARDED_FOR']}), 200    


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)
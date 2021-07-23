from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def test():
    return render_template('test.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    name = ''
    if request.method == 'POST':
        test_result = request.form
        for key, value in test_result.items():
            if key in '이름:':
                name = value
            if key in '년도:':
                year = value
            if key in '월:':
                month = value
            if key in '일:':
                day = value
        return render_template("result.html", result=test_result, name=name, year=year, month=month, day=day)


@app.route('/save', methods=['POST', 'GET'])
def save():
    if request.method == 'POST':

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
from calculation.specific_gravity import calculate

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        water = float(request.form['water'])
        dry = float(request.form['dry'])
        result = calculate(water, dry)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

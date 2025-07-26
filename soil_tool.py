from flask import Flask, render_template, request

from calculation.specific_gravity import calculate as sg_calculate
from calculation.plasticity import calculate as pl_calculate
from calculation.compaction import calculate as cp_calculate
from calculation.consolidation import calculate as cs_calculate
from calculation.permeability import calculate as pm_calculate
from calculation.hydrometer import calculate as hy_calculate
from calculation.grain_size import calculate as gs_calculate

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/specific_gravity', methods=['GET', 'POST'])
def specific_gravity():
    result = None
    if request.method == 'POST':
        try:
            water = float(request.form['water'])
            dry = float(request.form['dry'])
            result = sg_calculate(water, dry)
        except (ValueError, KeyError):
            result = "Invalid input. Please enter numeric values."
    return render_template('specific_gravity.html', result=result)


@app.route('/plasticity', methods=['GET', 'POST'])
def plasticity():
    result = None
    if request.method == 'POST':
        try:
            wl = float(request.form['wl'])
            wp = float(request.form['wp'])
            result = pl_calculate(wl, wp)
        except (ValueError, KeyError):
            result = "Invalid input. Please enter numeric values."
    return render_template('plasticity.html', result=result)


@app.route('/compaction', methods=['GET', 'POST'])
def compaction():
    result = None
    if request.method == 'POST':
        try:
            weight_mold = float(request.form['weight_mold'])
            weight_compacted = float(request.form['weight_compacted'])
            volume_mold = float(request.form['volume_mold'])
            result = cp_calculate(weight_mold, weight_compacted, volume_mold)
        except (ValueError, KeyError):
            result = "Invalid input. Please enter numeric values."
    return render_template('compaction.html', result=result)


@app.route('/consolidation', methods=['GET', 'POST'])
def consolidation():
    result = None
    if request.method == 'POST':
        try:
            load = float(request.form['load'])
            settlement = float(request.form['settlement'])
            result = cs_calculate(load, settlement)
        except (ValueError, KeyError):
            result = "Invalid input. Please enter numeric values."
    return render_template('consolidation.html', result=result)


@app.route('/permeability', methods=['GET', 'POST'])
def permeability():
    result = None
    if request.method == 'POST':
        try:
            discharge = float(request.form['discharge'])
            area = float(request.form['area'])
            length = float(request.form['length'])
            head = float(request.form['head'])
            result = pm_calculate(discharge, area, length, head)
        except (ValueError, KeyError):
            result = "Invalid input. Please enter numeric values."
    return render_template('permeability.html', result=result)


@app.route('/hydrometer', methods=['GET', 'POST'])
def hydrometer():
    result = None
    if request.method == 'POST':
        try:
            reading = float(request.form['reading'])
            temperature = float(request.form['temperature'])
            time = float(request.form['time'])
            result = hy_calculate(reading, temperature, time)
        except (ValueError, KeyError):
            result = "Invalid input. Please enter numeric values."
    return render_template('hydrometer.html', result=result)


@app.route('/grain_size', methods=['GET', 'POST'])
def grain_size():
    result = None
    if request.method == 'POST':
        try:
            weight_retained = float(request.form['weight_retained'])
            total_weight = float(request.form['total_weight'])
            result = gs_calculate(weight_retained, total_weight)
        except (ValueError, KeyError):
            result = "Invalid input. Please enter numeric values."
    return render_template('grain_size.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)

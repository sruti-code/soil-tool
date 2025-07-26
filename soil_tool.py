from flask import Flask, render_template, request

from calculation.specific_gravity import calculate_specific_gravity as sg_calculate
from calculation.plasticity import calculate_plasticity_limits as pl_calculate
from calculation.compaction import calculate_compaction as cp_calculate
from calculation.consolidation import calculate_consolidation as cs_calculate
from calculation.permeability import calculate_constant_head_permeability as ch_calculate
from calculation.permeability import calculate_falling_head_permeability as fh_calculate
from calculation.hydrometer import calculate_particle_diameter as hy_calculate
from calculation.grain_size import calculate_percent_finer as gs_calculate

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/specific_gravity', methods=['GET', 'POST'])
def specific_gravity():
    result = None
    if request.method == 'POST':
        try:
            weight_dry = float(request.form['weight_dry'])
            weight_submerged = float(request.form['weight_submerged'])
            weight_container = float(request.form['weight_container'])
            result = sg_calculate(weight_dry, weight_submerged, weight_container)
        except (ValueError, KeyError):
            result = "Invalid input. Please enter numeric values."
    return render_template('specific_gravity.html', result=result)

@app.route("/permeability", methods=["GET", "POST"])
def permeability():
    result = None
    if request.method == "POST":
        method = request.form.get("method")
        try:
            if method == "constant":
                length = float(request.form["length"])
                area = float(request.form["area"])
                head_loss = float(request.form["head_loss"])
                time = float(request.form["time"])
                result = ch_calculate(length, area, head_loss, time)
            elif method == "falling":
                a = float(request.form["a"])
                A = float(request.form["A"])
                L = float(request.form["L"])
                t = float(request.form["t"])
                h1 = float(request.form["h1"])
                h2 = float(request.form["h2"])
                result = fh_calculate(a, A, L, t, h1, h2)
            else:
                result = "Unknown method selected"
        except (ValueError, KeyError):
            result = "Invalid input. Please enter numeric values."
    return render_template("permeability.html", result=result)
    
@app.route('/compaction', methods=['GET', 'POST'])
def compaction():
    result = None
    if request.method == 'POST':
        try:
            weight_mold_wet = float(request.form['weight_mold_wet'])
            weight_mold = float(request.form['weight_mold'])
            volume_mold = float(request.form['volume_mold'])
            moisture_content = float(request.form['moisture_content'])

            result = cp_calculate(weight_mold_wet, weight_mold, volume_mold, moisture_content)
        except (ValueError, KeyError):
            result = "Invalid input. Please enter numeric values."
    return render_template('compaction.html', result=result)

@app.route('/consolidation', methods=['GET', 'POST'])
def consolidation():
    result = None
    if request.method == 'POST':
        try:
            strain = float(request.form['strain'])
            time_initial = float(request.form['time_initial'])
            time_final = float(request.form['time_final'])
            result = cs_calculate(strain, time_initial, time_final)
        except (ValueError, KeyError):
            result = "Invalid input. Please enter numeric values."
    return render_template('consolidation.html', result=result)


@app.route('/hydrometer', methods=['GET', 'POST'])
def hydrometer():
    result = None
    if request.method == 'POST':
        try:
            viscosity = float(request.form['viscosity'])
            specific_gravity = float(request.form['specific_gravity'])
            time = float(request.form['time'])
            depth = float(request.form['depth'])
            result = hy_calculate(viscosity, specific_gravity, time, depth)
        except (ValueError, KeyError):
            result = "Invalid input. Please enter numeric values."
    return render_template('hydrometer.html', result=result)

@app.route("/grain_size", methods=["GET", "POST"])
def grain_size():
    result = None
    if request.method == "POST":
        try:
            total_weight = float(request.form['total_weight'])
            retained_input = request.form['retained_weights']
            retained_weights = [float(w.strip()) for w in retained_input.split(',') if w.strip()]
            result = gs_calculate(total_weight, retained_weights)
        except (ValueError, KeyError):
            result = "Invalid input. Please ensure weights are numbers, separated by commas."
    return render_template("grain_size.html", result=result)

@app.route('/plasticity', methods=['GET', 'POST'])
def plasticity():
    result = None
    if request.method == 'POST':
        try:
            liquid_limit = float(request.form['liquid_limit'])
            plastic_limit = float(request.form['plastic_limit'])
            result = pl_calculate(liquid_limit, plastic_limit)
        except (ValueError, KeyError):
            result = "Invalid input. Please enter numeric values."
    return render_template('plasticity.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)

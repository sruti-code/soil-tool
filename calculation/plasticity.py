# calculation/plasticity.py

def calculate_plasticity_limits(liquid_limit, plastic_limit):
    try:
        if liquid_limit <= 0 or plastic_limit <= 0:
            return "Limits must be positive."
        if plastic_limit > liquid_limit:
            return "Plastic limit cannot be greater than liquid limit."
        plasticity_index = liquid_limit - plastic_limit
        return round(plasticity_index, 2)
    except Exception as e:
        return f"Error: {e}"

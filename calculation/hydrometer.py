def calculate_particle_diameter(viscosity, specific_gravity, time, depth):
    try:
        if any(x <= 0 for x in [viscosity, specific_gravity, time, depth]):
            return "All inputs must be positive."
        if specific_gravity <= 1:
            return "Specific gravity must be greater than 1 (soil particles > water)."
        d = ((18 * viscosity * depth) / ((specific_gravity - 1) * 980 * time)) ** 0.5
        return round(d * 1000, 4)  # diameter in mm
    except Exception as e:
        return f"Error: {e}"

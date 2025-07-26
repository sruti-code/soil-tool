def calculate_particle_diameter(viscosity, specific_gravity, time, depth):
    try:
        # Input validation
        if viscosity <= 0 or specific_gravity <= 1 or time <= 0 or depth <= 0:
            return "Inputs must be positive, and specific gravity must be > 1."

        # Stokes' law based calculation
        g = 980  # acceleration due to gravity in cm/s²
        diameter_cm = ((18 * viscosity * depth) / ((specific_gravity - 1) * g * time)) ** 0.5
        diameter_mm = diameter_cm * 10  # convert from cm to mm

        return round(diameter_mm, 4)
    except Exception as e:
        return f"Error: {e}"

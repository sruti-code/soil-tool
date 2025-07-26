def calculate_permeability(length, area, head_loss, time):
    try:
        # Validate inputs
        if length <= 0:
            return "Length must be a positive value."
        if area <= 0:
            return "Cross-sectional area must be a positive value."
        if head_loss <= 0:
            return "Head loss must be a positive value."
        if time <= 0:
            return "Time duration must be a positive value."

        # Calculate permeability coefficient (k)
        permeability = (length * area) / (time * head_loss)
        return round(permeability, 6)
    
    except Exception as e:
        return f"Error during calculation: {e}"

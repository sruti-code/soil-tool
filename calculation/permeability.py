def calculate_permeability(length, area, head_loss, time):
    try:
        if any(x <= 0 for x in [length, area, head_loss, time]):
            return "Length, area, head loss, and time must all be positive."
        k = (length * area) / (time * head_loss)
        return round(k, 6)
    except Exception as e:
        return f"Error: {e}"

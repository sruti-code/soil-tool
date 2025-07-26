def calculate_consolidation(strain, time_initial, time_final):
    try:
        if strain <= 0:
            return "Strain must be positive."
        if time_final <= time_initial:
            return "Final time must be greater than initial time."
        cv = strain / (time_final - time_initial)
        return round(cv, 4)
    except Exception as e:
        return f"Error: {e}"

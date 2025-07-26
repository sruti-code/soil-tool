def calculate_consolidation(strain_cm, time_start_min, time_end_min):
    try:
        if strain_cm <= 0:
            return "Strain must be a positive number."
        if time_end_min <= time_start_min:
            return "Final time must be greater than initial time."
        
        time_diff = time_end_min - time_start_min
        cv = strain_cm / time_diff  # Cv in cm/min
        return round(cv, 4)
    except Exception as e:
        return f"Error: {e}"

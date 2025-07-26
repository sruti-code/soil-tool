def calculate_percent_finer(total_weight, retained_weights):
    try:
        if total_weight <= 0:
            return "Total weight must be positive."
        if not retained_weights or any(w < 0 for w in retained_weights):
            return "Retained weights must be a list of non-negative values."
        if sum(retained_weights) > total_weight:
            return "Retained weight cannot exceed total sample weight."
        cumulative_retained = sum(retained_weights)
        percent_finer = 100 - ((cumulative_retained / total_weight) * 100)
        return round(percent_finer, 2)
    except Exception as e:
        return f"Error: {e}"

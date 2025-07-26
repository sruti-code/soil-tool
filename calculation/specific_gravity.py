# for calculating the specific gravity of soil.

def calculate_specific_gravity(weight_dry, weight_submerged, weight_container):
    try:
        if weight_dry <= 0 or weight_submerged <= 0 or weight_container < 0:
            return "All weights must be positive, and container weight should be non-negative."
        denominator = weight_dry - weight_submerged - weight_container
        if denominator <= 0:
            return "Invalid: denominator for specific gravity is zero or negative."
        specific_gravity = weight_dry / denominator
        return round(specific_gravity, 3)
    except Exception as e:
        return f"Error: {e}"

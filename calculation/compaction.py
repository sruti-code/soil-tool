def calculate_compaction(weight_mold_wet, weight_mold, volume_mold, moisture_content):
    try:
        # Input validation
        if weight_mold_wet <= 0 or weight_mold <= 0 or volume_mold <= 0:
            return "All weights and mold volume must be positive."
        if moisture_content < 0:
            return "Moisture content cannot be negative."

        # Calculations
        wet_density = (weight_mold_wet - weight_mold) / volume_mold
        if wet_density <= 0:
            return "Wet density calculation resulted in a non-positive value."

        dry_density = wet_density / (1 + (moisture_content / 100))

        return {
            "wet_density": round(wet_density, 2),
            "dry_density": round(dry_density, 2)
        }

    except Exception as e:
        return f"Error during calculation: {e}"


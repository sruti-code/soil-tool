def calculate_compaction(weight_mold_wet, weight_mold, volume_mold, moisture_content):
    try:
        if any(val <= 0 for val in [weight_mold_wet, weight_mold, volume_mold]):
            return "Weights and mold volume must be positive."
        if moisture_content < 0:
            return "Moisture content cannot be negative."
        wet_density = (weight_mold_wet - weight_mold) / volume_mold
        if wet_density <= 0:
            return "Wet density must be positive."
        dry_density = wet_density / (1 + (moisture_content / 100))
        return {
            "wet_density": round(wet_density, 2),
            "dry_density": round(dry_density, 2)
        }
    except Exception as e:
        return f"Error: {e}"

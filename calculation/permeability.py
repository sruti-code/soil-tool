def calculate_constant_head_permeability(length, area, head_loss, time):
    """
    K = (Q * L) / (A * h * t)
    Q = volume of water collected (cm^3)
    L = length of soil sample (cm)
    A = cross-sectional area of soil sample (cm^2)
    h = head loss (cm)
    t = time (s)
    Returns permeability coefficient K (cm/s)
    """
    try:
        if area <= 0 or length <= 0 or head_loss <= 0 or time <= 0:
            return "All values must be positive."
        Q = area * head_loss  # For demonstration, Q can be measured separately in real tests
        K = (Q * length) / (area * head_loss * time)
        return round(K, 6)
    except Exception as e:
        return f"Error: {e}"

def calculate_falling_head_permeability(a, A, L, t, h1, h2):
    """
    K = (a * L) / (A * t) * ln(h1/h2)
    a = area of standpipe (cm^2)
    A = area of soil sample (cm^2)
    L = length of soil sample (cm)
    t = elapsed time (s)
    h1 = initial head (cm)
    h2 = final head (cm)
    Returns permeability coefficient K (cm/s)
    """
    import math
    try:
        if a <= 0 or A <= 0 or L <= 0 or t <= 0 or h1 <= 0 or h2 <= 0:
            return "All values must be positive."
        if h2 >= h1:
            return "Final head (h2) must be less than initial head (h1)."
        K = (a * L) / (A * t) * math.log(h1 / h2)
        return round(K, 6)
    except Exception as e:
        return f"Error: {e}" 
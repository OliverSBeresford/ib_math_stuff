def calc_pi(terms: int) -> float:
    """Calculate an approximation of Pi using the Leibniz formula.

    Args:
        terms (int): The number of terms to include in the approximation.

    Returns:
        float: The approximate value of Pi.
    """
    pi_over_4 = 0.0
    for k in range(terms):
        pi_over_4 += ((-1) ** k) / (2 * k + 1)
    
    return pi_over_4 * 4

print(calc_pi(10000000))
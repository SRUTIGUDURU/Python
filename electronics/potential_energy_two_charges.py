from __future__ import annotations

k_e = 8.99 * (10**9)  # N·m²/C², Coulomb's constant
# Reference:
# https://phys.libretexts.org/Bookshelves/University_Physics/
# University_Physics_(OpenStax)/University_Physics_II_-_Thermodynamics_
# Electricity_and_Magnetism_(OpenStax)/07%3A_Electric_Potential/7.02%3A_
# Electric_Potential_Energy


def potential_energy_2_charges(
    charge_1: float,
    charge_2: float,
    distance: float,
) -> float:
    """
    Calculate the potential energy due to two charges.

    Parameters:
    - charge_1 (float): The charge in Coulombs.
    - charge_2 (float): The charge in Coulombs.
    - distance (float): The distance between the charges in meters.

    Returns:
    - float: The potential energy.

    Raises:
    - ValueError: If distance is less than zero.

    Examples:
    >>> potential_energy_2_charges(1e-6, 1e-6, 0.01)
    899000.0
    >>> potential_energy_2_charges(2e-6, 3e-6, 0.05)
    1078800.0
    >>> potential_energy_2_charges(0, 3e-6, 0.05)
    0
    >>> potential_energy_2_charges(2e-6, 3e-6, 0)
    inf
    >>> potential_energy_2_charges(2e-6, 3e-6, -0.05)
    Traceback (most recent call last):
        ...
    ValueError: Distance cannot be less than zero.
    """
    if charge_1 == 0 or charge_2 == 0:
        return 0
    elif distance == 0:
        return float("inf")
    elif distance < 0:
        raise ValueError("Distance cannot be less than zero.")
    else:
        potential_energy = k_e * charge_1 * charge_2 / distance
        return potential_energy


if __name__ == "__main__":
    import doctest

    doctest.testmod()

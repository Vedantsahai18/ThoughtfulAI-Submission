def sort(width, height, length, mass):
    """
    Determines the stack where the package should go based on its dimensions and mass.

    Parameters:
    - width (int/float): Width of the package in centimeters.
    - height (int/float): Height of the package in centimeters.
    - length (int/float): Length of the package in centimeters.
    - mass (int/float): Mass of the package in kilograms.

    Returns:
    - str: The name of the stack ("STANDARD", "SPECIAL", or "REJECTED").
    """
    # Calculate the volume of the package
    volume = width * height * length

    # Determine if the package is bulky or heavy
    bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    heavy = mass >= 20

    # Sort into appropriate stack
    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

# Example test cases
if __name__ == "__main__":
    # Standard package
    print(sort(50, 50, 50, 5))  # Output: "STANDARD"
    # Special package (bulky)
    print(sort(200, 50, 50, 5))  # Output: "SPECIAL"
    # Special package (heavy)
    print(sort(50, 50, 50, 25))  # Output: "SPECIAL"
    # Rejected package (bulky and heavy)
    print(sort(200, 200, 200, 25))  # Output: "REJECTED"

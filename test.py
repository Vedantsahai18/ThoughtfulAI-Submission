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

    # Check if the package is bulky
    if volume >= 1_000_000 or max(width, height, length) >= 150:
        # Check if the package is also heavy
        if mass >= 20:
            return "REJECTED"
        return "SPECIAL"
    
    # Check if the package is heavy
    if mass >= 20:
        return "SPECIAL"
    
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
    # Edge case: exactly at the bulky threshold
    print(sort(100, 100, 100, 5))  # Output: "SPECIAL"
    # Edge case: exactly at the heavy threshold
    print(sort(50, 50, 50, 20))  # Output: "SPECIAL"
    # Edge case: exactly at both thresholds
    print(sort(100, 100, 100, 20))  # Output: "REJECTED"
    # Edge case: large dimension but not bulky
    print(sort(150, 10, 10, 5))  # Output: "SPECIAL"

# ThoughtfulAI-Submission

## Objective

This project is designed to implement a function for Thoughtful's robotic automation factory. The function sorts packages into different stacks based on their volume and mass, ensuring efficient handling and dispatching.

## Sorting Criteria

Packages are sorted using the following criteria:

- **Bulky**: A package is considered bulky if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or if any of its dimensions is greater than or equal to 150 cm.
- **Heavy**: A package is considered heavy if its mass is greater than or equal to 20 kg.

### Stacks

- **STANDARD**: Packages that are neither bulky nor heavy.
- **SPECIAL**: Packages that are either bulky or heavy.
- **REJECTED**: Packages that are both bulky and heavy.

## Implementation

The function `sort(width, height, length, mass)` determines the appropriate stack for a package based on its dimensions and mass.

### Function Signature

```python
def sort(width, height, length, mass):
    # Implementation here
```

## Usage

To use the function, simply call it with the package's dimensions and mass:

```python
result = sort(50, 50, 50, 5)
print(result)  # Output: "STANDARD"
```

## Testing

The function can be tested using the provided test cases in the script. To run the tests, execute the script in a Python environment:

```bash
python your_script_name.py
```

### Example Test Cases

- **Standard Package**: `sort(50, 50, 50, 5)` should return `"STANDARD"`.
- **Special Package (Bulky)**: `sort(200, 50, 50, 5)` should return `"SPECIAL"`.
- **Special Package (Heavy)**: `sort(50, 50, 50, 25)` should return `"SPECIAL"`.
- **Rejected Package**: `sort(200, 200, 200, 25)` should return `"REJECTED"`.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

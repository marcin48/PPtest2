def to_binary(number):
    """Convert natural number in range 0–100 to binary."""
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    if not (0 <= number <= 100):
        raise ValueError("Number must be between 0 and 100")
    return bin(number)

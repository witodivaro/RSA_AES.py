

def egcd(a, b):
    """Calculate Greatest Common Divisor using Eucledian Algorithm

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: GCD
        dict: GCD hash
    """

    (number, base) = (a, b)
    gcd_hash = {}

    div = number // base
    mod = number % base

    gcd_hash[number] = {
        base: div,
    }

    while (mod):
        gcd_hash[number][mod] = 1

        number = base
        base = mod

        div = number // base
        mod = number % base

        gcd_hash[number] = {
            base: div,
        }

    return base, gcd_hash

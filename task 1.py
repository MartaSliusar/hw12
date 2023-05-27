def difference(*args):
    if not args:
        return 0

    numbers = list(args)
    n1 = min(numbers)
    n2 = max(numbers)
    diff = n2 - n1
    return diff

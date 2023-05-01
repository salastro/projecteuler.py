from math import log

def largest_exponential(file: str) -> int:
    """Return the line number of the pair with the largest exponential."""
    # parse the file into a tuple
    with open(file, 'r') as f:
        pairs = tuple([tuple(map(int, line.split(','))) for line in f])

    # multiply the exponent by the log of the base
    logs = [pair[1] * log(pair[0]) for pair in pairs] # list of logs
    return logs.index(max(logs)) + 1 # return the line number

print(largest_exponential('data/p099_base_exp.txt'))

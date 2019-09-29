from functools import reduce


def pipe(functions, initial):
    return reduce(lambda input, function: function(input), functions, initial)

#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = [0, 0]

    for ind in range(0, 2):
        result[ind] = 0
        result[ind] += sum(
            [tup[ind] if len(tup) > ind else 0 for tup in [tuple_a, tuple_b]]
            )

    return tuple(result)

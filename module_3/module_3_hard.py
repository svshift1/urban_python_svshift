def calculate_structure_sum(d):
    if isinstance(d, (int, float, complex)):
        return d
    elif isinstance(d, str):
        return len(d)
    elif isinstance(d, dict):
        s: int = 0
        for it in d.items():
            # it == (key, value)
            s += calculate_structure_sum(it[0]) + calculate_structure_sum(it[1])
        return s
    elif hasattr(d, '__iter__'):
        s: int = 0
        for it in d:
            s += calculate_structure_sum(it)
        return s
    else:
        return 0


data_structure = [
    [(-1)**0.5, 2, 3], # с комплексной 1j так смешнее.
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

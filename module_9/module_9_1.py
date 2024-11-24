
def apply_all_func(int_list:list[int|float], *functions) -> dict[str,int|float]:
    res={}
    for f in functions:
        res[f.__name__] = f(int_list)
    return res


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
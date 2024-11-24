
def add_everything_up(a: (int, float, str), b: (int, float, str)) -> (int, float, str):
    try:
        return a + b
    except TypeError as e:
        #print(e, f"a={a} b={b}")
        if isinstance(a, str) or isinstance(b, str):
            return str(a) + str(b)
        else:
            return None

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
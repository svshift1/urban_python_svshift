def get_matrix(n, m, val):
    # return [[val]*m]*n   # :-)
    a = []
    for i in range(n):
        a.append([])
        for j in range(m):
            a[i].append(val)
    return a


print(get_matrix(3, 3, 10))
print(get_matrix(3, 5, -1))

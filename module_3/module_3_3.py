def print_params(a=1, b='строка', c=True):
    print(f"a={a}\nb={b}\nc={c}")

print("без аргументов:")
print_params()
print("-------\n:print_params(b='два')")
print_params(b='два')
print("-------\n:print_params('два')")
print_params('два')
print("-------\n:print_params(1,'два')")
print_params(1,'два')
print("-------\n:print_params(c = [1,2,3])")
print_params(c = [1,2,3])
print("-------\n:lst=[1, 'два', True]; print_params(*lst)")
lst=[1, 'два', True]; print_params(*lst)
print("-------\n:dik={'a':True, 'b':'два', 'c':'1'}; print_params(**dik)")
dik={'a':True, 'b':'два', 'c':'1'}; print_params(**dik)
print("-------\n:dik2={'a':True, 'c':'1'}; print_params(**dik2)")
dik2={'a':True,  'c':'1'}; print_params(**dik2)
print("-------\n:lst2=[1, 'два']; print_params(*lst2)")
lst2=[1, 'два']; print_params(*lst2)
print("-------\n:lst3=[1, 'два']; print_params(*lst3,3)")
lst3=[1, 'два']; print_params(*lst3,3)


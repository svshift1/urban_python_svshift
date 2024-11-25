from pprint import pprint
import inspect

# это 'hard' задание 5го модуля. там есть что интраспектировать
from urtube import *


def introspection_info(obj) -> dict :
    res=dict()
    res['type']=type(obj).__name__
    if hasattr(obj, '__dict__'):
        res['attributes']=list(vars(obj).keys())
    else:
        res['attributes'] = []
    res['methods']=[ p[0] for p in inspect.getmembers(obj) if not p[0].startswith('__') and not p[0].endswith('__')]
    # большинство из этого -- дефолтные реализации унаследованные от object
    res['operators']=[ p[0] for p in inspect.getmembers(obj) if  p[0].startswith('__') and p[0].endswith('__')]
    res['module']= inspect.getmodule(type(obj)).__name__
    # if inspect.isclass(type(obj)):
    res['isobject']=True
    res['parents']=[ t.__name__ for t in type(obj).__bases__]
    # else:
    #     res['isobject']=False  # такого еще ни резу не было
    #     res['parents']=[]

    return res


obj = UrTube()
pprint(introspection_info(obj))
print('------')
pprint(introspection_info(42))
print('------')
pprint(introspection_info("С мягким знаком!"))
print('======')
# pprint(dir(type(42)))  -- (42).denominator !!!


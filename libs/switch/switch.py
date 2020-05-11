from functools import update_wrapper
from types import MappingProxyType
from typing import Hashable, Callable, Union 

def switch(key: Union[int, str]) -> Callable:

    def decorate(func: Callable) -> Callable:
        registry = {}

        def dispatch(key: Hashable) -> Callable:
            try:
                impl = registry[key]
            except KeyError:
                impl = registry[object]

            return impl 

        def register(key: Hashable, func: Callable=None) -> Callable:
            if func is None:
                return lambda f: register(key, f)

            registry[key] = func 
            return func 

        def wrapper_index(*args, **kw):
            return dispatch(args[key])(*args, **kw)

        def wrapper_keyword(*args, **kw):
            return dispatch(kw[key])(*args, **kw)

        registry[object] = func 
        if isinstance(key, int):
            wrapper = wrapper_index
        elif isinstance(key, str):
            wrapper = wrapper_keyword
        else:
            raise KeyError('The key must be int or str')

        wrapper.register = register 
        wrapper.dispatch = dispatch
        wrapper.registry = MappingProxyType(registry)
        update_wrapper(wrapper, func)

        return wrapper 

    return decorate 

"""
def handle_case(case):
    if case == 1:
        print('case 1')
    elif case == 2:
        print('case 2')
    else:
        print('default case')
"""

@switch(key=str("general"))
def handle_case(case):
    print('default case')

@handle_case.register(str("one"))
def _(case):
    print('case 1')

@handle_case.register(str("two"))
def _(case):
    print('case 2')

def main():
    handle_case(str("one"))
    handle_case(str("two"))
    handle_case(str("default"))

if __name__ == '__main__':
    main()

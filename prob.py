from inspect import getmembers, isfunction, ismethod
import types


def introspection_info(obj):
    info = {}


    info['type'] = type(obj).__name__


    info['attributes'] = [attr for attr in dir(obj) if not attr.startswith('__')]


    info['methods'] = [m[0] for m in getmembers(obj, predicate=callable) if ismethod(m[1]) or isfunction(m[1])]


    if hasattr(obj, '__module__'):
        info['module'] = obj.__module__
    else:
        info['module'] = '__main__'  # Default if module information is not available

    return info



number_info = introspection_info(42)
print(number_info)
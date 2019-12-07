import constants
import os

import log
import shared
import random


def enforce_types(*types, return_type=None):
    def decorator(f):
        def new_f(*args, **kwds):
            # we need to convert args into something mutable
            for (a, t) in zip(args, types):
                if not isinstance(a, t):
                    raise TypeError(" [Enforced Types]: Arguments of wrong type passed to function")
                # feel free to have more elaborated convertion
            result = f(*args, **kwds)
            if return_type:
                if not isinstance(result, return_type):
                    raise TypeError(
                        f" [Enforced Types]: Function returned wrong type \n Expected {repr(return_type)}. Received {type(result)} ")

            return result

        return new_f

    return decorator



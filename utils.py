from colorama import Fore

import constants
import os

import log
import shared
import random
import colorama


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


def colorprint(*args, **kwargs):
    foreground = kwargs.get('foreground', None)
    background = kwargs.get('background', None)
    style = kwargs.get('style', None)
    end = "\n"
    if "end" in kwargs:
        end = kwargs['end']

    message = " ".join([str(arg) for arg in args])

    print(foreground, end="") if foreground else ""
    print(background, end="") if background else ""
    print(style, end="") if style else ""
    print(message, end=end)
    print(colorama.Style.RESET_ALL, end=end)


def get_numerical_choice(inp_string, start, end):
    choice = input(inp_string)
    try:
        choice = int(choice)
    except ValueError:
        colorprint("Enter a valid choice", foreground=Fore.RED)
        return get_numerical_choice(inp_string, start, end)

    if not start <= choice <= end:
        colorprint("Enter a valid choice", foreground=Fore.RED)
        return get_numerical_choice(inp_string, start, end)

    return choice


def get_choice(inp_string, validator):
    choice = input(inp_string)

    if not validator(choice):
        colorprint("Enter a valid choice", foreground=Fore.RED)
        return get_choice(inp_string, validator)

    return choice

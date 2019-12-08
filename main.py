import constants
import shared
import utils
from colorama import Fore, Back, Style
import getpass
import router
import api


def init():
    utils.colorprint("Welcome to Gringotts CLI", foreground=Fore.LIGHTBLUE_EX)
    utils.colorprint("Login:", foreground=Fore.LIGHTYELLOW_EX)
    utils.colorprint("email:", foreground=Fore.LIGHTYELLOW_EX, end=" ")
    # email = input()
    # password = getpass.getpass(Fore.LIGHTYELLOW_EX + "password: ")

    try:
        router.main_router_loop()
    except KeyboardInterrupt:
        utils.colorprint("\n Thank you for visiting", foreground=Fore.GREEN)
    # api.login(email, password)


if __name__ == "__main__":
    init()

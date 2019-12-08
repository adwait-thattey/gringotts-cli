import log
import constants
import shared
import api
import utils
from colorama import Fore, Back, Style
import creds


def get_engines_route_input(cur_route="", route_key=""):
    engines_data = api.make_authenticated_request(url="engine")
    shared.ENGINES_DATA = engines_data
    utils.colorprint("The following types are available:", foreground=Fore.BLUE)
    print("1. Credentials \n2. AWS \n3. SSH")
    choice = utils.get_numerical_choice("Enter choice: ", start=1, end=3)
    chosen_type = ""
    if choice == 1:
        chosen_type = "kv"
    elif choice == 2:
        chosen_type = "aws"
    elif choice == 3:
        chosen_type = "ssh"

    utils.colorprint("The Following Engines are available:", foreground=Fore.BLUE)
    chosen_type_engines = [e for e in engines_data if e["type"] == chosen_type]
    eng_names = [e["name"] for e in chosen_type_engines]
    print(eng_names)
    chosen_eng = utils.get_choice(inp_string="Enter Engine Name: ", validator=lambda ee: ee in eng_names)

    if chosen_type == "kv": chosen_type = "creds"

    return f"{chosen_type}/{chosen_eng}"


def cred_route_parser(cur_route, route_parts):
    if len(route_parts) == 2:
        log.debug("Select cred category")
        return creds.select_categories(cur_route=cur_route, eng_name=route_parts[-1])

    if len(route_parts) == 3:
        log.debug("Select secret and get value")
        return creds.get_secret(cur_route=cur_route, eng_name=route_parts[-2], category_name=route_parts[-1])

def route_parser(inp_route=""):
    utils.colorprint(f"Current Route: {inp_route} ", foreground=Fore.BLUE)
    route_parts = inp_route.strip('/').split('/')

    if len(route_parts) < 2:
        log.debug("Engine not in route", module="router")
        return get_engines_route_input()

    if route_parts[0] == "creds":
        return cred_route_parser(inp_route, route_parts)


def main_router_loop():
    utils.colorprint("Enter the route to go directly go deep else press enter to start from default",
                     foreground=Fore.LIGHTBLUE_EX)
    route_to = input("Enter Route: ")
    exit = False

    while not exit:
        route_to = route_parser(route_to)

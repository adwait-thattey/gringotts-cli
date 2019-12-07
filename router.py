import log
import constants
import shared


def get_route_input():
    pass


def main_router_loop():
    route_to = ""
    exit = False

    while not exit:
        if not route_to:
            route_to = get_route_input()

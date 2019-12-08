import constants
import log
import shared
import utils
import api
from colorama import Fore, Back, Style
from os.path import join as path_join


def select_categories(cur_route, eng_name):
    cur_engine = [eng for eng in shared.ENGINES_DATA if eng["name"] == eng_name][0]
    categories = cur_engine["categories"]
    cat_names = [c["name"] for c in categories]
    print("Following categories are available")
    print(cat_names)
    chosen_cat = utils.get_choice(inp_string="Choose category: ", validator=lambda c: c in cat_names)

    return path_join(cur_route, chosen_cat)


def get_secret(cur_route, eng_name, category_name):
    cur_engine = [eng for eng in shared.ENGINES_DATA if eng["name"] == eng_name][0]
    cur_cat = [cat for cat in cur_engine["categories"] if cat["name"] == category_name][0]
    log.debug(cur_cat)
    input()


    return ""

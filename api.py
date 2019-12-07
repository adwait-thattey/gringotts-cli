import constants
import log
import shared


def make_unauthenticated_request(**kwargs):
    url = kwargs['url']
    type = kwargs.get('request_type', "get")
    payload = kwargs.get('payload', None)
    custom_headers = kwargs.get('headers', None)


def make_authenticated_request(**kwargs):
    url = kwargs['url']
    type = kwargs.get('request_type', "get")
    payload = kwargs.get('payload', None)
    custom_headers = kwargs.get('headers', None)

    if shared.CUR_USER_TOKEN is None:
        raise ConnectionAbortedError("User is not logged in")

    # while making request also put shared.CUR_USER_TOKEN in payload

def login():
    # take username and password in input
    # put in payload and send an unauthenticated request to server to get token
    # store token as shared.CUR_USER_TOKEN
    pass


def logout():
    shared.CUR_USER_TOKEN = None

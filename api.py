import constants
import log
import shared
import utils
from colorama import Fore, Back, Style
import requests
from requests.exceptions import HTTPError
from urllib.parse import urljoin


def make_unauthenticated_request(**kwargs):
    url = kwargs['url']
    abs_url = urljoin(constants.SERVER_ADDR, url)
    print(abs_url)
    type = kwargs.get('request_type', "get")
    payload = kwargs.get('payload', {})
    custom_headers = kwargs.get('headers', {})
    response = None
    try:

        if type == 'get':
            response = requests.get(abs_url,
                                    headers=custom_headers,
                                    json=payload
                                    )
        else:
            print('type: post')
            response = requests.post(abs_url, headers=custom_headers, json=payload)

            # If the response was successful, no Exception will be raised
            response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!')

    # response = requests.post('url', json={})
    json_response = response.json()
    # json_response['data']

    # repository = json_response['items'][0]

    # json_response['headers']['Content-Type']
    return json_response


def make_authenticated_request(**kwargs):
    url = kwargs['url']
    abs_url = urljoin(constants.SERVER_ADDR, url)
    type = kwargs.get('request_type', "get")
    payload = kwargs.get('payload', None)
    custom_headers = kwargs.get('headers', {})

    if shared.CUR_USER_TOKEN is None:
        raise ConnectionAbortedError("User is not logged in")

    custom_headers['auth-token'] = shared.CUR_USER_TOKEN
    # while making request also put shared.CUR_USER_TOKEN in header

    try:
        if type.lower() == "get":
            response = requests.get(abs_url,
                                    headers=custom_headers,
                                    json=payload,
                                    )
        else:
            response = requests.post(abs_url,
                                     headers=custom_headers,
                                     json=payload,
                                     )
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!')

    # response = requests.post('url', json={})
    json_response = response.json()
    # json_response['data']

    # repository = json_response['items'][0]

    # json_response['headers']['Content-Type']
    return json_response


def login(email, password):
    # take username and password in input
    # put in payload and send an unauthenticated request to server to get token
    # store token as shared.CUR_USER_TOKEN
    payload = {
        "email": email,
        "password": password
    }
    url = "auth/login"
    abs_url = urljoin(constants.SERVER_ADDR, url)
    print(abs_url)

    response = requests.post(abs_url, json=payload)
    if response.status_code != 200:
        utils.colorprint("Either username or password is incorrect", foreground=Fore.RED)
        return None

    btoken = response.content
    token = btoken.decode()
    login_header = f"Bearer {token}"
    shared.CUR_USER_TOKEN = login_header
    print(shared.CUR_USER_TOKEN)
    utils.colorprint("Login Success", foreground=Fore.GREEN)


def logout():
    shared.CUR_USER_TOKEN = None


if __name__ == "__main__":
    requrl = 'https://jsonplaceholder.typicode.com/todos/1'
    response = make_unauthenticated_request(url=requrl)
    # response = make_authenticated_request(url=requrl)
    print(response)

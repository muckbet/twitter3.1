import urllib.request, urllib.parse, urllib.error
from docs import twurl
import json
import ssl


def ignore_ssl_er():
    """
    (None) -> <class 'ssl.SSLContext'>

    Return a new SSLContext object with some settings.
    """
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


def get_user_name():
    """
    (None) -> str

    Return the name of person that we want to find
    """
    print()
    account = input('Enter Twitter Account: ')
    if len(account) < 1:
        return False
    print(account)
    return account


def create_get_request(account):
    """
    (str) -> str

    Return created GET request
    """
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
    # get url
    url = twurl.augment(TWITTER_URL, {'screen_name': account})
    return url


def get_url_data(url, ctx):
    """
    () -> <class 'http.client.HTTPResponse'>, str

    Return client HTTP response and information about friends
    """
    # connection = client HTTP response
    connection = urllib.request.urlopen(url, context=ctx)
    # data = all the info in str
    data = connection.read().decode()
    return connection, data


def data_to_json_file(path, data):
    """
    (str, str) -> None

    Data to json file
    """
    f = open(path, "w+")
    f.write(data)
    f.close()


def from_json_file_info(path):
    """
    (str) -> dict

    Return dictionary with data from JSON file
    """
    f = open(path, encoding='utf-8')
    info = json.load(f)
    f.close()
    return info


def main(name):
    """
    (None) -> dict

    Call all the functions
    Return names with their location names
    """
    ctx = ignore_ssl_er()
    twitter_account = name
    if not twitter_account:
        return False
    try:
        url = create_get_request(twitter_account)
        connection, data = get_url_data(url, ctx)
    except:
        return False
    path = "./temporary_files/friends_data.json"
    data_to_json_file(path, data)
    json_dict = from_json_file_info(path)
    return json_dict

import requests as rq
import sys
import getpass
from github import Github
from datetime import datetime


def isValid_username(username: str):
    """
    Check is given username is a valid account name or not
    :param username:
    :return:
    """
    query = f"https://api.github.com/users/{username}"
    response = rq.get(query)
    return response.status_code == 200


def login_github(username: str, password: str):
   """
   Login into github account
   :param username:
   :param password:
   :return:
   """
   
   pass


def main():
    username = input("Enter your github  username: ").strip()

    if isValid_username(username):
        print("SUCCESS: Valid github username", file=sys.stdout)
    else:
        print("ERROR: Invalid github username", file=sys.stderr)
        sys.exit(1)
    login_passcode = getpass.getpass("Enter password(to login into github): ")

    
if __name__=="__main__":
    main()

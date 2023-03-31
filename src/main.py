from fectch_commit_data import sendQuery
import requests
import sys
import datetime


def isValid_username(username: str):
    """
    Check is given username is a valid account name or not
    :param username:
    :return:
    """
    query = f"https://api.github.com/users/{username}"
    response = requests.get(query)
    return response.status_code == 200



def getCommitData(username, date, password=None):
    return sendQuery(username, date)

def getDate():
    # @TODO: later we may try to fetch the periods with most number of commits 
    current_date = datetime.datetime.now()  # get current date 
    to_date_str = current_date.isoformat(timespec="seconds")+'Z'
    from_date = current_date - datetime.timedelta(days=365)
    from_date_str = from_date.isoformat(timespec="seconds")+'Z'

    return (from_date_str, to_date_str)



def main():
    username = input("Enter your github  username: ").strip()

    if isValid_username(username):
        print("SUCCESS: Valid github username", file=sys.stdout)
    else:
        print("ERROR: Invalid github username", file=sys.stderr)
        sys.exit(1)

    # login_passcode = getpass.getpass("Enter password(to login into github): ")
    data = getCommitData(username, getDate())
    print(data)






if __name__=="__main__":
    main()

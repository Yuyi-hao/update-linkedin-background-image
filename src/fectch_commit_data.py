import requests
import configparser


# retrieving access token from .ini file 
config = configparser.ConfigParser()
config.read("credentials/credentials.ini")
access_token = config.get('github', 'github_access_token').strip()
# lets hardcode the access token 
access_token = "random"


URL = "https://api.github.com/graphql"  # Base url for github api 

query = """
    query($userName:String!, $from:DateTime!, $to:DateTime!) { 
      user(login: $userName){
        contributionsCollection(from: $from, to:$to){
          contributionCalendar{
            totalContributions
            weeks {
              contributionDays {
                contributionCount
                date
              }
            }
          }
        }
      }
    }
"""



def sendQuery(username, date):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github.v4+json"
    }
    variables = {
        'userName': username,
        'from': date[0],
        'to': date[1]
    }

    response = requests.post(
        URL, 
        json={
            'query': query, 
            'variables': variables
        }, 
        headers=headers)
    if response.status_code == 200:
        data = response.json()['data']['user']['contributionsCollection']['contributionCalendar']
        total_commit = data['totalContributions']
        commit_list = []
        for week in data['weeks']:
            for day in week['contributionDays']:
                    commit_list.append(day['contributionCount'])
        
        return commit_list, date
    else:
        return response.json()
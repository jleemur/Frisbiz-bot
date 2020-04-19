from os import getenv
from dotenv import load_dotenv
from random import shuffle
import requests

# get environment from .env file
load_dotenv()
RIOT_API_KEY = getenv('RIOT_API_KEY')

RIOT_BASE_URL = "https://na1.api.riotgames.com/lol"
CHAMPIONS_BASE_URL = "http://ddragon.leagueoflegends.com/cdn/10.8.1"


def junkyard(p1, p2, p3, p4, p5):
    # list indexes for roles
    TOP, JG, MID, BOT, SUP = 0, 1, 2, 3, 4

    roles = [r.lower() for r  in [p1, p2, p3, p4, p5]]
    shuffle(roles)

    # calvin jungle nunu hack
    calvin_str = ""
    if 'calvin' in roles:
        calvin_index = roles.index('calvin')
        roles[calvin_index], roles[JG] = roles[JG], roles[calvin_index]
        calvin_str =  " (as nunu)"

    # flora support morgana hack
    flora_str = ""
    if 'flora' in roles:
        flora_index = roles.index('flora')
        roles[flora_index], roles[SUP] = roles[SUP], roles[flora_index]
        flora_str =  " (as morgana)"


    message = (
        f"Top: {roles[TOP]}\n"
        f"Jungle: {roles[JG]}{calvin_str}\n"
        f"Mid: {roles[MID]}\n"
        f"Bottom: {roles[BOT]}\n"
        f"Support: {roles[SUP]}{flora_str}\n"
    )
    return message


def memes(subreddit='leagueofmemes'):
    response = requests.get(f"https://meme-api.herokuapp.com/gimme/{subreddit}").json()

    if 'code' in response:
        # error
        message = f"{response['code']} - {response['message']}"
        return message
    else:
        # success
        return response['url']


def top_champions(name):
    summoner_url = f"{RIOT_BASE_URL}/summoner/v4/summoners/by-name/{name}?api_key={RIOT_API_KEY}"
    summoner_resp = requests.get(summoner_url).json()

    if 'status' in summoner_resp:
        # error
        message = summoner_resp['status']['message']
        return message

    # get champions data
    champions_url = f"{CHAMPIONS_BASE_URL}/data/en_US/champion.json"
    champions_resp = requests.get(champions_url).json()
    champions_data = champions_resp['data']
    champions = _map_champions_by_key(champions_data)

    # get summoner matchlist
    account_id = summoner_resp['accountId']
    matchlist_url = f"{RIOT_BASE_URL}/match/v4/matchlists/by-account/{account_id}?api_key={RIOT_API_KEY}"
    matchlist_resp = requests.get(matchlist_url).json()
    matchlist = matchlist_resp['matches']
    latest_champions = _get_champions_from_matchlist(matchlist)

    
    message = f"In the last {len(matchlist)} games, {name}'s top 5 champions played are:\n"
    for champion_key in list(latest_champions)[:5]:
        num_played = latest_champions[champion_key]
        message += f"{champions[champion_key]['name']}: {num_played}\n"
    return message


def _map_champions_by_key(champions_data):
    champions = {}
    for champion in champions_data.values():
        champions[int(champion['key'])] = champion
    return champions


def _get_champions_from_matchlist(matchlist):
    latest_champions = {}
    for match in matchlist:
        champion_key = match['champion']
        if champion_key in latest_champions:
            latest_champions[champion_key] += 1
        else:
            latest_champions[champion_key] = 1

    # sort by highest # played
    latest_champions_sorted = {k: v for k, v in sorted(latest_champions.items(), key=lambda latest_champions: latest_champions[1], reverse=True)}
    return latest_champions_sorted

import requests
from secret.riotapikey import RiotAPIKey

spellDictionaryById = {}
spellDictionaryByName = {}

def requestSpells():
    print('[riotapi/spell] request spells...')

    URL = "https://global.api.pvp.net/api/lol/static-data/euw/v1.2/summoner-spell?api_key=" + RiotAPIKey
    response = requests.get(URL)
    response.connection.close()
    response = response.json()

    print('[riotapi/champion] request spell success')

    return response

def updateSpellDictionary():
    response = requestSpells()
    global spellDictionaryById
    global spellDictionaryByName


    data = response['data']
    for spellName in data:
        spellDictionaryByName[spellName] = data[spellName]['id']
        spellDictionaryById[data[spellName]['id']] = spellName


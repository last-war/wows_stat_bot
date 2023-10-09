import json
import requests


"""
NFUA
https: // api.worldofwarships.eu/wows/clans/list /?application_id =  & fields = clan_id % 2Ctag & search ='+clantag
https: // api.worldofwarships.eu/wows/clans/accountinfo /?application_id =  & account_id = '+str(member)+' & extra = clan & fields = clan.tag
https: // clans.worldofwarships.eu/api/encyclopedia/vehicles_info /?lang = ru
https: // api.worldofwarships.eu/wows/clans/list /?application_id =  & search = '+clantag+' & fields = clan_id % 2C+tag
https://api.worldofwarships.eu/wows/clans/info/?application_id=&clan_id=+clan_id+&extra=members
https: // clans.worldofwarships.eu/api/members/'+clan_id+'/
https: // clans.worldofwarships.eu/api/members//
"""


class jsnBot:
    jsn_field = []

    def __init__(self, value):
        self.value = None
        self.validate(value)

    def validate(self, value):
        self.value = value

    def __contains__(self, item):
        return item in self.value

    def __str__(self):
        return f"{self.jsn_field}: {self.value}"


class playerInfo:
    # strukt
    def __init__(self, value):
        self.namePlayer = value
        
        
def get_clan_members(clan_id):
    x = requests.get('https://api.worldofwarships.eu/wows/clans/info/?application_id=&clan_id='+clan_id+'&extra=members')
        
def get_clan_id(clantag):
    x = requests.get('https://api.worldofwarships.eu/wows/clans/list/?application_id=&fields=clan_id%2Ctag&search='+clantag)
    return x.get('data').get('clan_id')

def main():
    #x = requests.get('https://clans.worldofwarships.eu/api/encyclopedia/vehicles_info/?lang=ru')
    clantag = 'NFUA'
    clan_id = '500229722'
    x = requests.get('https://api.worldofwarships.eu/wows/clans/list/?&fields=clan_id%2Ctag&search='+clantag)
    print(x.text)


if __name__ == '__main__':
    main()
    # main prog

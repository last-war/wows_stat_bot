import json
import requests

myWGappID = "9f2c3f9953a1084d88f94ca9ff78c06e"

"""
https: // api.worldofwarships.eu/wows/clans/list /?application_id = 9f2c3f9953a1084d88f94ca9ff78c06e & fields = clan_id % 2Ctag & search ='+clantag
https: // api.worldofwarships.eu/wows/clans/accountinfo /?application_id = 9f2c3f9953a1084d88f94ca9ff78c06e & account_id = '+str(member)+' & extra = clan & fields = clan.tag
https: // clans.worldofwarships.eu/api/encyclopedia/vehicles_info /?lang = ru
https: // api.worldofwarships.eu/wows/clans/list /?application_id = 9f2c3f9953a1084d88f94ca9ff78c06e & search = '+clantag+' & fields = clan_id % 2C+tag
https: // api.worldofwarships.eu/wows/clans/info /?application_id = 9f2c3f9953a1084d88f94ca9ff78c06e & clan_id = '+clan_id+' & extra = members
https: // clans.worldofwarships.eu/api/members/'+clan_id+'/
https: // clans.worldofwarships.eu/api/members/428592/
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


def main():
    x = requests.get(
        'https://clans.worldofwarships.eu/api/encyclopedia/vehicles_info/?lang=ru')
    print(x.text)


if __name__ == '__main__':
    main()
    # main prog

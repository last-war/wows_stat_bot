from dotenv import load_dotenv
import requests
import os


load_dotenv()


def get_id_by_name(name):
    link = f'https://{os.environ.get("URL")}?application_id={os.environ.get("MY_WG_APP_ID")}&search={name}&type=exact'
    rez = requests.get(link)
    if rez.status_code == 200:
        return rez.json().get('data')[0].get('account_id')

    return f"Error code:{rez.status_code}"

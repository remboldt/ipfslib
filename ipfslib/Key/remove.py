import json
import requests
from typing import List

# Removes IPNS key
def remove(api, key_name: str, extra_info: bool = False) -> List[dict]:
    params = {
        'arg': key_name,
        'l': extra_info 
    }
    response = requests.post('http://{endpoint}/api/v0/key/rm'.format(endpoint=api.endpoint), params=params)
    raw_json = response.text
    
    try:
        return json.loads(raw_json)['Keys']
    except KeyError:
        raise Exception(json.loads(raw_json)['Message'])
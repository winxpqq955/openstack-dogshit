import requests
import json

openstack_endpoint = "http://192.168.100.10"

body = {
    "auth": {
        "identity": {
            "methods": ["password"],
            "password": {
                "user": {
                    "id": "0befa70f767848e39df8224107b71858",
                    "password": "000000"
                }
            }
        },
        "scope": {
            "project": {
                "id": "f9ff39ba9daa4e5a8fee1fc50e2d2b34"
            }
        }
    }
}

headers = {}


def get_token():
    url = openstack_endpoint + ":5000/v3/auth/tokens"
    re = requests.post(url, headers=headers, data=json.dumps(body)).headers["X-Subject-Token"]
    return re


def flavor_create():
    url = openstack_endpoint + ":8774/v2.1/f9ff39ba9daa4e5a8fee1fc50e2d2b34/flavors"
    headers["X-Auth-Token"] = get_token()
    body2 = {
        "flavor": {
            "name": "balls",
            "id": 769394,
            "vcpus": 1,
            "ram": 2048,
            "disk": 40,
        }
    }
    re = requests.post(url, data=json.dumps(body2), headers=headers).json()
    return re


flavor_create()

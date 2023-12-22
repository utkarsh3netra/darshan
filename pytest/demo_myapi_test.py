import requests
import pytest

ENDPOINT = "https://90ovbrh4e6.execute-api.us-east-1.amazonaws.com/v1/darshan_test_api"

response = requests.get(ENDPOINT)
print(response)

data = response.json()
print(data)

status_code = response.status_code
print("status code: ", status_code)


def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
    pass
def test_can_create_endpoint():
    payload = {
        "name": "segment 12",
        "description": "test Segment 12",
        "where_condition": "segment==pytest",
        "update_time": " "
    }
    response = requests.post(ENDPOINT , json=payload)
    assert response.status_code == 200

    data = response.json()
    print(data)

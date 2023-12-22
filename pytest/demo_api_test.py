import requests

ENDPOINT = "https://todo.pixegami.io/"

def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
    pass


def test_can_create_task():
    payload = new_task_payload()
    create_response = create_task(payload)
    assert create_response.status_code == 200

    data = create_response.json()
    print(data)

    task_id = data["task"]["task_id"]
    get_response = get_task(task_id)

    assert get_response.status_code == 200
    get_data = get_response.json()
    assert get_data["content"] == payload["content"]
    assert get_data["user_id"] == payload["user_id"]

def test_can_update_task():
    payload = new_task_payload()
    create_response = create_task(payload)
    assert create_response.status_code == 200
    task_id = create_response.json()["task"]["task_id"]

    new_payload = {
        "user_id": payload["user_id"],
        "task_id": task_id,
        "content": "my update content",
        "is_done": True
    }
    update_responce = update_task(new_payload)
    assert update_responce.status_code == 200

    get_response = get_task(task_id)
    assert get_response.status_code == 200
    get_data = get_response.json()
    assert get_data['content'] == new_payload['content']
    assert get_data['is_done'] == new_payload['is_done']


def create_task(payload):
    return requests.put(ENDPOINT + "/Create-task", json=payload)

def update_task(payload):
    return requests.put(ENDPOINT + "/update-task", json=payload)

def get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")

def new_task_payload():
    return {
        "content": "my contest",
        "user_id": "test_user",
        "is_done": False,
        }
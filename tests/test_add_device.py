import requests
import json


def test_add_device():
    header = {'Content-Type': 'application/json'}
    body = {"DeviceName": "device_1"}
    response = requests.post('http://localhost:8080/device/add', data=json.dumps(body), headers=header)
    assert response.json() == 'Successfully added device - device_1!', 'Add device response incorrect!'
    assert response.status_code == 200, 'Add device status code incorrect!'


def test_add_device_exists():
    header = {'Content-Type': 'application/json'}
    body = {"DeviceName": "device_2"}
    requests.post('http://localhost:8080/device/add', data=json.dumps(body), headers=header)
    response = requests.post('http://localhost:8080/device/add', data=json.dumps(body), headers=header)
    assert response.json() == 'Device already exists!', 'Add device that exists response incorrect!'
    assert response.status_code == 400, 'Add device status code incorrect!'


def test_add_device_check():
    header = {'Content-Type': 'application/json'}
    body = {"DeviceName": "device_3"}
    response = requests.post('http://localhost:8080/device/add', data=json.dumps(body), headers=header)
    assert response.json() == 'Successfully added device - device_3!', 'Add device response incorrect!'
    assert response.status_code == 200, 'Add device status code incorrect!'

    reservation_response = json.dumps(str(requests.get('http://localhost:8080/reservation')))
    for i in range(len(reservation_response)):
        if 'device_3' == reservation_response[i][0]:
            assert reservation_response[i] == {
        "DeviceName": 'device_3',
        "ReservationStatus": "free",
        "ReservationPeriod": {
            "From": "none",
            "To": "none"
        },
        "ReservationOwner": "none"
    }


import requests
import json


def test_delete_device():
    header = {'Content-Type': 'application/json'}
    body = {"DeviceName": "device_del"}
    response = requests.post('http://localhost:8080/device/add', data=json.dumps(body), headers=header)
    assert response.json() == 'Successfully added device - device_del!', 'Add device response incorrect!'
    assert response.status_code == 200, 'Add device status code incorrect!'

    param = 'id=device_del'
    del_response = requests.delete('http://localhost:8080/device/del', params=param)
    assert del_response.json() == 'Removed device - device_del!', 'Delete device response incorrect!'
    assert del_response.status_code == 200, 'Delete device status code incorrect!'


def test_delete_device_not_found():
    param = 'id=device_not_found'
    del_response = requests.delete('http://localhost:8080/device/del', params=param)
    assert del_response.json() == 'Device not found!', 'Delete device response incorrect!'
    assert del_response.status_code == 404, 'Delete device status code incorrect!'


def test_delete_device_with_check():
    count = 0
    header = {'Content-Type': 'application/json'}
    body = {"DeviceName": "device_del_c"}
    response = requests.post('http://localhost:8080/device/add', data=json.dumps(body), headers=header)
    assert response.json() == 'Successfully added device - device_del_c!', 'Add device response incorrect!'
    assert response.status_code == 200, 'Add device status code incorrect!'

    param = 'id=device_del_c'
    del_response = requests.delete('http://localhost:8080/device/del', params=param)
    assert del_response.json() == 'Removed device - device_del_c!', 'Delete device response incorrect!'
    assert del_response.status_code == 200, 'Delete device status code incorrect!'

    reservations_res = json.dumps(str(requests.get('http://localhost:8080/reservation')))
    for i in range(len(reservations_res)):
        if 'device_del_c' == reservations_res[i][0]:
            count =+ 1

    assert count == 0, 'Device was not delete!'
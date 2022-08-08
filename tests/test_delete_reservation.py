import requests
import json


def test_delete_reservation():
    header = {'Content-Type': 'application/json'}
    body_device = {"DeviceName": "device_res_del"}
    response_add_d = requests.post('http://localhost:8080/device/add', data=json.dumps(body_device), headers=header)
    assert response_add_d.json() == 'Successfully added device - device_res_del!', 'Add device response incorrect!'
    assert response_add_d.status_code == 200, 'Add device status code incorrect!'

    body = {
        "DeviceName": "device_res_del",
        "ReservationStatus": "reserved",
        "ReservationPeriod": {
            "From": "2022-09-20",
            "To": "2022-09-25"
        },
        "ReservationOwner": "default_owner"
    }
    response = requests.post('http://localhost:8080/reservation/create', data=json.dumps(body), headers=header)
    assert response.json() == 'Reservation has been made!', 'Create reservation response incorrect!'
    assert response.status_code == 201, 'Create reservation status code incorrect!'

    body_del = {
        "DeviceName": "device_res_del",
        "ReservationPeriod": {
            "From": "2022-09-20",
            "To": "2022-09-25"
        },
        "ReservationOwner": "default_owner"
    }
    response_del = requests.delete('http://localhost:8080/reservation/cancel', data=json.dumps(body_del), headers=header)
    assert response_del.json() == 'Reservation has been canceled!', 'Cancel reservation response incorrect!'
    assert response_del.status_code == 200, 'Cancel reservation status code incorrect!'

def test_delete_reservation_not_found():
    header = {'Content-Type': 'application/json'}
    body_device = {"DeviceName": "device_res_del_not_found"}
    response_add_d = requests.post('http://localhost:8080/device/add', data=json.dumps(body_device), headers=header)
    assert response_add_d.json() == 'Successfully added device - device_res_del_not_found!', 'Add device response incorrect!'
    assert response_add_d.status_code == 200, 'Add device status code incorrect!'

    body_del = {
        "DeviceName": "device_res_del_not_found",
        "ReservationPeriod": {
            "From": "2022-09-20",
            "To": "2022-09-25"
        },
        "ReservationOwner": "default_owner"
    }
    response = requests.delete('http://localhost:8080/reservation/cancel', data=json.dumps(body_del), headers=header)
    assert response.json() == 'Reservation not found!', 'Cancel reservation not found response incorrect!'
    assert response.status_code == 404, 'Cancel reservation not found status code incorrect!'


def test_delete_reservation_check():
    header = {'Content-Type': 'application/json'}
    body_device = {"DeviceName": "device_res_del_check"}
    response_add_d = requests.post('http://localhost:8080/device/add', data=json.dumps(body_device), headers=header)
    assert response_add_d.json() == 'Successfully added device - device_res_del_check!', 'Add device response incorrect!'
    assert response_add_d.status_code == 200, 'Add device status code incorrect!'

    body = {
        "DeviceName": "device_res_del_check",
        "ReservationStatus": "reserved",
        "ReservationPeriod": {
            "From": "2022-09-20",
            "To": "2022-09-25"
        },
        "ReservationOwner": "default_owner"
    }
    response = requests.post('http://localhost:8080/reservation/create', data=json.dumps(body), headers=header)
    assert response.json() == 'Reservation has been made!', 'Create reservation response incorrect!'
    assert response.status_code == 201, 'Create reservation status code incorrect!'

    body_del = {
        "DeviceName": "device_res_del_check",
        "ReservationPeriod": {
            "From": "2022-09-20",
            "To": "2022-09-25"
        },
        "ReservationOwner": "default_owner"
    }
    response_del = requests.delete('http://localhost:8080/reservation/cancel', data=json.dumps(body_del), headers=header)
    assert response_del.json() == 'Reservation has been canceled!', 'Cancel reservation response incorrect!'
    assert response_del.status_code == 200, 'Cancel reservation status code incorrect!'

    res_del_for_check = json.dumps(str(response_del))
    for i in range(len(res_del_for_check)):
        if 'device_res_del_check' == res_del_for_check[i][0]:
            assert res_del_for_check[i] == {
                "DeviceName": "device_res_del_check",
                "ReservationStatus": "free",
                "ReservationPeriod": {
                    "From": "none",
                    "To": "none"
                },
                "ReservationOwner": "none"
            }

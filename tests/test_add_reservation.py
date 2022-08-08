import requests
import json


def test_add_reservation():
    header = {'Content-Type': 'application/json'}
    body_device = {"DeviceName": "device_res_new"}
    response_add_d = requests.post('http://localhost:8080/device/add', data=json.dumps(body_device), headers=header)
    assert response_add_d.json() == 'Successfully added device - device_res_new!', 'Add device response incorrect!'
    assert response_add_d.status_code == 200, 'Add device status code incorrect!'

    body = {
        "DeviceName": "device_res_new",
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


def test_add_reservation_check():
    header = {'Content-Type': 'application/json'}
    body_device = {"DeviceName": "device_res_new_c"}
    response_add_d = requests.post('http://localhost:8080/device/add', data=json.dumps(body_device), headers=header)
    assert response_add_d.json() == 'Successfully added device - device_res_new_c!', 'Add device response incorrect!'
    assert response_add_d.status_code == 200, 'Add device status code incorrect!'

    body = {
        "DeviceName": "device_res_new_c",
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

    res_for_check = json.dumps(str(response))
    for i in range(len(res_for_check)):
        if 'device_3' == res_for_check[i][0]:
            assert res_for_check[i] == {
        "DeviceName": "device_res_new_c",
        "ReservationStatus": "reserved",
        "ReservationPeriod": {
            "From": "2022-09-20",
            "To": "2022-09-25"
        },
        "ReservationOwner": "default_owner"
    }


def test_add_reservation_device_not_found():
    header = {'Content-Type': 'application/json'}
    body = {
        "DeviceName": "device_res_not_found",
        "ReservationStatus": "reserved",
        "ReservationPeriod": {
            "From": "2022-09-20",
            "To": "2022-09-25"
        },
        "ReservationOwner": "default_owner"
    }
    response = requests.post('http://localhost:8080/reservation/create', data=json.dumps(body), headers=header)
    assert response.json() == 'Device not found, reservation not made!',\
        'Create reservation device not found response incorrect!'
    assert response.status_code == 404, 'Create reservation device not found status code incorrect!'


def test_add_reservation_exists():
    header = {'Content-Type': 'application/json'}
    body_device = {"DeviceName": "device_res_exists"}
    response_add_d = requests.post('http://localhost:8080/device/add', data=json.dumps(body_device), headers=header)
    assert response_add_d.json() == 'Successfully added device - device_res_exists!', 'Add device response incorrect!'
    assert response_add_d.status_code == 200, 'Add device status code incorrect!'

    body = {
        "DeviceName": "device_res_exists",
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

    response_exists = requests.post('http://localhost:8080/reservation/create', data=json.dumps(body), headers=header)
    assert response_exists.json() == 'Device already reserved for period: 2022-09-20 - 2022-09-25. Reservation not made!', \
        'Create reservation that exists response incorrect!'
    assert response_exists.status_code == 400, 'Create reservation that exists status code incorrect!'


def test_add_reservation_after_other():
    header = {'Content-Type': 'application/json'}
    body_device = {"DeviceName": "device_res_2"}
    response_add_d = requests.post('http://localhost:8080/device/add', data=json.dumps(body_device), headers=header)
    assert response_add_d.json() == 'Successfully added device - device_res_2!', 'Add device response incorrect!'
    assert response_add_d.status_code == 200, 'Add device status code incorrect!'

    body = {
        "DeviceName": "device_res_2",
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

    body_2 = {
        "DeviceName": "device_res_2",
        "ReservationStatus": "reserved",
        "ReservationPeriod": {
            "From": "2022-09-26",
            "To": "2022-09-29"
        },
        "ReservationOwner": "default_owner_new"
    }
    response = requests.post('http://localhost:8080/reservation/create', data=json.dumps(body_2), headers=header)
    assert response.json() == 'Reservation has been made!', 'Create reservation response incorrect!'
    assert response.status_code == 201, 'Create reservation status code incorrect!'

import requests


def response_default():
    body = {
        "DeviceName": "default_device",
        "ReservationStatus": "reserved",
        "ReservationPeriod": {
            "From": "2022-08-05",
            "To": "2022-08-10"
        },
        "ReservationOwner": "default_owner"
    }
    return body

def test_get_reservations_list():
    response = requests.get('http://localhost:8080/reservationfgk')
    assert response.json()[0] == response_default(), 'Reservation list incorrect!'
    assert response.status_code == 200, 'Response status code incorrect!'


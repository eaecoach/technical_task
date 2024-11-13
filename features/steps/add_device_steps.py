import requests
from behave import *
import json



@given("I have added a device")
def test_add_device_step(context):
    header = {'Content-Type': 'application/json'}
    body = {"DeviceName": "device_3_for_testing_behave"}
    context.response = requests.post('http://localhost:8080/device/add', data=json.dumps(body), headers=header)
    assert context.response.json() == 'Successfully added device - device_3_for_testing_behave!', 'Add device response incorrect! ' + str(context.response.json())
    assert context.response.status_code == 200, 'Add device status code incorrect!'


@when("Check added device")
def check_added_device(context):
    context.reservation_response = json.dumps(str(requests.get('http://localhost:8080/reservation')))


@then("I see correct status and response")
def check_add_device_response(context):
    for i in range(len(context.reservation_response)):
        if 'device_3' == context.reservation_response[i][0]:
            assert context.reservation_response[i] == {
        "DeviceName": 'device_3_for_testing_behave',
        "ReservationStatus": "free",
        "ReservationPeriod": {
            "From": "none",
            "To": "none"
        },
        "ReservationOwner": "none"
    }


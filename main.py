# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from flask import *
import json, time

app = Flask(__name__)
reservations = [{
        "Device name": "default_device",
        "Reservation status": "reserved",
        "Reservation period": {
            "From": "2022-08-05",
            "To": "2022-08-10"
        },
        "Reservation owner": "default_owner"
    }]

devices = ['default_device']

@app.route('/reservation', methods=['GET'])
def get_reservations():
    data_set = reservations
    response = app.response_class(
        response=json.dumps(data_set),
        status=200,
        mimetype='application/json'
    )

    return response


@app.route('/user/', methods=['GET'])
def users_page():
    user = str(request.args.get('user')) #/user/?user=SOME_USER
    data_set = {'Page': 'Home', 'Info': f'some user {user}', 'time': time.time()}
    json_text = json.dumps(data_set)

    return json_text


@app.route('/device/add', methods=['POST'])
def device_add():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        device = request.json
        device_name = device['Device name']
        if device_name in devices:
            message = 'Device already exists!'
            status = 400
        else:
            devices.append(device_name)
            message = f'Successfully added device - {device_name}!'
            status = 200
    else:
        message = 'Content-Type not supported!'
        status = 400

    response = app.response_class(
        response=json.dumps(message),
        status=status,
        mimetype='application/json'
    )

    return response


@app.route('/device/del/', methods=['DELETE'])
def device_del():
    device_id = str(request.args.get('id'))
    if device_id in devices:
        devices.remove(device_id)
        message = f'Removed device - {device_id}!'
        status = 200
    else:
        message = 'Device not found!'
        status = 404

    response = app.response_class(
        response=json.dumps(message),
        status=status,
        mimetype='application/json'
    )

    return response


@app.route('/reservation/create', methods=['GET'])
def reservation_create():
    data_set = reservations
    json_text = json.dumps(data_set)

    return json_text


if __name__ == '__main__':
    app.run(port=8080)


#for id, devices in enumerate(reservations):
    #    if devices['Device name'] == device_id:
    #        reservations.pop(id)

from flask import *
import json, time

app = Flask(__name__)
reservations = [{
        "DeviceName": "default_device",
        "ReservationStatus": "reserved",
        "ReservationPeriod": {
            "From": "2022-08-05",
            "To": "2022-08-10"
        },
        "ReservationOwner": "default_owner"
    }]


@app.route('/reservation', methods=['GET'])
def get_reservations():
    data_set = reservations
    response = app.response_class(
        response=json.dumps(data_set),
        status=200,
        mimetype='application/json'
    )

    return response


@app.route('/device/add', methods=['POST'])
def device_add():
    exists = False
    device = request.json
    device_name = device['DeviceName']
    for i in range(len(reservations)):
        if device_name == reservations[i]['DeviceName']:
            message = 'Device already exists!'
            status = 400
            exists = True

    if not exists:
        new_device = {
    "DeviceName": f'{device_name}',
    "ReservationStatus": "free",
    "ReservationPeriod": {
        "From": "none",
        "To": "none"
        },
    "ReservationOwner": "none"
    }
        reservations.append(new_device)
        message = f'Successfully added device - {device_name}!'
        status = 200


    response = app.response_class(
        response=json.dumps(message),
        status=status,
        mimetype='application/json'
    )

    return response


@app.route('/device/del', methods=['DELETE'])
def device_del():
    delete = False
    index = []
    device_id = str(request.args.get('id'))
    for i in range(len(reservations)):
        if device_id == reservations[i]['DeviceName']:
            delete = True
            index.append(i)
            message = f'Removed device - {device_id}!'
            status = 200
        else:
            message = 'Device not found!'
            status = 404
    if delete:
        for ind in sorted(index, reverse=True):
            del reservations[ind]

    response = app.response_class(
        response=json.dumps(message),
        status=status,
        mimetype='application/json'
    )

    return response


@app.route('/reservation/create', methods=['POST'])
def reservation_create():
    new_reservation = request.json
    for i in range(len(reservations)):
        if new_reservation['DeviceName'] == reservations[i]['DeviceName'] and \
                reservations[i]['ReservationStatus'] == 'free':
            reservations.pop(i)
            reservations.append(new_reservation)
            message = 'Reservation has been made!'
            status = 201
        elif new_reservation['DeviceName'] != reservations[i]['DeviceName']:
            message = 'Device not found, reservation not made!'
            status = 404
        else:
            new_date_to = time.strptime(new_reservation['ReservationPeriod']['To'], '%Y-%m-%d')
            new_date_from = time.strptime(new_reservation['ReservationPeriod']['From'], '%Y-%m-%d')
            date_to = time.strptime(reservations[i]['ReservationPeriod']['To'], '%Y-%m-%d')
            date_from = time.strptime(reservations[i]['ReservationPeriod']['From'], '%Y-%m-%d')
            if (date_from <= new_date_from <= date_to or date_from <= new_date_to <= date_to) or \
                    (date_from <= new_date_from <= date_to or date_from <= new_date_to <= date_to):
                message = 'Device already reserved for period: ' + str(reservations[i]['ReservationPeriod']['From']) +\
                          ' - ' + str(reservations[i]['ReservationPeriod']['To']) + \
                          '. Reservation not made!'
                status = 400
            else:
                reservations.append(new_reservation)
                message = 'Reservation has been made!'
                status = 201

    response = app.response_class(
        response=json.dumps(message),
        status=status,
        mimetype='application/json'
    )

    return response


@app.route('/reservation/cancel', methods=['DELETE'])
def reservation_cancel():
    count = 0
    device_remove = False
    cancel_reservation = request.json
    for i in range(len(reservations)):
        if cancel_reservation['DeviceName'] == reservations[i]['DeviceName'] and \
                reservations[i]['ReservationStatus'] == 'reserved':
            count =+ 1
            if cancel_reservation['ReservationPeriod']['To'] == reservations[i]['ReservationPeriod']['To'] and \
                cancel_reservation['ReservationPeriod']['From'] == reservations[i]['ReservationPeriod']['From'] and \
                cancel_reservation['ReservationOwner'] == reservations[i]['ReservationOwner']:
                device_remove = True
                device_id = i
                message = 'Reservation has been canceled!'
                status = 200
            else:
                message = 'Reservation not found!'
                status = 404
        else:
            message = 'Reservation not found!'
            status = 404

    if count == 1 and device_remove:
        device = {
            "DeviceName": f'{cancel_reservation["DeviceName"]}',
            "ReservationStatus": "free",
            "ReservationPeriod": {
                "From": "none",
                "To": "none"
            },
            "ReservationOwner": "none"
        }
        reservations.append(device)

    if device_remove:
        reservations.pop(device_id)

    response = app.response_class(
        response=json.dumps(message),
        status=status,
        mimetype='application/json'
    )

    return response


if __name__ == '__main__':
    app.run(port=8080)

# technical_task

API covers all needed endpoints, runs locally. Example curls can be found at the end of this README.md. 
Using API:
- pull this repo
- run api_task.py
- API run on localhost

For running test automation manually first the api_task.py should be run locally, while the APIs are hosted use:
1. running all tests - go to tests directory in this repo and use command
```
pytest
```
2. running tests for one endpoint - go to tests directory in this repo and use command example
```
pytest test_add_reservation.py
```
3. running one test - go to tests directory in this repo and use command example
```
pytest test_add_reservation.py::test_add_reservation_check
```
###### Example curls:
###### Get reservations:
```
curl --location --request GET 'http://localhost:8080/reservation'
```
###### Create reservations:
```
curl --location --request POST 'http://localhost:8080/reservation/create' \
--header 'Content-Type: application/json' \
--data-raw '{
        "DeviceName": "example",
        "ReservationStatus": "reserved",
        "ReservationPeriod": {
            "From": "2022-09-20",
            "To": "2022-09-25"
        },
        "ReservationOwner": "example_owner"
    }'
```
###### Cancel reservations:
```
curl --location --request DELETE 'http://localhost:8080/reservation/cancel' \
--header 'Content-Type: application/json' \
--data-raw '{
        "DeviceName": "device_1",
        "ReservationPeriod": {
            "From": "2022-08-27",
            "To": "2022-08-30"
        },
        "ReservationOwner": "default_owner"
    }'
```
###### Add device:
```
curl --location --request POST 'http://localhost:8080/device/add' \
--header 'Content-Type: application/json' \
--data-raw '{
    "DeviceName": "example"
}'
```
###### Delete device:
```
curl --location --request DELETE 'http://localhost:8080/device/del?id=example_device_name'
```

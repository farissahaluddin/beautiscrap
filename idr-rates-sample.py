import requests

json_data = requests.get('http://www.floatrates.com/daily/idr.json')
# print(json_data.json())

data_idr = {
    "usd": {"code": "USD", "alphaCode": "USD", "numericCode": "840", "name": "U.S. Dollar", "rate": 6.9248482087728e-5,
            "date": "Fri, 25 Jun 2021 23:55:01 GMT", "inverseRate": 14440.749744278},
    "eur": {"code": "EUR", "alphaCode": "EUR", "numericCode": "978", "name": "Euro", "rate": 5.7971595191573e-5,
            "date": "Fri, 25 Jun 2021 23:55:01 GMT", "inverseRate": 17249.827207538},
    "gbp": {"code": "GBP", "alphaCode": "GBP", "numericCode": "826", "name": "U.K. Pound Sterling",
            "rate": 4.9790187518983e-5, "date": "Fri, 25 Jun 2021 23:55:01 GMT", "inverseRate": 20084.278646646}
}
# print(data_idr)
for data in data_idr.values():
    print(data['code']),
    print(data['name']),
    print(data['date']),
    print(data['rate'])

import requests
import json


result = requests.get('http://ip-api.com/json')
data = json.loads(result.text)


def test_check_country():
    result = requests.get('http://ip-api.com/json')
    data = result.json()

    countryCode = data.get('countryCode')

    assert countryCode == 'RU', 'Country is wrong!'


def test_check_lat():
    lat = data.get('lat')

    assert lat != ''
    assert check_lat(lat), 'You are not in Russia!'


def check_lat(lat):

    if lat < 41.1107 or lat > 81.5035:
        return False

    return True


def test_check_lon():
    lon = data.get('lon')

    assert lon != ''
    assert check_lon(lon), 'You are not in Russia!'


def check_lon(lon):

    if lon < 19.3819 or lon > 169.01:
        return False

    return True


def test_check_region():
    regionName = data.get('regionName')

    assert len(regionName) > 0, 'Region is wrong!'


def test_check_timezone():
    timezone = data.get('timezone')

    assert timezone == 'Europe/Moscow', 'Timezone differs from Moscow'



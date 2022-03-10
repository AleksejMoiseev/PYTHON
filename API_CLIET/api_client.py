import requests
import os
import pytest

BASE_URL = 'http://127.0.0.1:8001/'
EXPECTED_LIST = [
    {'0': 'Alex-0'}, {'1': 'Alex'}, {'2': 'Mariya'}, {'3': 'Fedor'}, {'4': 'Peter_1'},
    {'5': 'Ivan_4'}, {'6': 'Nicola-2'}, {'7': 'Katya'}, {'8': 'Fridrix'}, {'9': 'Kalita'}
]

url = BASE_URL + 'users-1/2'
url1 = os.path.join(BASE_URL, 'users-1/')


params = {'limit': 2, "offset": 1}

params_post = {
        'name': "ANqqqqq"
    }



#res = requests.get(url1, params)
res1 = requests.post('http://127.0.0.1:8001/issues/', params_post)


@pytest.fixture
def url__issues():
    return os.path.join(BASE_URL, 'users-1/')


def test_check_limit(url__issues):
    params = {'limit': 1}
    res = requests.get(url, params)
    assert res.status_code == 200
    assert len(res.json()) == 2

def test_check_offset(url__issues):
    params = {'offset': 1}
    res = requests.get(url, params)
    assert res.status_code == 200




if __name__ == '__main__':
    #res1 = requests.get(url1, {'offset': 1})
    print(res1.json())
import requests
import json
import pytest
from virtualmashine import VirtualMashine


class MockedResponse:
    def __init__(self, text):
        self.text = text


@pytest.fixture
def test_ip_address():
    t = "212.35.191.219"
    return t


@pytest.fixture
def vm_name():
    return "test_vm"


@pytest.fixture(autouse=True)
def virtual_machine(monkeypatch, test_ip_address):
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: MockedResponse(text=test_ip_address))
    return VirtualMashine(name="test_vm")


def test_my_ip_json(virtual_machine, test_ip_address):
    ip_json_str = virtual_machine.my_ip()
    jd = json.loads(ip_json_str)
    print(jd)
    assert 'ip' in jd
    assert test_ip_address == jd['ip']
    assert len(jd) == 1


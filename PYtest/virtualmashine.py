import requests



class VirtualMashine:

    def __init__(self, name):
        self.name = name

    def my_ip(self):
        my_ip_json = requests.get(url="http://icanhazip.com")
        result = my_ip_json.text
        return '{"ip": "%s"}' %result


if __name__ == '__main__':
    vm = VirtualMashine(name='mmm')
    print(vm.my_ip())

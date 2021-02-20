import threading

def tr_print(name):
    print(name)

if __name__ == '__main__':
    obj = threading.Thread(target=tr_print, args=(1,))
    obj.start()

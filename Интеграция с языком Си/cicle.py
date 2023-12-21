from ctypes import *
import os
libname = os.path.abspath("./adder.so")
libc = CDLL(libname)

print('FINISH', libc.loop())
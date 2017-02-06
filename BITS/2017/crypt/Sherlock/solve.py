#! /usr/bin/env python3

import binascii
import sys


def main():
    with open('final.txt', 'r') as f:
        data = f.read()

    table = {}
    string = ''
    
    for i in range(0, len(data)):
        if data[i].isupper():
            if data[i] in table.keys():
                table[data[i]] += 1
            else:
                table[data[i]] = 1
            string += data[i]

    string = string.replace('ZERO', '0')
    string = string.replace('ONE', '1')

    data = int(string, 2)
    flag = binascii.unhexlify('%x' % data).decode()
    
    print(flag)
            
    
                

if __name__ == '__main__':
    main()

#!/usr/bin/env python

"""
 Modbus TestKit: Implementation of Modbus protocol in python

 (C)2009 - Luc Jean - luc.jean@gmail.com
 (C)2009 - Apidev - http://www.apidev.fr

 This is distributed under GNU LGPL license, see license.txt
"""

import sys

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import serial
import random


#PORT = 0
PORT = '/dev/ttyUSB1'

def main():
    """main"""
    logger = modbus_tk.utils.create_logger(name="console", record_format="%(message)s")

    #Create the server
    server = modbus_rtu.RtuServer(serial.Serial(port=PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0))


    try:
        logger.info("running...")
        logger.info("enter 'quit' for closing the server")

        server.start()

        slave_1 = server.add_slave(1)
 #       slave_1.add_block('0', cst.HOLDING_REGISTERS, 0x200, 8)
        slave_1.add_block('0', cst.ANALOG_INPUTS, 0x200, 8)
        slave_1.set_values('0',0x200,0x3131)
        slave_1.set_values('0',0x201,0x3131)
        slave_1.set_values('0',0x202,0x3131)
        slave_1.set_values('0',0x203,0x3131)
        slave_1.set_values('0',0x204,0x3131)
        slave_1.set_values('0',0x205,0x3131)
        slave_1.set_values('0',0x206,0x3131)
        slave_1.set_values('0',0x207,0x3131)
#        slave_1.add_block('1', cst.ANALOG_INPUTS, 0x208, 8)
#        slave_1.set_values('1',0x208,0x3232)
#        slave_1.set_values('1',0x209,0x3232)
#        slave_1.set_values('1',0x20A,0x3232)
#        slave_1.set_values('1',0x20B,0x3232)
#        slave_1.set_values('1',0x20C,0x3232)
#        slave_1.set_values('1',0x20D,0x3232)
#        slave_1.set_values('1',0x20E,0x3232)
#        slave_1.set_values('1',0x20F,0x3232)
        slave_1.add_block('2', cst.ANALOG_INPUTS, 0x210, 8)
        slave_1.set_values('2',0x210,0x3333)
        slave_1.set_values('2',0x211,0x3333)
        slave_1.set_values('2',0x212,0x3333)
        slave_1.set_values('2',0x213,0x3333)
        slave_1.set_values('2',0x214,0x3333)
        slave_1.set_values('2',0x215,0x3333)
        slave_1.set_values('2',0x216,0x3333)
        slave_1.set_values('2',0x217,0x3333)
        slave_1.add_block('3', cst.ANALOG_INPUTS, 0x218, 8)
        slave_1.set_values('3',0x218,0x3434)
        slave_1.set_values('3',0x219,0x3434)
        slave_1.set_values('3',0x21A,0x3434)
        slave_1.set_values('3',0x21B,0x3434)
        slave_1.set_values('3',0x21C,0x3434)
        slave_1.set_values('3',0x21D,0x3434)
        slave_1.set_values('3',0x21E,0x3434)
        slave_1.set_values('3',0x21F,0x3434)


        while True:
            cmd = sys.stdin.readline()
            args = cmd.split(' ')

            if cmd.find('quit') == 0:
                sys.stdout.write('bye-bye\r\n')
                break

            elif args[0] == 'add_slave':
                slave_id = int(args[1])
                server.add_slave(slave_id)
                sys.stdout.write('done: slave %d added\r\n' % (slave_id))

            elif args[0] == 'add_block':
                slave_id = int(args[1])
                name = args[2]
                block_type = int(args[3])
                starting_address = int(args[4])
                length = int(args[5])
                slave = server.get_slave(slave_id)
                slave.add_block(name, block_type, starting_address, length)
                sys.stdout.write('done: block %s added\r\n' % (name))

            elif args[0] == 'set_values':
                slave_id = int(args[1])
                name = args[2]
                address = int(args[3])
                values = []
                for val in args[4:]:
                    values.append(int(val))
                slave = server.get_slave(slave_id)
                slave.set_values(name, address, values)
                values = slave.get_values(name, address, len(values))
                sys.stdout.write('done: values written: %s\r\n' % (str(values)))

            elif args[0] == 'get_values':
                slave_id = int(args[1])
                name = args[2]
                address = int(args[3])
                length = int(args[4])
                slave = server.get_slave(slave_id)
                values = slave.get_values(name, address, length)
                sys.stdout.write('done: values read: %s\r\n' % (str(values)))

            else:
                sys.stdout.write("unknown command %s\r\n" % (args[0]))
    finally:
        server.stop()

if __name__ == "__main__":
    main()

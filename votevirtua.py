import hashlib
import binascii

class Vote_Virtua:
    def __init__(self, vno, vpn, v, vm, va):
        self.vno = vno # Voter Number (#No)
        self.vpn = vpn # Voter's Private Number (Random, "R")
        self.v = v # Vote
        self.vm = vm # Vote Message
        self.va = va # Voting Authority

    def funcha(self):
        md5 = hashlib.md5()

        user_input = input("Enter a Voter's Binary value: ")

        fmt_str = print("{}".format(int(user_input, 2)))
        data_str = binascii.a2b_hex(fmt_str + str(self.vno) + str(self.vpn) + str(self.v) + str(self.vm) + str(self.va))

        md5.update(data_str)
        return md5.hexdigest()

def return_funcha():
    return Vote_Virtua

def nhbs(lbs):
    _vno = lbs.vno
    _vpn = lbs.vpn
    _v = lbs.v
    _vm = lbs.vm
    _va = lbs.va

    return Vote_Virtua(_vno, _vpn, _v, _vm, _va)

lvv = [return_funcha()] # Last Virtual Vote Hash Block Segment

pbs = lvv[0] # Previous (Hash) Block Segment

add_no = 8

for i in range(0, add_no):
    vv2a = nhbs(pbs)
    lvv.append(vv2a)
    pbs = vv2a

    print("Awaiting input of Bill of Lading Details:\n")
    bol2a = input(bol2a)

    print("Voter String Message to Concatenated Hex Digest:\n #{}#{}#{}#{}#{}".format(vv2a.vno, vv2a.vpn, vv2a.v, vv2a.vm, vv2a.va))

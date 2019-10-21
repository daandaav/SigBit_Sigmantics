import binascii
import collections
import datetime
import hashlib
import json

#   .: Shorthanded Variable Naming Description :.
#       bol = Bill of Lading#
#       cbol = Create Bill of Lading
#       bol2a = Bill of Lading (to) Add
#       ts = Timestamp
#       pow = Proof-of-Work
#       hbs = Hash Block Segment
#       nhbs = Next Hash Block Segment
#       hbc = Hash Block Chain
#       pbs = Previous (Hash) Block Segment
#       hb2a = Hash Block (to) Add

Bill = collections.namedtuple('Lading', ['dataset'])

class BoL:

    dataset = "issuer shipper consignee notif_addr vessel freight port_loading port_discharge contents ts invoice".split()

    def __init__(self):
        self._bill_ = [Bill(dataset) for dataset in self.dataset]

    def hashbol(self):
        md5 = hashlib.md5()
        md5.update(str(self._bill_))

        return md5.hexdigest()

    def _eBill_(self, set):
        return self._bill_[set]

def returnBoL():
    return BoL

def nextbol(lastbol):
    this_lastbol = BoL._eBill_
    return this_lastbol

class Hash_Block:
    def __init___(self, gene_bloc, prev_hash, data, curr_hash, bol, ts):
        self.gene_bloc = []
        self.prev_hash = []
        self.data = data
        self.curr_hash = []
        self.chain = []
        self.bol = BoL
        self.ts = ts
        self.hb = self.hb()

def transact(self, prev_bloc, next_bloc, tras_val):
    self.curr_hash.append({
        'prev_bloc' : prev_bloc,
        'next_bloc' : next_bloc,
        'tras_val' : tras_val
    })

    return self.prev_hash['hash_index_val'+1]

def gene(self, prev_hash, pow): # Generate: Genesis Block
    gene_bloc = {'hash_index_val':len(self.chain)+1, 'transact':self.transact, 'proof_of_work':pow, 'prev_hash':prev_hash}
    return gene_bloc, Hash_Block(0, BoL, datetime.datetime.now(), "Genesis", prev_hash=1, pow=1028)

def hbs(self):
    gene_line = json.dumps(self.gene_bloc, sort_keys=True).encode()
    bina_gene = binascii.a2b_hex(gene_line)

    md5 = hashlib.md5(bina_gene)
    md5.update(str(self.prev_hash) + str(self.data) + str(self.curr_hash) + str(
        self.bol) + str(self.ts) + str(bina_gene))

    return md5.hexdigest()

def nhbs(lbs):
    this_prev_hash = lbs.prev_hash + 1
    this_ts = datetime.datetime.now()
    this_data = lbs.data
    this_curr_hash = lbs.curr_hash
    this_bol = lbs.bol

    return Hash_Block(this_prev_hash, this_data, this_curr_hash, this_bol, this_ts)

chbol = [returnBoL()]
hbc = [gene(0, prev_hash=1+1,pow=1028+1)]

prevbol = chbol[0]

pbs = hbc[0]
in_range = 16

for i in range(0, in_range):
    hb2a = nhbs(pbs)
    hbc.append(hb2a)
    pbs = hb2a

    bol2a = nextbol(prevbol)
    chbol.append(bol2a)
    prevBoL = bol2a

    with open('bol_file.md') as f:
        print("Awaiting input of Bill of Lading Details:\nInput ...\tIssuer\nConsignee\nShipper\nInvoice\n")
        user_BoL_INPUT = input(BoL._eBill_)
        print("{BoL._eBill_}")

        user_boli_PRINT = print("BoL Issuer: {}\n".format(user_BoL_INPUT))
        user_hashboli_Print = print("BoL Hash String Value: {}\n".format(bol2a))

        user_block_PRINT = print("For ...\nBlock Segment #{} added!".format(hb2a.data))
        user_hash_PRINT = print("Hash : {}\n".format(hb2a.curr_hash))

        f.write(user_boli_PRINT, user_hashboli_Print, user_block_PRINT, user_hash_PRINT)

    json.dump('bol_file.md', f)
    json.load(f)
#!/bin/env python3

from os import walk
from scapy.all import *

CAPTURE_PATH = './captures'
CAPTURE_LIST=next(walk(CAPTURE_PATH))[2]
OUTPUT_DIR = './output'

ts = time.time()

output_file = f'flowmatrix_{int(ts)}.txt'

_processed_pkt = 0

buffer = []

def get_headers(header, attributes):
    res = ''
    for attr in attributes:
        print(f"trying {header.attr}")
        try:
            stub = header.attr
        except :
            stub = ''
        res = res + stub
    return res
        

for capture in CAPTURE_LIST:

    print(f"Processing \"{capture}\"...")
    SAMPLE= f"{CAPTURE_PATH}/{capture}"

    _new_pkt = 0

    record = rdpcap(SAMPLE)
    for pkt in record:
        if IP in pkt:
            _processed_pkt = _processed_pkt + 1
            headers=pkt[IP]

            if UDP in pkt:
                proto='udp'
            elif TCP in pkt:
                proto='tcp'

            sample = proto
            for attr in ['src', 'sport', 'dst', 'dport']:
                try:
                    stub = getattr(headers, attr)
                except :
                    stub = ''
                sample = f"{sample},{stub}"

            if sample not in buffer:
                buffer.append(sample)
                _new_pkt = _new_pkt + 1

    print(f"Processed packets until now : {_processed_pkt}")
    if _new_pkt > 0:
        print(f"New packets : {_new_pkt}")
    print()

    print(f"Done processing \"{capture}\".\n")

flows_matrix = ['protocol,src ip,src port,dst ip,dst port'] + sorted(buffer)

with open(f"{OUTPUT_DIR}/{output_file}", 'w') as output:
    for flow in flows_matrix:
        output.write(f"{flow}\n")
        print(flow)

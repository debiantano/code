#!/usr/bin/python3
import os

malicious_files=["exploit1", "exploit2", "exploit3"]

for item in malicious_files:
    print(os.path.basename(item))

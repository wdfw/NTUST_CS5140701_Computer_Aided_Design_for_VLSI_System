#!/bin/python3

import os 
TESTCASES = [   "5xp1.blif", "9symml.blif",  "alu4.blif",  "apex4.blif",  
                "dalu.blif",  "e64.blif",  "ex1010.blif",  "ex5p.blif",  
                "i9.blif",  "pdc.blif",  "sample.blif",  "x4.blif"]

EXE="bin/multilevel"
INPUT_DIR="testcase"
OUTPUT_DIR="output"

for testcase in TESTCASES :
    os.system(f"{EXE} {INPUT_DIR}/{testcase} {OUTPUT_DIR}/{testcase}")

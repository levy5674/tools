#!/usr/bin/env python

"""
tool that reads jsons files, normalizes (sorts keys, indents) then prints the md5
"""
import argparse
from glob import glob
import json
from md5 import md5

def check_fp(f):
	docs = map(json.loads, f)
	combined = json.dumps(docs, sort_keys=True, indent=2)
	return md5(combined).hexdigest()

def check_fn(filename):
	with open(filename) as f:
		return check_fp(f)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Compute md5 of normalized jsons file')
	parser.add_argument("-p", "--pattern", type=str, help="glob pattern of jsons files", default="*jsons")
	args = parser.parse_args()
	files = sorted(glob(args.pattern))
	for fn in files:
		print("%s\t%s" % (fn, check_fn(fn)))
#!/usr/bin/env python

import argparse

from numpy.random import shuffle, seed

def random_pw(n=8, allow_specials=True):
	seed()
	valid = map(chr, range(ord('a'), ord('z') + 1))
	valid += map(str.upper, valid)
	valid += map(str, range(10))
	if allow_specials:
		valid += list('!@#$%^&*()')
	shuffle(valid)
	return ''.join(valid[:n])

	
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Generate N character random password (numbers, letters, specials)')
	parser.add_argument('-N', type=int, default=8)
	parser.add_argument('--no_specials', action='store_true')
	args = parser.parse_args()
	print(random_pw(args.N, not args.no_specials))

#!/usr/bin/python3

import hashlib
import argparse
from functools import partial

# add command line arguments i.e. brutemd5 --md5 /path/to/file <hash_value>
# refactor entire script to better code

def md5(word):
        hashMD5 = hashlib.md5()
        hashMD5.update(word.encode())
        return hashMD5.hexdigest()

def sha1(word):
        hashSHA1 = hashlib.sha1()
        hashSHA1.update(word.encode())
        return hashSHA1.hexdigest()

def sha224(word):
        hashSHA224 = hashlib.sha224()
        hashSHA224.update(word.encode())
        return hashSHA224.hexdigest()

def sha256(word):
        hashSHA256 = hashlib.sha256()
        hashSHA256.update(word.encode())
        return hashSHA256.hexdigest()

def sha512(word):
        hashSHA512 = hashlib.sha512()
        hashSHA512.update(word.encode())
        return hashSHA512.hexdigest()

def hash_mode(hash_type):
        switcher = {
                'md5': md5,
                'sha1': sha1,
                'sha224': sha224,
                'sha256': sha256,
                'sha512': sha512
        }
        func = switcher.get(hash_type)
        return func

# TODO better implementation of cli - make arguments like -host <host> -username <username>
# maybe its better to check hashes while reading the file than read, then iteragte through it again
# define default set of files to search for hash?
def read_file(path_to_file):
        try:
                f = open(path_to_file, "r", encoding="ISO-8859-1")
        except:
                print('Couldn\'t open file ' + path_to_file)
                quit()
        words = []
        for line in f:
                words.append(line[:-1])
        f.close()
        return words

def init_args():
        parser = argparse.ArgumentParser()
        parser.add_argument("hash_type", help="type of hash to crack") #md5, sha1, sha224, sha256, sha512
        parser.add_argument("hash_value", help="value of hash to identify")
        parser.add_argument("wordlist", help="path to file with words to check")
        args = parser.parse_args()
        return args

def main():
        args = init_args()
        hash_func = hash_mode(args.hash_type)
        words = read_file(args.wordlist)
        for word in words:
                if args.hash_value == hash_func(word):
                        print('Found solution for entered hash: ' + word)
                        exit(0)

main()

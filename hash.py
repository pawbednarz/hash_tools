#!/usr/bin/python3

import hashlib

value = str(input('Enter data to hash:\n'))

hashMD5 = hashlib.md5()
hashMD5.update(value.encode())
print('MD5 - ' + hashMD5.hexdigest())

hashSHA1 = hashlib.sha1()
hashSHA1.update(value.encode())
print('SHA1 - ' + hashSHA1.hexdigest())

hashSHA224 = hashlib.sha224()
hashSHA224.update(value.encode())
print('SHA224 - ' + hashSHA224.hexdigest())

hashSHA256 = hashlib.sha256()
hashSHA256.update(value.encode())
print('SHA256 - ' +hashSHA256.hexdigest())

hashSHA512 = hashlib.sha512()
hashSHA512.update(value.encode())
print('SHA512 - ' + hashSHA512.hexdigest())

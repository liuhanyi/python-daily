#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

import hashlib

def sign(params):
    param_list = ["%s=%s" % (k, v) for k, v in params.items()]
    param_list.sort()
    param_list.append('242ece4afde95a049d7afc7b916d008a')
    print(param_list)

    print(hashlib.algorithms_available)
    md5_hash = hashlib.md5()
    md5_hash.update('|'.join(param_list).encode('utf8'))
    print(md5_hash.hexdigest())

if __name__ == '__main__':
    params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
    sign(params)

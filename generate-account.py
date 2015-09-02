#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import requests

def getConnection(url, user, passwd, db=None, charset='utf8'):
    if db == None:
        db = user
    return MySQLdb.connect(host=url, user=user, passwd=passwd, db=db, charset=charset)


def generateAccount():
    # change the url
    conn = getConnection('192.168.56.10','develop', '123456', 'prague')
    cur = conn.cursor()

    sql = "replace into t_origin_account_user(user_name, name, role_id) values('test{}', '测试', 3)"
    rsql = "replace into t_origin_user_resource(user_name, resource_id) values('test{}', 1)"
    for i in range(20, 101):
        cur.execute(sql.format(i))
        cur.execute(rsql.format(i))
        conn.commit()

    cur.close()
    conn.close()


def getUserAgent():
    print(requests.get('https://httpbin.org/user-agent').text)

if __name__ == '__main__':
    getUserAgent()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

def getConnection(url, user, passwd, db=None, charset='utf8'):
    if db == None:
        db = user
    return MySQLdb.connect(host=url, user=user, passwd=passwd, db=db, charset=charset)


def generateAccount():
    conn = getConnection('10.10.90.156','develop', 'p3m12d', 'prague')
    cur = conn.cursor()

    sql = "replace into t_origin_account_user(user_name, name, role_id) values('test{}', '测试', 3)"
    rsql = "replace into t_origin_user_resource(user_name, resource_id) values('test{}', 1)"
    for i in range(20, 101):
        cur.execute(sql.format(i))
        cur.execute(rsql.format(i))
        conn.commit()

    cur.close()
    conn.close()

if __name__ == '__main__':
    generateAccount()
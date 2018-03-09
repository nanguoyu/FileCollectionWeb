# coding=utf-8
from __future__ import print_function
from datetime import date
import datetime
from dbconnect.dbmanage import db_manage
import json
import logging
import time

logging.basicConfig(filename=time.strftime("%Y-%m-%d", time.localtime()) + 'easkongadmin_database.log',
                    level=logging.DEBUG)
logging.info(time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()) + 'mention_database start')


def db2json(dbname):
    # type: (object) -> object
    # db应为字符串类型
    db = db_manage()
    result = db.queryall(dbname)
    db.close()
    logging.info(time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()) + 'db2json')
    return json.dumps(result, cls=ComplexEncoder)


def query2json(sql):
    # sql 应为字符串类型的sql语句
    db = db_manage()
    result = db.query(sql)
    db.close()
    logging.info(time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()) + 'query2json')
    return json.dumps(result, cls=ComplexEncoder)


def update2json(sql):
    db = db_manage()
    result = db.updae(sql)
    db.close()
    logging.info(time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()) + 'update2json')
    return result


def datetime_now():
    # 返回明天对应的现在时刻
    return (datetime.datetime.today()).strftime('%Y-%m-%d')


def datetime_after(n):
    return (datetime.datetime.now() + datetime.timedelta(days=n)).strftime('%Y-%m-%d')


def result2json(result):
    return json.loads(result)


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

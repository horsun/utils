import os
import time

import pymysql

target_dbUser = 'root'
target_dbpwd = '123456'
dbHost = '127.0.0.1'
target_database = 'mysql'
dbCharset = 'utf8'
target_dir = '/home/horsun/Desktop'
date = time.strftime("%Y%m%d")

# 查出MySQL中所有的数据库名称
sqlStr1 = "show databases like '{0}'".format(target_database)
print(sqlStr1)
try:
    connDB = pymysql.connect(dbHost, target_dbUser, target_dbpwd, )
    connDB.select_db(target_database)
    cursor = connDB.cursor()
    cursor.execute(sqlStr1)
    allDatabase = cursor.fetchall()
    if target_database in allDatabase[0]:
        fileName = '%s/%s_%s.sql' % (target_dir, date, target_database)
        if os.path.exists(fileName):
            os.remove(fileName)
        os.system("mysqldump -h%s -u%s -p%s %s --default_character-set=%s > %s/%s_%s.sql" % (
            dbHost, target_dbUser, target_dbpwd, target_database, dbCharset, target_dir, date, target_database))
        # TODO
        # email / cos storage/....
    else:
        print('database is not exist!')
except pymysql.Error as msg:
    # 异常
    print(" error :", str(msg))

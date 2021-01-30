#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 10:36:51 2021

@author: douglasbzzz
"""
import mysql.connector
from mysql.connector import errorcode


def conn():
    try:
        db_connection = mysql.connector.connect(host='localhost', user='root', password='DouglasMysqlMac',
                                                database='python_migration')
        print("Sucesso!")
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Banco de dados nao existe")
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("user ou password incorretos")
        else:
            print(error)
    else:
        db_connection.close()


#conexao = PyDO()
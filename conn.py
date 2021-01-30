from datetime import date
import mysql.connector
#print(cursor.fetchall())

class Conn:
    def conexao(self):

        conexao = mysql.connector.connect(host='localhost', user='root', password='DouglasMysqlMac',
                                      database='python_migration')

        cursor = conexao.cursor()

        sql = "select * from pessoas"
        cursor.execute(sql)
    #def cursor(self):

# to querendo dar um jeito de levar essa responsa pra outra entidade tomar conta. :/

import mysql.connector
import datetime

class Dao():

    ''' Executa query'''
    def _execute(self, sql, param=None, select=False):
        con = mysql.connector.connect(*self._args,**self._kwargs)
        cur = con.cursor()
        try:
            cur.execute(sql, param)
        except mysql.connector.DatabaseError as e:
            return False
        if select:
            dados = []
            for reg in cur.fetchall():
                dados.append(self._dict_factory(cursor=cur, row=reg))
        else:
            dados = True
            con.commit()
        con.close()
        return dados

    ''' Converte para dicionário'''
    def _dict_factory(self, cursor, row):
        # print(cursor.description)
        dicionario = {}
        for item in enumerate(cursor.column_names):
            dicionario[item[1]] = row[item[0]]
        return dicionario

    ''' Agora '''
    def _now(self):
        return datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')


    def desconnect(self):
        pass
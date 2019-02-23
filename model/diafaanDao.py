from model.dao import Dao
class DiafaanDao(Dao):

    def __init__(self,*args,**kwargs):
        self._args,self._kwargs = args,kwargs
        super(DiafaanDao, self).__init__()

    def insert_answer(self,database_table,time,sms_from,sms_to,sms_text):
        sql = "insert into {}(SendTime,MessageFrom,MessageTo,MessageText) values ('{}','{}','{}','{}');".format(database_table,time,sms_from,sms_to,sms_text)
        return self._execute(sql=sql)
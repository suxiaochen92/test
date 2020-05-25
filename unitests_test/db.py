import pymysql
import traceback

class Db:
    def __init__(self,host,user,password,db,port):
        self.host=host
        self.user=user
        self.password=password
        self.db=db
        self.port=port
    def query(self,sql):
        db=pymysql.connect(host=self.host,user=self.user,password=self.password,db=self.db,port=self.port)
        try:
            cursor=db.cursor()
            cursor.execute(sql)
            res=cursor.fetchall()
            db.close()
            return res
        except:
            traceback.print_exc()
            return 'False'
    def commit(self,sql):
        db=pymysql.connect(host=self.host,user=self.user,password=self.password,db=self.db,port=self.port)
        try:
            cursor=db.cursor()
            cursor.execute(sql)
            db.commit()
            db.close()
            return 'True'
        except Exception as e:
            return 'False{e}'.format(e=e)
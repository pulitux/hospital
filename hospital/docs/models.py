from django.db import models
import cx_Oracle

class Doctor:
    def __init__(self):
        self.connection = cx_Oracle.connect(user='system', password='pythonoracle', dsn='localhost/XE')


    def por_hospital(self, hospitales):
        cursor = self.connection.cursor()

        try:
            consulta = 'select * from doctor where HOSPITAL_COD in {{hospitales}}'
            cursor.execute(consulta)
            return cursor
        except self.connection.Error as e:
            print ('Error: ', e)



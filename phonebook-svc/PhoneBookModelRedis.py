import redis
import uuid
import os
import json

#redis library python
#https://pypi.org/project/redis/

class PhoneBook:
    def __init__(self):
        self.server = os.getenv('REDIS_SERVER') or 'redis-server'
        # ip server dibawah ini hanya untuk testing tanpa harus masuk container
        # untuk mengetahui ip dari redis-server gunakan docker inspect redis-server
        #self.server = '172.22.0.2'
        self.db =redis.Redis(host=self.server, port=6379, db=0)
    def list(self):
        data = []
        try:
            for i in self.db.keys():
                #data.append(dict(id=i,data=self.db[i]))
                data.append(self.read(i))
            return dict(status='OK',data=data)
        except:
            return dict(status='ERR',msg='Error')
    def create(self,info):
        #info harus dalam bentuk string
        try:
            id = str(uuid.uuid1())
            if (type(info)==dict):
                #string harus diencode menjadi bytes (agar bisa disimpan)
                info = json.dumps(info).encode()
            self.db.set(id,info)
            return dict(status='OK',id=id)
        except Exception as e:
            return dict(status='ERR',msg='Tidak bisa Create',errmsg=str(e))
    def delete(self,id):
        try:
            self.db.delete(id)
            return dict(status='OK',msg='{} deleted' . format(id), id=id)
        except:
            return dict(status='ERR',msg='Tidak bisa Delete')
    def update(self,id,info):
        try:
            if (type(info)==dict):
                info = json.dumps(info).encode()
            if self.db.get(id) is None:
                raise
            self.db.set(id,info)
            return dict(status='OK',msg='{} updated' . format(id), id=id)
        except:
            return dict(status='ERR',msg='Tidak bisa Update')
    def read(self,id):
        try:
            return dict(status='OK',id=id.decode(),data=json.loads(self.db.get(id).decode()))
        except:
            return dict(status='ERR',msg='Tidak Ketemu')
    def clear(self):
        try:
            self.db.flushall()
        except:
            return dict(status='ERR',msg='Tidak Ketemu')





if __name__=='__main__':
    pd = PhoneBook()
    pd.clear()
#    ----------- create
    result = pd.create(dict(nama='royyana',alamat='ketintang',notelp='6212345'))
    print(result)
    result = pd.create(dict(nama='ibrahim',alamat='ketintang',notelp='6212341'))
    print(result)
    result = pd.create(dict(nama='Ananda', alamat='Dinoyo Sekolahan', notelp='6212345'))
    print(result)
#    ------------ list
#    print(pd.list())
#    ------------ info
    result = pd.update('9fd1df70-3c0b-11eb-988d-cb63b512d357',dict(nama='john',alamat='portugal',notelp='123123'))
    print(result)

#    print(pd.read('c516b780-2fa2-11eb-bf35-7fc0bd24c845'))
    for x in pd.list()['data']:
        id = x['id']
        nama = x['data']['nama']
        alamat = x['data']['alamat']
        print(f"{id} {nama} {alamat}")
    #pd.clear()
    #print(pd.list())




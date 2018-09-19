import RWaerospike
import sys
from RWaerospike.exception import *

class AeroSpikeJob():
    def __init__(self):
        self.main='Aero'
        self.client = None
        self.config = None
        self.db_setname = None

    def ConnectAero(self, Host, Port):
        self.config = {'hosts': [(str(Host), Port)]}
        try:
            self.client = RWaerospike.client(self.config).connect()
            print self.client
        except Exception as e:
            print(e.message)
            sys.exit(1)

    def GetNameSpace(self):
        ns_set_info = self.client.info('sets')
        nameSpaces = {}
        values = ns_set_info.values()[0]
        values = list(values)[1]
        split3 = values.split(';')
        for s in split3:
            if s.__contains__('ns'):
                d = s.split(':')
                val = d[0].replace('ns=', '')
                if val not in nameSpaces:
                    nameSpaces[val]=[]
                    nameSpaces[val].append(d[1].replace('set=', ''))
                else:
                    nameSpaces[val].append(d[1].replace('set=', ''))
        return nameSpaces


    def FetchDataSets(self,namespace,setname,userid,start,stop):
        self.db_setname=setname
        for x in range(start,stop+1):
            dataDict = self.ReadValue(x,namespace,setname)
            self.dpcache.WriteDataToDPCS(0,self.db_setname + userid + str(x), dataDict['Data'])
        value = self.ReadValue(1,namespace,setname)
        return value["Data"].keys()


    def WriteValue(self, KN, NameSpace, DB1, Value):
        key = (str(NameSpace), str(DB1), str(KN))
        try:
            self.client.put(key, {'Data': Value})
        except Exception as e:
            print(e.message)

    def ReadValue(self, KN, NameSpace, DB1):
        try:
            key = (str(NameSpace), str(DB1), str(KN))
            (key, meta, record) = self.client.get(key)
        except Exception as e:
            print (e.message)
        return record


    def FetchData(self,dataset,userid,minimum,maximum,flag):
        try:
            dic = self.dpcache.FetchData(self.db_setname, userid, minimum, maximum)
            if flag==0:
                packet = self.dpcache.Binding_Data(dic,dataset)
                return packet
            else:
                return dic
        except:
            raise


    def Close(self):
        self.client.close();
        return 1
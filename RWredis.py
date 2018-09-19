import redis

import ast

class DPCS():

    def __init__(self):
        self.name   ='DPCS'
        self.DPCSIP = '127.0.0.1'
        self.DPCSPort = 6380


    def WriteDataToDPCS(self, DB, Key, Data):
        try:
            DPCS = redis.StrictRedis(host=str(self.DPCSIP), port=self.DPCSPort, db=DB)
            DPCS.set(str(Key), Data)
            return True
        except Exception as e:
            print (e.message)

    def ReadDataFromDPCS(self, DB, Key):
        try:
            DPCS = redis.StrictRedis(host=str(self.DPCSIP), port=self.DPCSPort, db=DB)
            return DPCS.get(str(Key))
        except Exception as e:
            print (e.message)

    def Binding_Data(self, dataDict, dataset):
        lst = []
        for x in dataDict:
            packet = {}
            if dataset == "Pi":
                for key in x[dataset]:
                    if key != "FKey":
                        packet[key] = x[dataset][key][:18]
            else:
                for key in x[dataset]:
                    if key != "FKey":
                        packet[key] = x[dataset][key]
            lst.append(packet)
        return lst


    def FetchData(self,dbname,userid,minkey,maxkey):
        count = minkey
        lst = []
        while count<=maxkey:
            try:
                lst.append(ast.literal_eval(self.ReadDataFromDPCS(0,dbname+userid+str(count))))
                count+=1
            except:
                break
        return lst






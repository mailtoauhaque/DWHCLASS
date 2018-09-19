import GenerateData
import RWmongo
import RWredis
#import RWaerospike
import RWcouch
import ast

import json


#Show Generated Data into Console
Masterdict = GenerateData.GenerateData().Generate(4,5)

print ('Stock Data >>')
print (Masterdict['Stock'])
print ('CreditCard Data >>')
print (Masterdict['CreditCard'])
print ('Medical Data >>')
print (Masterdict['Medical'])




# #Writing Data into MongoDB
CollectionName = "ClassCol" #your collection Name
RWmongo.WriteValue(collectionName=CollectionName, KN='2', Value=Masterdict['CreditCard'])


#Writing data into CouchDB
RWcouch.createdbincouch('bdme')
Masterdict_json = json.dumps(str(Masterdict['Medical']))
print (Masterdict_json)
RWcouch.writeincouch(data=Masterdict_json, key='2', dbname='bdme')

#Writing data into Redis
RWredis.DPCS().WriteDataToDPCS(DB='0', Key='2', Data=Masterdict['Stock'])




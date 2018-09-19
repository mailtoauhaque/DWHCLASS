import GenerateData
import RWmongo
import RWredis
#import RWaerospike
import RWcouch
import ast

import json





CollectionName="ClassCol"
#Reading Data from

print ('Data from Mongodb')
Data = RWmongo.ReadValue(CollectionName, '2')
print (Data)
print ('------------------------------------------------------------------------')

Data = RWredis.DPCS().ReadDataFromDPCS(DB='0', Key='2')
print (Data)
print ('------------------------------------------------------------------------')

#
Data = RWcouch.readfromcouch('bdme')
print (Data)
print ('------------------------------------------------------------------------')
#
